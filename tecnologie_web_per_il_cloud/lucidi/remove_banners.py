from pdf2image import convert_from_path
from PIL import Image
import numpy as np
from matplotlib.colors import rgb_to_hsv
import colorsys
import img2pdf
import cv2
import os
import argparse, sys
import glob
from sklearn.cluster import DBSCAN

TEMP_FOLDER = "temp_images"

from enum import Enum
from enum import IntEnum


class BoxDetectionMode(Enum):
    CHUNK = "chunk"
    CONNECTED = "connected"


class RegionMask(IntEnum):
    BACKGROUND = 0
    TEXT = 1
    DARK_BLOCK = 2

# ------------------------
# Funzioni ausiliarie
# ------------------------

def to_grayscale_array(image):
    return np.array(image.convert("L"))  # 8-bit grayscale

def assert_grayscale_color(value):
    if not isinstance(value, (int, np.integer)):
        raise TypeError(f"Expected grayscale color as integer in range [0, 255], got type {type(value)}: {value}")
    if not (0 <= value <= 255):
        raise ValueError(f"Grayscale color must be in range [0, 255], got {value}")

def assert_grayscale_thresholds_color(threshold):
    for bound in threshold:
        assert_grayscale_color(bound if bound is not None else 0)

    
def to_rgb_array(image):
    return np.array(image.convert("RGB"))

def assert_rgb_color(value):
    if not isinstance(value, (tuple, list, np.ndarray)):
        raise TypeError(f"Expected RGB color as tuple/list/array of 3 ints, got type {type(value)}: {value}")
    
    if len(value) != 3:
        raise ValueError(f"RGB color must have exactly 3 components, got {len(value)}: {value}")
    
    for i, channel in enumerate(value):
        if not isinstance(channel, (int, np.integer)):
            raise TypeError(f"RGB channel {i} must be int, got {type(channel)}: {channel}")
        if not (0 <= channel <= 255):
            raise ValueError(f"RGB channel {i} must be in range [0, 255], got {channel}")

def assert_hsv_color(value):
    if not isinstance(value, (tuple, list, np.ndarray)):
        raise TypeError(f"Expected HSV color as tuple/list/array of 3 ints, got type {type(value)}: {value}")
    
    if len(value) != 3:
        raise ValueError(f"HSV color must have exactly 3 components, got {len(value)}: {value}")

    limits [[0, 360], [0, 100], [0, 100]]
    for i, channel in enumerate(value):
        if not isinstance(channel, (int, np.integer)):
            raise TypeError(f"HSV channel {i} must be int, got {type(channel)}: {channel}")
        min_level, max_level = limits[i]
        if not (min_level <= channel <= max_level):
            raise ValueError(f"HSV channel {i} must be in range {limits[i]}, got {channel}")
        

def assert_hsv_thresholds_color(thresholds):
    hsv_lower_bound = []
    hsv_upper_bound = []
    for (lower_bound, upper_bound) in thresholds:
        hsv_lower_bound.append(lower_bound if not None else 0)
        hsv_upper_bound.append(upper_bound if not None else 0)

    assert_hsv_color(hsv_lower_bound)
    assert_hsv_color(hsv_upper_bound)

def compute_dark_binary_mask(gray_array, lower_level = 0, upper_level = 255):
    # pixel con intensità < ligth_upper_level considerati “scuri”
    return gray_array >= lower_level & gray_array <= upper_level

