from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import matplotlib.cm as matcm
from matplotlib.colors import rgb_to_hsv
import matplotlib.pyplot as plt
import colorsys
import img2pdf
import cv2
import os
import argparse, sys
import glob
import math
from sklearn.cluster import DBSCAN

TEMP_FOLDER = "temp_images"

from enum import Enum
from enum import IntEnum


class BoxDetectionMode(Enum):
    CHUNK = "chunk"
    CONNECTED = "connected"

    def __eq__(self, other):
        if isinstance(other, Enum):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other
        return False

    def __hash__(self):
        return hash(self.value)
            
       


class RegionMask(IntEnum):
    BACKGROUND = 0
    TEXT = 1
    INNER_BLOCK = 2

    def __eq__(self, other):
        if isinstance(other, RegionMask):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f"RegionMask.{self.name} ({self.value})"


    

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

def chunk_density(dark_binary_mask, chunk_size=16, density_thresh=0.6, debug = False):
    H, W = dark_binary_mask.shape

    if debug:
        print("------ Banners Density Detection Parameters ------")
        print(f" - dark binary mask size: {H, W};")
        print(f" - subdivision chunk size: {chunk_size};")
        print(f" - withe threshold: {density_thresh}")
        debug_for_output = ""
        debug_for_counter = 0
        debug_for_output_columns = 5
        debug_for_output_column_splitter = "| "
        debug_for_output_last_column_row_completed = 0
        print(f"Banners detection...")
    
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
                if debug:
                    debug_for_counter += 1
                    debug_for_output += f"banner block detected in {(x, y)}\n"
                    debug_for_output += f" - shape: {(x, y, chunk_size + x, chunk_size + y)}\n"
                dense_blocks.append((x, y, chunk_size, chunk_size))
    if debug:
        rows = debug_for_output.split("\n")
        max_row_length = 0
        for r in rows:
            if len(r) > max_row_length:
                max_row_length = len(r)
                
        debug_for_output = ""
        row_per_for = int(len(rows)/debug_for_counter)
        for starter in range(0, int(len(rows)/(row_per_for * debug_for_output_columns)), debug_for_output_columns*row_per_for): 
            debug_for_counter = 0
            for row_offst in range(row_per_for):
                for r in range(starter + row_offst, row_per_for * debug_for_output_columns + starter, row_per_for):
                    if debug_for_counter % len(rows)//10 == 0 or len(rows) < 5:
                        debug_for_output += rows[r] + " "*(max_row_length - len(rows[r])) + debug_for_output_column_splitter
                        debug_for_counter += 1
                        if debug_for_counter % debug_for_output_columns == 0:
                            debug_for_output = debug_for_output[:-len(debug_for_output_column_splitter)]
                            debug_for_output += "\n"
        print(debug_for_output)
        print(f"found {len(dense_blocks)} banner blocks")
        print("--------------------------------------------------")
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
    compute_as_gray=False,
    dark_binary_mask=None,

    use_erode_before_contours_definition=False,
    erode_kernel_size=None,
    erode_iterations=None,

    use_dilate_after_contours_definition=False,
    dilate_kernel_size=None,
    dilate_iterations=None,

    inner_text_threshold_level=None,
    min_text_density=0.4,

    debug=False
):
    if dark_binary_mask is None:
        raise ValueError("dark_binary_mask must be provided.")

    if debug:
        print("Computing block inner text binary mask...")

    # Step 1: calcola maschera binaria del testo
    inner_text_mask = obtain_binary_mask(
        image_block,
        compute_as_gray=compute_as_gray,
        mask_threshold_level=inner_text_threshold_level,
        debug=debug
    )

    shape_2d = image_block.shape[:2]

    # Step 2: verifica densità del testo
    text_density = np.sum(inner_text_mask) / inner_text_mask.size
    if debug:
        print(f"Inner text density: {text_density:.3f}")

    if text_density < min_text_density:
        if debug:
            print("Block discarded: text density too low.")
        return {
            RegionMask.TEXT: np.zeros(shape_2d, dtype=np.uint8),
            RegionMask.INNER_BLOCK:np.ones(shape_2d, dtype=np.uint8)
        }

    # Step 3: copia e prepara la maschera binaria
    binary_mask = dark_binary_mask.copy().astype(np.uint8)
    assert np.all(np.isin(binary_mask, [0, 1])), "dark_binary_mask must contain only 0 and 1 values."

    # Step 4: erosione (pre-contorni)
    if use_erode_before_contours_definition:
        if debug:
            print(f"Applying erosion: kernel={erode_kernel_size}, iterations={erode_iterations}")
        binary_mask = erode_image(binary_mask * 255, erode_kernel_size, erode_iterations)
        binary_mask = (binary_mask > 127).astype(np.uint8)

    # Step 5: trova contorni e riempi
    if debug:
        print("Filling contours to define block area...")

    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    binary_filled = np.zeros(shape_2d, dtype=np.uint8)
    cv2.drawContours(binary_filled, contours, -1, 1, thickness=-1)

    # Step 6: dilatazione (post-contorni)
    if use_dilate_after_contours_definition:
        if debug:
            print(f"Applying dilation: kernel={dilate_kernel_size}, iterations={dilate_iterations}")
        expanded = dilate_image(binary_filled * 255, dilate_kernel_size, dilate_iterations)
        expanded = (expanded > 127).astype(np.uint8)
    else:
        expanded = binary_filled

    # Step 7: output finale
    inner_text_inside_block = expanded & inner_text_mask
    return {
        RegionMask.TEXT: inner_text_inside_block,
        RegionMask.INNER_BLOCK: expanded & ~inner_text_mask
    }
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



def compute_Ndimentional_mask_from_blocks(array_image, binary_mask, boxes, compute_masks_fn, mask_values, debug = False):
    if not mask_values:
        raise ValueError("Provide mask values.")

    if isinstance(mask_values, (list, tuple)):
        keys = range(len(mask_values))
    elif isinstance(mask_values, (dict)):
        keys = list(mask_values.keys())
    else:
        raise TypeError(f"Expected mask_values_args to be list, tuple or dict, but go {type(mask_values_args).__name__}")

    n_dim_mask = np.full(array_image.shape[:2], RegionMask.BACKGROUND, dtype=np.uint8)

    
    if debug:
        box_colors = matcm.get_cmap('Paired', len(mask_values) + 1)

    for b_index, (x, y, w, h) in enumerate(boxes):
        debug =  (debug and b_index % len(boxes)//10 == 0) or (debug and len(boxes) < 5)
        block = array_image[y:y+h, x:x+w]
        block_binary_mask = binary_mask[y:y+h, x:x+w]
        if debug:
            print(f"Computing n-dimensional mask for chunk at {((x,y), (x+w, y+h))}...")
        local_out_masks = compute_masks_fn(block, block_binary_mask)
        
        if isinstance(local_out_masks, (list, tuple)):
            for local_out_mask in local_out_masks:
                assert np.array_equal(np.unique(local_out_mask), [0]) or \
                       np.array_equal(np.unique(local_out_mask), [1]) or \
                       np.array_equal(np.unique(local_out_mask), [0, 1]), \
                       f"Mask at key '{key}' is not binary. Found values: {np.unique(local_out_mask)}"
        elif isinstance(local_out_masks, (dict)):
            for local_out_mask_key in local_out_masks:
                assert np.array_equal(np.unique(local_out_masks[local_out_mask_key]), [0]) or \
                               np.array_equal(np.unique(local_out_masks[local_out_mask_key]), [1]) or \
                               np.array_equal(np.unique(local_out_masks[local_out_mask_key]), [0, 1]), \
                               f"Mask at key '{key}' is not binary. Found values: {np.unique(local_out_masks[local_out_mask_key])}"

        # Controlli robusti
        if isinstance(mask_values, (list, tuple)):
            if not isinstance(local_out_masks, (dict)):
                assert isinstance(local_out_masks, (list, tuple)), \
                f"Expected local_out_masks to be list or tuple, but got {type(local_out_masks).__name__}"
            
                assert len(local_out_masks) == len(mask_values), \
                    f"Length mismatch: mask_values has {len(mask_values)} elements, but local_out_masks has {len(local_out_masks)}"
            elif isinstance(local_out_masks, (dict)):
                mask_values_t = {}
                for key in local_out_masks:
                    assert key in mask_values, f"If mask_values is a list type, then must contains the same keys of the output of {compute_masks_fn.__name__} function"

                    mask_values_t.update({key: key})

                mask_values = mask_values_t
                keys = list(mask_values.keys())
                
            
        elif isinstance(mask_values, dict):
            assert isinstance(local_out_masks, dict), \
                f"Expected local_out_masks to be dict, but got {type(local_out_masks).__name__}"
            
            assert mask_values.keys() == local_out_masks.keys(), \
                f"Key mismatch: mask_values keys = {list(mask_values.keys())}, local_out_masks keys = {list(local_out_masks.keys())}"
                
        else:
            raise TypeError(f"mask_values must be a list, tuple or dict, but got {type(mask_values).__name__}")


        # Crea maschera locale
        local_mask = np.full((h, w), RegionMask.BACKGROUND, dtype=np.uint8)

        if debug:
            n = len(keys) + 1  # +1 per la mask finale
            if w > h:
                nrows, ncols = n, 1  # disposti in colonna
            elif h > w:
                nrows, ncols = 1, n  # disposti in riga
            else:
                ncols = math.ceil(math.sqrt(n))
                nrows = math.ceil(n / ncols)
                
        
            fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 5))
            fig.suptitle(f'Box at {((x,y), (x+w, y+h))}')
            fig.tight_layout()
        
            
            # axs sarà un array 2D solo se nrows > 1 and ncols > 1
            axs = np.array(axs).reshape(-1)  # flatten per indicizzare facilmente
            
            for i in range(n, ncols * nrows):                
                axs[i].axis("off")
                
        for i, key in enumerate(keys):
            local_mask[local_out_masks[key].astype(bool)] = mask_values[key]
            if debug:
                axs[i].imshow(local_out_masks[key], cmap='gray')
                axs[i].set_title(f"mask: {key}, white filled with {mask_values[key]:.0f}")
                print(f"    > key {key}, mask filled: {np.sum(local_out_masks[key])} pixels")
                print(f"    > inner_text_mask shape: {local_out_masks[keys[0]].shape}, dtype: {local_out_masks[keys[0]].dtype}")
                print(f"    > block area shape: {local_out_masks[keys[1]].shape}, dtype: {local_out_masks[keys[1]].dtype}")
        if debug:
            axs[i + 1].imshow(local_mask, cmap= box_colors)
            axs[i + 1].set_title(f"Local Ndimentional mask")
            print(f"Unique mask values in local mask: {np.unique(local_mask)}")

        

        # Unisci senza sovrascrivere
        current_slice = n_dim_mask[y:y+h, x:x+w]
        n_dim_mask[y:y+h, x:x+w] = np.where(local_mask != RegionMask.BACKGROUND, local_mask, current_slice)
    return n_dim_mask