def get_dark_bounding_boxes(dark_binary_mask, min_area=150):
    contours, _ = cv2.findContours(dark_binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = [cv2.boundingRect(cnt) for cnt in contours if cv2.contourArea(cnt) > min_area]
    return boxes

def chunk_density(dark_binary_mask, chunk_size=16, density_thresh=0.6):
    H, W = dark_binary_mask.shape
    dense_blocks = []
    for y in range(0, H, chunk_size):
        for x in range(0, W, chunk_size):
            block = dark_binary_mask[y:y+chunk_size, x:x+chunk_size]
            if block.size == 0:
                continue
            # Maschera pixel scuri
            dark_pixels = np.sum(block)
            density = dark_pixels / block.size
            if density > density_thresh:
                dense_blocks.append((x, y, chunk_size, chunk_size))

    return dense_blocks

    

def cluster_blocks_dbscan(rects, eps=20, min_samples=1):
    # calcolo centri dei rettangoli
    points = np.array([[x + w/2, y + h/2] for (x, y, w, h) in rects])
    
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(points)
    labels = clustering.labels_  # -1 = rumore, 0..n cluster
    
    clusters = {}
    for label, rect in zip(labels, rects):
        if label == -1:
            # rumore, puoi decidere se tenerlo o meno
            continue
        clusters.setdefault(label, []).append(rect)
    
    # Per ogni cluster, calcola il rettangolo bounding che contiene tutti i blocchi
    merged_rects = []
    for cluster_rects in clusters.values():
        xs = [r[0] for r in cluster_rects]
        ys = [r[1] for r in cluster_rects]
        ws = [r[2] for r in cluster_rects]
        hs = [r[3] for r in cluster_rects]

        x_min = min(xs)
        y_min = min(ys)
        x_max = max(x + w for x, w in zip(xs, ws))
        y_max = max(y + h for y, h in zip(ys, hs))

        merged_rects.append((x_min, y_min, x_max - x_min, y_max - y_min))

    return merged_rects


def erode_image(image_array, kernel_size, iterations):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    return cv2.erode(image_array, kernel, iterations=iterations)

def dilate_image(image_array, kernel_size, iterations):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    return cv2.dilate(image_array, kernel, iterations=iterations)


    
# ------------------------
# Funzioni principali
# ------------------------


    
def obtain_inner_text_and_dark_block_masks(
    image_block,
    
    compute_as_gray = False,
    dark_binary_mask=None,
    
    
    use_erode_before_contours_definition = False,
    erode_kernel_size = None,
    erode_iterations = None,
    use_dilate_after_contours_definition = False,
    dilate_kernel_size = None,
    dilate_iterations = None,

    inner_text_threshold_level = None,

    min_text_density=0.4,
    
    debug=False
):

    inner_text_mask = obtain_binary_mask(image_block, compute_as_gray, inner_text_threshold_level)
    
    text_density = np.sum(inner_text_mask) / inner_text_mask.size

    if text_density < min_text_density:
        return np.zeros(image_block.shape, dtype=np.uint8), np.ones(image_block.shape, dtype= np.uint8)

    binary_mask = dark_binary_mask.copy()

    if use_erode_before_contours_definition:
        binary_mask = erode_image(binary_mask * 255, erode_kernel_size, erode_iterations)

    # 4. Trova contorni
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    binary_filled = np.zeros(binary_mask.shape, dtype=np.uint8)
    cv2.drawContours(binary_filled, contours, -1, 1, thickness=-1)


    if use_dilate_after_contours_definition:
        expanded = dilate_image(binary_filled * 255, dilate_kernel_size, dilate_iterations)
        expanded = (expanded > 0)
    else:
        expanded = (binary_filled > 0)

    # 5. Costruisci risultato finale
    return  expanded & inner_text_mask, binary_mask # expanded & ~inner_text_mask
    """
    result = np.ones_like(block) * 255
    result[final_mask] = [0, 0, 0]
    result[~expanded] = block[~expanded]

    if debug:
        print(f"[DEBUG] Text density: {text_density:.2f}, Contours: {len(contours)}")

    return result.astype(np.uint8)
    """





        

class ChunkBlockEroderParams:
    def __init__(self,
                 use_erode=False, erode_kernel_size= (3, 3), erode_iterations=1,
                 use_dilate_after_contours_definition=True, dilate_kernel_size=(3, 3), dilate_iterations= 1, 
                 chunk_size=10, ligth_upper_level=0.75, density_thresh=0.65,
                 dbscan_epsilon=10, dbscan_min_samples=2):
        super().__init__(BoxDetectionMode.CHUNK, use_erode, erode_kernel_size, erode_iterations, use_dilate_after_contours_definition, dilate_kernel_size, dilate_iterations, ligth_upper_level)
        self.chunk_size = chunk_size
        self.density_thresh = density_thresh
        self.dbscan_epsilon = dbscan_epsilon
        self.dbscan_min_samples = dbscan_min_samples

    def get_density_args(self):
        return {
            "chunk_size": self.chunk_size,
            "ligth_upper_level": self.ligth_upper_level,
            "density_thresh": self.density_thresh
        }

    def get_dbscan_args(self):
        return {
            "eps": self.dbscan_epsilon,
            "min_samples": self.dbscan_min_samples
        }


class ConnectedBlockEroderParams:
    def __init__(self, 
                 use_erode=False, erode_kernel_size= (3, 3), erode_iterations=1, 
                 use_erode_before_contours_definition=False, inblock_erode_kernel_size= (3, 3), inblock_erode_iterations=2, 
                 use_dilate_after_contours_definition=True, dilate_kernel_size=(3, 3), dilate_iterations= 1, 
                 ligth_upper_level=200, min_area=150):
        
        super().__init__(BoxDetectionMode.CONNECTED, use_erode, erode_kernel_size, erode_iterations, use_dilate_after_contours_definition, dilate_kernel_size, dilate_iterations, ligth_upper_level)
        self.min_area = min_area
        
        self.use_erode_before_contours_definition = use_erode_before_contours_definition
        self.inblock_erode_kernel_size = inblock_erode_kernel_size
        self.inblock_erode_iterations = inblock_erode_iterations

    def get_connected_args(self):
        return {
            "ligth_upper_level": self.ligth_upper_level,
            "min_area": self.min_area
        }



def compute_ternary_mask_from_blocks(array_image, binary_mask, boxes, compute_masks_fn):
    """
    Ritorna una maschera intera in cui:
    - RegionMask.BACKGROUND  = background
    - RegionMask.TEXT  = testo su blocco scuro
    - RegionMask.DARK_BLOCK  = blocco scuro senza testo
    """
    ternary_mask = np.empty(array_image.shape[:2], dtype=np.uint8)
    ternary_mask.fill(RegionMask.BACKGROUND)

    print(np.unique(binary_mask))

    for (x, y, w, h) in boxes:
        block = array_image[y:y+h, x:x+w]
        block_binary_mask = binary_mask[y:y+h, x:x+w]
        
        # Ritorna due maschere booleane locali del blocco
        inner_text_mask, dark_block_mask = compute_masks_fn(block, block_binary_mask)

        # Costruisci una maschera 0/1/2 del blocco
        local_mask = np.zeros((h, w), dtype=np.uint8)
        local_mask.fill(RegionMask.BACKGROUND)
        local_mask[dark_block_mask] = RegionMask.DARK_BLOCK 
        local_mask[inner_text_mask] = RegionMask.TEXT   # sovrascrive parte del 2

        # Inserisci nella maschera globale
        ternary_mask[y:y+h, x:x+w] = local_mask

    return ternary_mask



def detect_dark_blocks_by_chunks(
    dark_binary_mask,
    chunk_size,
    chunk_density_threshold,
    merge_chunks_with_dbscan,
    chunk_merge_epsilon,
    chunk_merge_min_samples):
    
    boxes = chunk_density(dark_binary_mask,
                          chunk_size= chunk_size,
                          density_thresh = chunk_density_threshold)
    if merge_chunks_with_dbscan:    
        boxes = cluster_blocks_dbscan(boxes, 
                                      eps= chunk_merge_epsilon,
                                      min_samples = chunk_merge_min_samples)
        boxes_to_remove = []
        for i, (x1, y1, w1, h1) in enumerate(boxes):
            for e in range(i+1, len(boxes)):
                x2, y2, w2, h2 = boxes[e]
                if x1 <= x2 and y1 <= y2 and x1 + w1 >= x2 + w2 and y1 + h1 >= y2 + h2:
                    boxes_to_remove.append(e)
        for i in sorted(boxes_to_remove, reverse = True):
            del boxes[i]
    return boxes

def detect_dark_with_connected_components(eroded_dark_binary_mask, connected_component_min_area=150):
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(eroded_dark_binary_mask, connectivity=8)
    boxes = []
    for i in range(1, num_labels):  # 0 è lo sfondo
        x, y, w, h, area = stats[i]
        if area >= connected_component_min_area:
            boxes.append((x, y, w, h))
    return boxes

def box_detection(binary_mask, 
                  detection_mode: BoxDetectionMode = BoxDetectionMode.CONNECTED,
                  use_pre_box_detection_erode = True,
                  erode_kernel_size = (3, 3),
                  erode_iterations = 1,
                  *args, **kwargs):

    unique = np.unique(binary_mask)
    assert len(unique) <=2, f"Box detection supported only on binary masks, found {unique} groups of level"

    if len(unique) < 2:
        return []

    if use_pre_box_detection_erode:
        binary_mask = erode_image(binary_mask * 255, erode_kernel_size, erode_iterations)
        binary_mask = (binary_mask > 0)       
        
    if detection_mode == BoxDetectionMode.CHUNK:
        return detect_dark_blocks_by_chunks(binary_mask,  *args, **kwargs)

    elif detection_mode == BoxDetectionMode.CONNECTED:
        return detect_dark_with_connected_components(binary_mask, *args, **kwargs)
        
    else:
        raise ValueError("Unsupported detection mode.")


def obtain_binary_mask(array_image, compute_as_gray, mask_threshold_level):
    if compute_as_gray:
        assert len(array_image.shape) == 2, f"Image shape expected is (W,H), got {array_image.shape}"
        assert len(mask_threshold_level) == 2, f"Expected only two elements for luminescence level threshold, got {mask_threshold_level}"
        lux_mask = np.ones_like(array_image, dtype=bool)
        l_min, l_max = mask_threshold_level
        if l_min is not None:
            lux_mask &= (array_image >= l_min)
        if l_max is not None:
            lux_mask &= (array_image <= l_max)
        return lux_mask.astype(np.uint8)
        
    else:
        assert array_image.shape[2] == 3, f"Image shape expected is (W,H,3), got {array_image.shape}"
        assert len(mask_threshold_level) == 3, f"Expected only tre elements for hsv level threshold, got {mask_threshold_level}"
        for i, channel in enumerate("HSV"):
            assert len(mask_threshold_level[i]) == 2, f"Expected only two elements for {channel} level threshold, got {mask_threshold_level}"
        r, g, b = array_image[..., 0], array_image[..., 1], array_image[..., 2]
        h, s, v = np.vectorize(colorsys.rgb_to_hsv)(r, g, b)
    
        (h_min, h_max), (s_min, s_max), (v_min, v_max) = mask_threshold_level
    
        h_mask = np.ones_like(h, dtype=bool)
        if h_min is not None:
            h_mask &= (h >= h_min)
        if h_max is not None:
            h_mask &= (h <= h_max)
    
        s_mask = np.ones_like(s, dtype=bool)
        if s_min is not None:
            s_mask &= (s >= s_min)
        if s_max is not None:
            s_mask &= (s <= s_max)
    
        v_mask = np.ones_like(v, dtype=bool)
        if v_min is not None:
            v_mask &= (v >= v_min)
        if v_max is not None:
            v_mask &= (v <= v_max)
    
        return (h_mask & s_mask & v_mask).astype(np.uint8)
        
def select_with_fallback(option1: bool, 
                         default_value=None, 
                         option1_value=None, 
                         option2_value=None):
    """
    Return option1_value if option1 is True, else option2_value.
    If the chosen value is None, return default_value instead.
    This avoids treating falsy values (like 0 or []) as missing.
    """
    selected = option1_value if option1 else option2_value
    return default_value if selected is None else selected


    
def apply_cleanup(
    image, 
    detection_mode: BoxDetectionMode, 
    compute_as_gray = True,
    output_as_gray = False,
    
    output_dark_block_color = None,
    output_dark_block_gray_color = 255,
    output_dark_block_rgb_color = [255, 255, 255],

    output_dark_block_inner_text_color = None,
    output_dark_block_inner_text_gray_color = 0,
    output_dark_block_inner_text_rgb_color = [0 , 0, 0],
    
    
    dark_block_threshold_level = None,
    dark_block_hsv_threshold_level = ((None, None), (None, 100), (None, 100)),
    dark_block_lux_threshold_level = (None, 180),
    
    use_pre_box_detection_erode = True, 
    pre_box_detection_erode_kernel_size = (3, 3), 
    pre_box_detection_erode_iterations = 1,
    
    chunk_size = 10,
    chunk_density_threshold = 0.6,
    merge_chunks_with_dbscan = True, 
    chunk_merge_epsilon = 15,
    chunk_merge_min_samples = 2,
    
    connected_component_min_area = 150,
    
    use_pre_contours_definition_erode = False,
    pre_contours_definition_erode_kernel_size = (3, 3),
    pre_contours_definition_erode_iterations = 1,
    
    use_post_contours_definition_dilate = True,
    post_contours_definition_dilate_kernel_size = (3, 3),
    post_contours_definition_dilate_iterations = 1,
    
    inner_text_threshold_level = None,
    inner_text_hsv_threshold_level = ((None, None), (None, 85), (None, 40)),
    inner_text_lux_threshold_level = (None, 200),
    minimum_inner_text_density = 0.05,

    show_preview_boxes = False,
    show_boxes_number= False,
    
    debug=False):

    dark_block_threshold_level = select_with_fallback(
        option1 = compute_as_gray,
        default_value = dark_block_threshold_level,
        option1_value = dark_block_lux_threshold_level,
        option2_value = dark_block_hsv_threshold_level)

    assert dark_block_threshold_level != None, f"Block filter not set."

    inner_text_threshold_level = select_with_fallback(
        option1 = compute_as_gray,
        default_value = inner_text_threshold_level,
        option1_value = inner_text_lux_threshold_level,
        option2_value = inner_text_hsv_threshold_level)

    assert inner_text_threshold_level != None, f"Text filter not set."

    
    output_dark_block_color = select_with_fallback(
        option1 = compute_as_gray,
        default_value = output_dark_block_color,
        option1_value = output_dark_block_gray_color,
        option2_value = output_dark_block_rgb_color)

    assert output_dark_block_color != None, f"Output dark block color not set."

    print(
        output_dark_block_inner_text_color,
output_dark_block_inner_text_gray_color,
output_dark_block_inner_text_rgb_color)

    output_dark_block_inner_text_color = select_with_fallback(
        option1 = compute_as_gray,
        default_value = output_dark_block_inner_text_color,
        option1_value = output_dark_block_inner_text_gray_color,
        option2_value = output_dark_block_inner_text_rgb_color)

    assert output_dark_block_inner_text_color != None, f"Output dark block innert text color not set."


    if compute_as_gray: 
        array_image = to_grayscale_array(image)
        assert_grayscale_thresholds_color(dark_block_threshold_level)
        assert_grayscale_thresholds_color(inner_text_threshold_level)
        assert_grayscale_color(output_dark_block_color)
        assert_grayscale_color(output_dark_block_inner_text_color)
        # Verifica che i colori siano scalari (1 valore per il grigio)
        if array_image.ndim == 3:
            output_image_array = cv2.cvtColor(array_image, cv2.COLOR_RGB2GRAY)
            if debug:
                print("Converted RGB array to grayscale for output.")
        else:
            output_image_array = array_image.copy()

            
    else:
        array_image = to_rgb_array(image) 
        assert_hsv_thresholds_color(dark_block_threshold_level)
        assert_hsv_thresholds_color(inner_text_threshold_level)
        # Verifica che i colori siano RGB
        assert_rgb_color(output_dark_block_color)
        assert_rgb_color(output_dark_block_inner_text_color)
        if array_image.ndim == 2:
            # Controlla se l’immagine originale era effettivamente in scala di grigi
            original_array_image = np.array(image)
            if original_array_image.ndim == 2:
                output_image_array = cv2.cvtColor(array_image, cv2.COLOR_GRAY2RGB)
                if debug:
                    print("Converted grayscale array to RGB for output.")
            else:
                output_image_array = original_array_image.copy()
        else:
            output_image_array = array_image.copy()
    
    dark_binary_mask = obtain_binary_mask(array_image, compute_as_gray, dark_block_threshold_level)

    
    if detection_mode == BoxDetectionMode.CHUNK:
        kwargs = {
            "chunk_size": chunk_size,
            "chunk_density_threshold": chunk_density_threshold,
            "merge_chunks_with_dbscan": merge_chunks_with_dbscan,
            "chunk_merge_epsilon": chunk_merge_epsilon,
            "chunk_merge_min_samples": chunk_merge_min_samples,
            
        }
        
    elif detection_mode == BoxDetectionMode.CONNECTED:
        kwargs = {
            "connected_component_min_area":  connected_component_min_area
        }
    else:
        
        raise ValueError("Unsupported detection mode.\nAvilable deteciton modes: " + 
                         str([e.value for e in BoxDetectionMode]) + f", got {detection_mode}")

    boxes = box_detection(binary_mask = dark_binary_mask, 
                          detection_mode = detection_mode,
                          use_pre_box_detection_erode = use_pre_box_detection_erode,
                          erode_kernel_size = pre_box_detection_erode_kernel_size,
                          erode_iterations = pre_box_detection_erode_iterations,
                          **kwargs)

    if show_preview_boxes:
        for i, (x, y, w, h) in enumerate(boxes):
            cv2.rectangle(output_image_array, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if show_boxes_number:
                cv2.putText(
                    output_image_array,      # immagine
                    str(i),                                  # testo da scrivere
                    (x, max(y - 5, 5)),                               # posizione (leggermente sopra il box)
                    cv2.FONT_HERSHEY_SIMPLEX,                # font
                    0.6,                                      # scala del font
                    (0, 0, 255),                              # colore (rosso)
                    2,                                        # spessore del tratto
                    cv2.LINE_AA                               # tipo di linea (anti-alias)
                )
    else:
        ternary_image_mask = compute_ternary_mask_from_blocks(
            output_image_array, dark_binary_mask, boxes,
            lambda block, binary_block: obtain_inner_text_and_dark_block_masks(image_block = block,
                                           compute_as_gray = compute_as_gray,
                                           dark_binary_mask = binary_block,
                                           use_erode_before_contours_definition = use_pre_contours_definition_erode,
                                           erode_kernel_size = pre_contours_definition_erode_kernel_size,
                                           erode_iterations = pre_contours_definition_erode_iterations,
                                           use_dilate_after_contours_definition = use_post_contours_definition_dilate,
                                           dilate_kernel_size = post_contours_definition_dilate_kernel_size,
                                           dilate_iterations = post_contours_definition_dilate_iterations,
         
                                           inner_text_threshold_level = inner_text_threshold_level,
                                           min_text_density = minimum_inner_text_density,
                                           debug=debug)
        )
    
        
        
        # Applica colori
        print("refee")
        output_image_array[ternary_image_mask == RegionMask.DARK_BLOCK] = output_dark_block_color
        output_image_array[ternary_image_mask == RegionMask.TEXT] = output_dark_block_inner_text_color


    return Image.fromarray(ternary_image_mask == RegionMask.DARK_BLOCK), boxes



def show_dark_bounding_boxes(
    image, 
    detection_mode: BoxDetectionMode, 
    compute_as_gray =True,
    output_as_gray = False,
    
    dark_block_threshold_level = None,
    dark_block_hsv_threshold_level = ((None, None), (None, 0.9), (None, 0.5)),
    dark_block_lux_threshold_level = (None, 0.85),
    
    use_pre_box_detection_erode = True, 
    pre_box_detection_erode_kernel_size = (3, 3), 
    pre_box_detection_erode_iterations = 1,
    
    chunk_size = 10,
    chunk_density_threshold = 0.6,
    merge_chunks_with_dbscan = True, 
    chunk_merge_epsilon = 15,
    chunk_merge_min_samples = 2,
    
    connected_component_min_area = 150,
    
    show_boxes_number= False,
    debug = False):



    dark_block_threshold_level = select_with_fallback(
                                                option1 = compute_as_gray,
                                                default_value = dark_block_threshold_level,
                                                option1_value = dark_block_lux_threshold_level,
                                                option2_value = dark_block_hsv_threshold_level
                                 )

    assert dark_block_threshold_level != None, f"Block filter not set."


    if compute_as_gray: 
        array_image = to_grayscale_array(image)
    else:
        array_image = to_rgb_array(image) 
    
    dark_binary_mask = obtain_binary_mask(array_image, compute_as_gray, dark_block_threshold_level)

    if detection_mode == BoxDetectionMode.CHUNK:
        kwargs = {
            "chunk_size": chunk_size,
            "chunk_density_threshold": chunk_density_threshold,
            "merge_chunks_with_dbscan": merge_chunks_with_dbscan,
            "chunk_merge_epsilon": chunk_merge_epsilon,
            "chunk_merge_min_samples": chunk_merge_min_samples,
            
        }
        
    elif detection_mode == BoxDetectionMode.CONNECTED:
        kwargs = {
            "connected_component_min_area":  connected_component_min_area
        }
        
    else:
        raise ValueError("Unsupported detection mode.\nAvilable deteciton modes: " +
                         str([e.value for e in BoxDetectionMode]) + f", got {detection_mode}")

    
    boxes = box_detection(binary_mask = dark_binary_mask, 
                          detection_mode = detection_mode,
                          use_pre_box_detection_erode = use_pre_box_detection_erode,
                          erode_kernel_size = pre_box_detection_erode_kernel_size,
                          erode_iterations = pre_box_detection_erode_iterations,
                          **kwargs)
    
    if output_as_gray:
        if array_image.ndim == 3:
            output_image_array = cv2.cvtColor(array_image, cv2.COLOR_RGB2GRAY)
            if debug:
                print("Converted RGB array to grayscale for output.")
        else:
            output_image_array = array_image
    else:
        if array_image.ndim == 2:
            original_array_image = np.array(image)
            if original_array_image.ndim == 2:
                output_image_array = cv2.cvtColor(array_image, cv2.COLOR_GRAY2RGB)
                if debug:
                    print("Converted grayscale array to RGB for output.")
            else:
                output_image_array = array_image
        else:
            output_image_array = array_image
        
    for i, (x, y, w, h) in enumerate(boxes):
        cv2.rectangle(output_image_array, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if show_boxes_number:
            cv2.putText(
                array_image,      # immagine
                str(i),                                  # testo da scrivere
                (x, max(y - 5, 5)),                               # posizione (leggermente sopra il box)
                cv2.FONT_HERSHEY_SIMPLEX,                # font
                0.6,                                      # scala del font
                (0, 0, 255),                              # colore (rosso)
                2,                                        # spessore del tratto
                cv2.LINE_AA                               # tipo di linea (anti-alias)
            )
            
    output_image_array = Image.fromarray(array_image)
    return output_image_array.convert("L") if output_as_gray else output_image_array.convert("RGB"), boxes



    

def cleanup_files(files, output_folder, dpi= 200, poppler_path= r"C:\Program Files\poppler-24.08.0\Library\bin", detection_mode=BoxDetectionMode.CHUNK, debug=False):

    return 
    '''
    output_files = []
    for file in files:
        base_name = os.path.splitext(os.path.basename(file))[0]
        if output_folder == '.':
            output_files.append(f"{base_name}_cleaned.pdf")
        else:
            output_files.append(os.path.join(output_folder, f"{base_name}_cleaned.pdf"))
        

    for input_pdf, output_pdf in zip(files, output_files):
        print(f"[START] File processing: {input_pdf}")
        pages = convert_from_path(input_pdf, dpi=dpi, poppler_path=poppler_path)
        image_paths = []

        bbox_args = BoundingBoxes_args()  # puoi anche parametrizzarlo

        for i, page in enumerate(pages):
            print(f"  -> Processing page {i + 1}/{len(pages)}...")
            img = apply_cleanup(page, bbox_args, detection_mode=detection_mode, debug=debug)
            img_path = os.path.join(TEMP_FOLDER, f"page_{i:03d}.jpg")
            img.save(img_path, "JPEG")
            image_paths.append(img_path)
        
        print(f"  -> PDF pages combined in: {output_pdf}")
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(image_paths))
    
        print(f"[DONE] File saved: {output_pdf}\n")

    '''
    '''
    # Facoltativo: pulizia immagini temporanee
    for img_path in image_paths:
        if os.path.exists(img_path):
            os.remove(img_path)
    '''
    


def batch_process(pattern: str, output: str, detection_mode=BoxDetectionMode.CHUNK):
    files = [f for f in glob.glob(pattern, recursive=True)]
    if not files:
        location = f"at {pattern}" if '*' not in pattern else f"with pattern {pattern}"
        print(f"Error: no figure files found {location}.")
        sys.exit(1)
    
    for f in files[:]:
        if os.path.isdir(f):
            batch_process(f"{f}\**\*.pdf", output, detection_mode=detection_mode)
            files.remove(f)
    
    if not files:
        sys.exit(0)

    cleanup_files(files, output, detection_mode=detection_mode)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cleanup PDF banners")
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-o", "--output", default='.')
    parser.add_argument("--mode", choices=["chunk", "connected"], default="chunk")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()
    mode = BoxDetectionMode(args.mode.upper())

    batch_process(args.file, args.output, args.mode)


    
    