def detect_dark_blocks_by_chunks(
    dark_binary_mask,
    chunk_size,
    chunk_density_threshold,
    merge_chunks_with_dbscan,
    chunk_merge_epsilon,
    chunk_merge_min_samples,
    debug = False,
    chunk_density_debug = False):

    
    if debug:
        print("Detecting banners using chunk density colors...")

    boxes = chunk_density(dark_binary_mask,
                          chunk_size= chunk_size,
                          density_thresh = chunk_density_threshold,
                         debug = chunk_density_debug)
    if merge_chunks_with_dbscan:
        if debug:
            print("Merging detected banners using dbscan algorithm...")
        boxes = cluster_blocks_dbscan(boxes, 
                                      eps= chunk_merge_epsilon,
                                      min_samples = chunk_merge_min_samples)
    
        boxes_to_remove = []
        if debug:
            print("Removing internal boxes after dbscan merging...")
        for i, (x1, y1, w1, h1) in enumerate(boxes):
            for e in range(i+1, len(boxes)):
                x2, y2, w2, h2 = boxes[e]
                if x1 <= x2 and y1 <= y2 and x1 + w1 >= x2 + w2 and y1 + h1 >= y2 + h2:
                    boxes_to_remove.append(e)
        for i in sorted(boxes_to_remove, reverse = True):
            del boxes[i]
    print(f"Banner blocks detected: {len(boxes)}")
    return boxes

def detect_dark_with_connected_components(eroded_dark_binary_mask, connected_component_min_area=150, debug = False):
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
                  use_post_detection_erode_dilate = True,
                  dilate_kernel_size = None,
                  dilate_iterations = None,
                  debug = False,
                  *args, **kwargs):

    unique = np.unique(binary_mask)
    assert len(unique) <=2, f"Box detection supported only on binary masks, found {unique} groups of level"

    if dilate_kernel_size is None:
        dilate_kernel_size = erode_kernel_size
    if dilate_iterations is None:
        dilate_iterations = erode_iterations

    if len(unique) < 2:
        return []

    if use_pre_box_detection_erode:
        if debug:
            print(f"Applying image eorde to remove text: kernel = {erode_kernel_size}, iterations = {erode_iterations}")
        binary_mask = erode_image(binary_mask * 255, erode_kernel_size, iterations= erode_iterations)

    if use_post_detection_erode_dilate:
        # NEW: Recupera i pixel persi con una dilatazione leggera
        if debug:
            print(f"Applying image dilation to recover border: kernel = {dilate_kernel_size}, iterations = {dilate_iterations}")
        binary_mask = dilate_image(binary_mask * 255, dilate_kernel_size, iterations= dilate_iterations)
    
    binary_mask = (binary_mask > 0).astype(np.uint8)
        
    if detection_mode == BoxDetectionMode.CHUNK:
        if debug:
            print(f"Appling detection by chunks subdivision...")
        return detect_dark_blocks_by_chunks(binary_mask,  *args, **kwargs, debug = debug)

    elif detection_mode == BoxDetectionMode.CONNECTED:
        if debug:
            print(f"Appling detection by connected components...")
        return detect_dark_with_connected_components(binary_mask, *args, **kwargs, debug = debug,)
        
    else:
        raise ValueError("Unsupported detection mode.")


def obtain_binary_mask(array_image, compute_as_gray, mask_threshold_level, debug = False):
    if compute_as_gray:
        assert len(array_image.shape) == 2, f"Image shape expected is (W,H), got {array_image.shape}"
        assert len(mask_threshold_level) == 2, f"Expected only two elements for luminescence level threshold, got {mask_threshold_level}"
        if debug:
            print(f"Computing binary image in grayscale")
            print(f"Luminescene threshold levels: {mask_threshold_level}")
        lux_mask = np.ones_like(array_image, dtype=bool)
        l_min, l_max = mask_threshold_level
        if l_min is not None:
            lux_mask &= (array_image >= l_min)
        if l_max is not None:
            lux_mask &= (array_image <= l_max)

        mask = lux_mask.astype(np.uint8)
        
    else:
        assert array_image.shape[2] == 3, f"Image shape expected is (W,H,3), got {array_image.shape}"
        assert len(mask_threshold_level) == 3, f"Expected only tre elements for hsv level threshold, got {mask_threshold_level}"
        for i, channel in enumerate("HSV"):
            assert len(mask_threshold_level[i]) == 2, f"Expected only two elements for {channel} level threshold, got {mask_threshold_level}"
        if debug:
            print(f"Computing binary image in HSV color space")
            print(f"HSV threshold levels: {mask_threshold_level}")
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
    
        mask = (h_mask & s_mask & v_mask).astype(np.uint8)

    if debug:
        print(f"Unique mask values: {np.unique(mask)}")
    return mask
        
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


"""
Missione:
    Fornisce un’interfaccia ad alto livello per la rilevazione e la rimozione (o ricolorazione)
    automatica delle aree maggiormente dense (tipicamente banner) presenti in un’immagine.

Funzionalità Principali:
    1. Modalità di rilevamento dei blocchi densi:
        - CHUNK: scansione a blocchi fissi; un blocco è considerato "denso" se la quantità di pixel
          scuri supera una soglia. I blocchi densi possono essere uniti tramite DBSCAN.
        - CONNECTED: utilizza cv2.connectedComponents per segmentare le regioni connesse
          di pixel scuri.

    2. Spazio colore di elaborazione:
        - Possibilità di elaborare l'immagine in scala di grigi (compute_as_gray=True) oppure in RGB.
        - Possibilità di restituire l'immagine modificata in scala di grigi (output_as_gray=True)
          oppure in RGB.

    3. Colori di output:
        - Colore delle aree dense ("banner"):
            - In scala di grigi (default: 255)
            - In RGB (default: [255, 255, 255])
        - Colore del testo interno alle aree dense:
            - In scala di grigi (default: 0)
            - In RGB (default: [0, 0, 0])

    4. Soglie per la rilevazione delle aree dense:
        - In scala di grigi (default: < 180)
        - In HSV (default: < [*, 100, 100])

    5. Pre- e post-processing per la rilevazione dei banner:
        - Erosione pre-detection:
            - Rimuove rumore e testo
            - Default: True, kernel: (3, 3), iterazioni: 1
        - Dilatazione post-detection:
            - Compensa i pixel persi per erosione
            - Default: True, stesso kernel e iterazioni

    6. Parametri per modalità CHUNK:
        - chunk_size: dimensione del blocco (default: 10)
        - chunk_density_threshold: soglia per considerare il blocco "denso"
        - merge_chunks_with_dbscan: se True, unisce blocchi vicini
        - chunk_merge_epsilon: distanza massima per unire
        - chunk_merge_min_samples: numero minimo di blocchi per regione

    7. Parametri per modalità CONNECTED:
        - connected_component_min_area: area minima per accettare una componente

    8. Rilevamento del testo interno ai banner:
        - use_pre_contours_definition_erode:
            - Applica erosione prima della definizione dei contorni
            - Default: False, kernel: (3, 3), iterazioni: 1
        - use_post_contours_definition_dilate:
            - Applica dilatazione dopo la definizione dei contorni
            - Default: False, kernel: (3, 3), iterazioni: 1
        - inner_text_threshold_level:
            - Soglia per identificare il testo interno
            - Default: <200 in grigio, < [*, 85, 40] in HSV
        - minimum_inner_text_density:
            - Soglia minima per accettare la presenza di testo (default: 0.05)

    9. Debug e anteprima:
        - show_preview_boxes:
            - Mostra i box rilevati ma non modifica l'immagine
        - show_boxes_number:
            - Mostra la numerazione accanto a ogni box

Cosa produce:
    - Una nuova immagine (`PIL.Image`) con aree dense e/o testo interno ricolorati (o rimossi)
    - Una lista di bounding box nel formato (x, y, w, h)

Note:
    - Tutte le soglie di luminosità e colore sono personalizzabili.
    - Funzione compatibile con immagini `PIL.Image` o `np.ndarray`.
    - Verifica automatica dei parametri colore in base allo spazio colore selezionato.

"""    
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

    use_post_detection_erode_dilate = True, 
    post_detection_dilate_kernel_size = None, 
    post_detection_dilate_iterations = None,
    
    chunk_size = 10,
    chunk_density_threshold = 0.6,
    merge_chunks_with_dbscan = True, 
    chunk_merge_epsilon = 15,
    chunk_merge_min_samples = 2,
    
    connected_component_min_area = 150,
    
    use_pre_contours_definition_erode = False,
    pre_contours_definition_erode_kernel_size = (3, 3),
    pre_contours_definition_erode_iterations = 1,
    
    use_post_contours_definition_dilate = False,
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
    print(f"Computing block masks...")
    dark_binary_mask = obtain_binary_mask(array_image, compute_as_gray, dark_block_threshold_level, debug = debug)

    
    if detection_mode == BoxDetectionMode.CHUNK:
        kwargs = {
            "chunk_size": chunk_size,
            "chunk_density_threshold": chunk_density_threshold,
            "merge_chunks_with_dbscan": merge_chunks_with_dbscan,
            "chunk_merge_epsilon": chunk_merge_epsilon,
            "chunk_merge_min_samples": chunk_merge_min_samples,
            "debug": debug,
            "chunk_density_debug": False
            
        }
        
    elif detection_mode == BoxDetectionMode.CONNECTED:
        kwargs = {
            "connected_component_min_area":  connected_component_min_area,
            "debug": debug
        }
    else:
        
        raise ValueError("Unsupported detection mode.\nAvilable deteciton modes: " + 
                         str([e for e in BoxDetectionMode]) + f", got {detection_mode}")

    boxes = box_detection(binary_mask = dark_binary_mask, 
                          detection_mode = detection_mode,
                          use_pre_box_detection_erode = use_pre_box_detection_erode,
                          erode_kernel_size = pre_box_detection_erode_kernel_size,
                          erode_iterations = pre_box_detection_erode_iterations,
                          use_post_detection_erode_dilate = use_post_detection_erode_dilate,
                          dilate_kernel_size = post_detection_dilate_kernel_size,
                          dilate_iterations = post_detection_dilate_iterations,
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
        print(f"Computing ternary masks for background, inner text and area block...")
        ternary_image_mask = compute_Ndimentional_mask_from_blocks(
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
                                           debug=debug),
            mask_values = [
                RegionMask.TEXT,
                RegionMask.INNER_BLOCK
            ],
            debug = debug
        )
    
        
        
        # Applica colori
        print("refee")
        output_image_array[ternary_image_mask == RegionMask.TEXT] = output_dark_block_inner_text_color
        output_image_array[ternary_image_mask == RegionMask.INNER_BLOCK] = output_dark_block_color

    return Image.fromarray(output_image_array), boxes



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


    
    

