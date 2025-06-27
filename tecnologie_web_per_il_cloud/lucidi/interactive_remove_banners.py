import matplotlib.pyplot as plt
from IPython.display import display
import numpy as np

# Per facilitare i comandi interattivi
from PIL import Image
import cv2

from remove_banners import compute_dark_mask, connected_component_boxes, clean_dark_block, to_rgb_array

def draw_bounding_boxes_on_image(image, data_boxes, as_gray=False, show_density_block= False, show_numbers= False):

    rgb = to_rgb_array(image)
    gray = to_grayscale_array(image)

    for i, data in enumerate(data_boxes):
        x, y, w, h = data["bbox"]
        
        cv2.rectangle(rgb if not as_gray else gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if show_numbers:
            cv2.putText(
                rgb if not as_gray else gray,      # immagine
                str(i),                                  # testo da scrivere
                (x, max(y - 5, 5)),                               # posizione (leggermente sopra il box)
                cv2.FONT_HERSHEY_SIMPLEX,                # font
                0.6,                                      # scala del font
                (0, 0, 255),                              # colore (rosso)
                2,                                        # spessore del tratto
                cv2.LINE_AA                               # tipo di linea (anti-alias)
            )

    return Image.fromarray(rgb if not as_gray else gray)

def apply_cleanup_parameters_on_boxes(image, data_boxes):

    rgb = to_rgb_array(image)
    
    for data in data_boxes:
        x, y, w, h = data["bbox"]
        apply_cleanup_params = data["apply_cleanup_params"]
        
        block = rgb[y:y+h, x:x+w]
        rgb[y:y+h, x:x+w] = clean_dark_block(block, box_args, **apply_cleanup_params)
            

    return Image.fromarray(cleaned_rgb)


def show_image_cv2(title, img_array):
    cv2.imshow(title, cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def parse_vd_args(cmd: str):
    parser = argparse.ArgumentParser(prog='vd', add_help=False)
    parser.add_argument(
        '--type',
        choices=['bounding_boxes', 'apply_cleanup', 'both'],
        default='bounding_boxes',
        help='Debug visualizzation type'
    )
    parser.add_argument('--as_gray', action='store_true')
    parser.add_argument('--show_density_block', action='store_true')
    parser.add_argument('--show_numbers', action='store_true')
    parser.add_argument('--side_by_side', action='store_true')
    
    try:
        args = parser.parse_args(cmd.split()[1:])  # Salta "vd"
    except SystemExit:
        print("Errore nei parametri di 'vd'.")
        return None

    return vars(args)


def parse_value(val, typ):
    if typ is bool:
        return val.lower() in ['true', '1', 'yes', 'y']
    elif typ is int:
        return int(val)
    elif typ is float:
        return float(val)
    elif typ is tuple:
        # es: (3, 3)
        items = val.strip('()').split(',')
        return tuple(int(i.strip()) for i in items)
    else:
        raise ValueError(f"Tipo non gestito: {typ}")

def handle_modify_block_box(self, block_ids, boxes):
    """
    Modifica le coordinate dei bounding box specificati in block_ids.

    Args:
        block_ids (list[int]): lista di indici dei box da modificare
        boxes (list[tuple]): lista di box (x,y,w,h) correnti

    Returns:
        list[tuple]: nuova lista di box aggiornata
    """
    for idx in block_ids:
        if idx < 0 or idx >= len(boxes):
            print(f"[WARN] Indice {idx} fuori range.")
            continue

        x, y, w, h = boxes[idx]
        print(f"Box {idx}: x={x}, y={y}, w={w}, h={h}")

        try:
            new_x = input(f"Nuovo x (ENTER per mantenere {x}): ")
            new_y = input(f"Nuovo y (ENTER per mantenere {y}): ")
            new_w = input(f"Nuova larghezza (ENTER per mantenere {w}): ")
            new_h = input(f"Nuova altezza (ENTER per mantenere {h}): ")

            x = int(new_x) if new_x.strip() != "" else x
            y = int(new_y) if new_y.strip() != "" else y
            w = int(new_w) if new_w.strip() != "" else w
            h = int(new_h) if new_h.strip() != "" else h

            if w <= 0 or h <= 0:
                print(f"[ERROR] Larghezza e altezza devono essere > 0. Box {idx} ignorato.")
                continue

            boxes[idx] = (x, y, w, h)
            print(f"Box {idx} aggiornato a: {boxes[idx]}")
        except Exception as e:
            print(f"[ERROR] Input non valido per box {idx}: {e}")

    return boxes
        

class CommandHandler:
    def __init__(self, pages, box_detection_args):
        self.pages = pages
        self.box_detection_args = box_detection_args
        self.page_index = 0
        self.current_image = pages[0]
        self.current_data_boxes = [
            {
                "bbox": []
                "cleanup_args": None,
                "apply_cleanup_params": {
                    "inner_text_s_thresh": (),
                    "inner_text_v_thresh": (),
                    "min_text_density": None,
                    "debug": False
                }
            }
        ]
        self.apply_cleanup_params = { ... }
        self.bounding_boxes_params = { ... }

        self.cleaned_pages = self.pages

        self.command_map = {
            "v": self.handle_view,
            "vd": self.handle_debug,
            "aa": self.handle_apply_all_cleanup,
            "ab": self.handle_apply_block_cleanup,
            "n": self.handle_next,
            "p": self.handle_prev,
            "set": self.handle_set_cleanup_params,
            "setb": self.handle_set_box_detection_args,
            "switchb": self.handle_switch_box_detection_args,
            "showb": self.handle_show_box_detection_args
            "q": self.handle_quit
        }

        self.running = True

    def run(self):
        while self.running:
            print(f"\n=== Pagina {self.page_index+1}/{len(self.pages)} ===")
            cmd = input("Comandi: [v]iew | [vd]ebug | [aa] apply all | [ab] apply block | [p]rev | [n]ext | [set] parameters | [setb] BoxArgs | [switchb] Mode | [Q]uit\n> ").strip()
            if not cmd:
                continue

            name = cmd.lower().split()[0]
            handler = self.command_map.get(name)
            if handler:
                handler(cmd)
            else:
                print("Comando non riconosciuto.")

    def handle_view(self, cmd):
        """
        Show the current image
        """
        show_image_cv2("Visualizzazione", to_rgb_array(self.current_image))

    def handle_debug(self, cmd):
        """
        Show the current image with advanced functions
        """
        options = parse_vd_args(cmd)
        if not options:
            return

        vis_type = options.pop("type")
        if vis_type == "bounding_boxes":
            img = draw_bounding_boxes_on_image (self.current_image, self.current_data_boxes, **options)
            show_image_cv2("Bounding boxes visualization", to_rgb_array(img))
            
        elif vis_type == "apply_cleanup":
            img = apply_cleanup_parameters_on_boxes(self.current_image, self.current_data_boxes)
            show_image_cv2("After cleanup visualization", to_rgb_array(img))
            
        elif vis_type == "both":
            side_by_side = options.pop("side_by_side")
            original_with_boxes = draw_bounding_boxes_on_image(self.current_image, self.current_data_boxes, **options)
            cleaned_with_boxes = draw_bounding_boxes_on_image(
                apply_cleanup_parameters_on_boxes(self.current_image, self.current_data_boxes),
                self.current_data_boxes, **options
            )
            if side_by_side:
                side_by_side_img = np.hstack([to_rgb_array(original_with_boxes), to_rgb_array(cleaned_with_boxes)])
                show_image_cv2("BoundingBoxes vs Cleanup", side_by_side_img)
            else:
                show_image_cv2("Cleanup Image", cleaned_with_boxes)
            return
            
        else:
            print(f"Tipo '{vis_type}' non supportato.")
            return

    def mark_page_cleaned(self):
        self.cleaned_pages[self.page_index] = self.current_image.copy()

    def handle_apply_all_cleanup(self, cmd):
        if not self.current_data_boxes:
            print("[AVVISO] Nessun blocco disponibile.")
            return
    
        vis = to_rgb_array(self.current_image)
    
        print(f"[INFO] Pulizia di {len(self.current_data_boxes)} blocchi in corso...")
    
        for idx, data in enumerate(self.current_data_boxes):
            x, y, w, h = data["bbox"]
            parms = data[""]
            (, parms)
            block = vis[y:y+h, x:x+w]
            cleaned = clean_dark_block(block, self.box_detection_args, **parms)
            vis[y:y+h, x:x+w] = cleaned
    
        show_image_cv2("Preview - Tutti i blocchi ripuliti", vis)
    
        choice = input("Confermi la modifica dell'immagine corrente? [Y/n]: ").strip().lower()
        if choice == 'y' or choice == '':
            self.current_image = Image.fromarray(vis)
            _, self.current_data_boxes = show_dark_bounding_boxes(self.current_image, self.box_detection_args)
            self.mark_page_cleaned()
            print("[INFO] Immagine aggiornata.")
        else:
            print("[INFO] Modifiche annullate.")


    def handle_apply_block_cleanup(self, cmd):
        print(f"Totale blocchi: {len(self.current_data_boxes)}")
        ids = input("Inserisci ID blocchi separati da virgola (es. 0,2,5): ")
        ids = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]
        vis = to_rgb_array(self.current_image).copy()

        for idx in ids:
            x, y, w, h = self.current_data_boxes[idx]
            block = vis[y:y+h, x:x+w]
            cleaned = clean_dark_block(block, self.box_detection_args, **self.apply_cleanup_params)
            vis[y:y+h, x:x+w] = cleaned

        show_image_cv2("Visualizzazione", np.array(vis))
        choice = input("Accept? [Y, n] ")
        if choice == 'y':
            self.current_image = Image.fromarray(vis)
            self.mark_page_cleaned()
            print("[INFO] Immagine aggiornata.")

    elif cmd.lower().startswith('mbb'):  # modify block box
        ids_str = input("Inserisci ID blocchi separati da virgola (es. 0,2,5): ")
        block_ids = [int(i.strip()) for i in ids_str.split(',') if i.strip().isdigit()]
        boxes = self.current_data_boxes  # assumendo che li abbia memorizzati
        boxes = self.handle_modify_block_box(block_ids, boxes)
        vis = to_rgb_array(self.current_image)

        for i, (x, y, w, h) in enumerate(boxes):
            cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                vis,      # immagine
                str(i),                                  # testo da scrivere
                (x, max(y - 5, 5)),                               # posizione (leggermente sopra il box)
                cv2.FONT_HERSHEY_SIMPLEX,                # font
                0.6,                                      # scala del font
                (0, 0, 255) if i in block_ids else (0, 0, 0),                              # colore (rosso)
                2,                                        # spessore del tratto
                cv2.LINE_AA                               # tipo di linea (anti-alias)
            )

        show_image_cv2("Visualizzazione", np.array(vis))
        choice = input("Accept? [Y, n] ")
        if choice == 'y':
            self.current_data_boxes = boxes
            print(f"[INFO] Bordi {[id for id in block_ids]} aggiornati.")

    def handle_set_cleanup_params(self, cmd):
        for k in self.apply_cleanup_params:
            val = input(f"{k} = {self.apply_cleanup_params[k]} → nuovo valore (ENTER per saltare): ")
            if val.strip() == '':
                continue
            try:
                if k.endswith('_thresh'):
                    if val.strip().lower() == "none":
                        self.apply_cleanup_params[k] = (None, None)
                    else:
                        t = tuple(float(v.strip()) if v.strip().lower() != 'none' else None for v in val.strip().split(','))
                        self.apply_cleanup_params[k] = t
                elif k == "debug":
                    self.apply_cleanup_params[k] = val.lower() in ['true', '1', 'yes']
                else:
                    self.apply_cleanup_params[k] = float(val)
            except Exception as e:
                print(f"Errore: {e}")

    def handle_set_box_detection_args(self, cmd):
        box_detection_args = self.box_detection_args
        base_fields = [
            ("use_erode", bool),
            ("erode_kernel_size", tuple),
            ("erode_iterations", int),
            ("use_dilate", bool),
            ("dilate_kernel_size", tuple),
            ("dilate_iterations", int),
            ("ligth_upper_level", int),
        ]
    
        # Parametri comuni
        for name, typ in base_fields:
            val = input(f"{name} = {getattr(box_detection_args, name)} → nuovo valore (ENTER per saltare): ").strip()
            if not val:
                continue
            try:
                parsed = parse_value(val, typ)
                setattr(box_detection_args, name, parsed)
            except Exception as e:
                print(f"Errore su '{name}': {e}")
    
        # Parametri specifici
        if isinstance(box_detection_args, ChunkCleanupArgs):
            chunk_fields = [
                ("chunk_size", int),
                ("density_thresh", float),
                ("dbscan_eps", int),
                ("dbscan_min_samples", int),
            ]
            for name, typ in chunk_fields:
                val = input(f"{name} = {getattr(box_detection_args, name)} → nuovo valore (ENTER per saltare): ").strip()
                if not val:
                    continue
                try:
                    parsed = parse_value(val, typ)
                    setattr(box_detection_args, name, parsed)
                except Exception as e:
                    print(f"Errore su '{name}': {e}")
    
        elif isinstance(box_detection_args, ConnectedCleanupArgs):
            connected_fields = [
                ("min_area", int),
                ("use_inblock_erode", bool),
                ("inblock_erode_kernel_size", tuple),
                ("inblock_erode_iterations", int),
            ]
            for name, typ in connected_fields:
                val = input(f"{name} = {getattr(box_detection_args, name)} → nuovo valore (ENTER per saltare): ").strip()
                if not val:
                    continue
                try:
                    parsed = parse_value(val, typ)
                    setattr(box_detection_args, name, parsed)
                except Exception as e:
                    print(f"Errore su '{name}': {e}")

    
    def handle_switch_box_detection_args(self, cmd):
        current_mode = self.box_detection_args.get_mode()
        print(f"[INFO] Modalità attuale: {current_mode.name}")
    
        new_mode = input("Nuova modalità (chunk / connected): ").strip().lower()
    
        if new_mode == "chunk":
            # Ricicla parametri comuni se presenti
            new_args = ChunkCleanupArgs(
                use_erode=self.box_detection_args.use_erode,
                erode_kernel_size=self.box_detection_args.erode_kernel_size,
                erode_iterations=self.box_detection_args.erode_iterations,
                use_dilate=self.box_detection_args.use_dilate,
                dilate_kernel_size=self.box_detection_args.dilate_kernel_size,
                dilate_iterations=self.box_detection_args.dilate_iterations,
                ligth_upper_level=self.box_detection_args.ligth_upper_level
            )
            print("[INFO] Passato a modalità CHUNK.")
    
        elif new_mode == "connected":
            new_args = ConnectedCleanupArgs(
                use_erode=self.box_detection_args.use_erode,
                erode_kernel_size=self.box_detection_args.erode_kernel_size,
                erode_iterations=self.box_detection_args.erode_iterations,
                use_dilate=self.box_detection_args.use_dilate,
                dilate_kernel_size=self.box_detection_args.dilate_kernel_size,
                dilate_iterations=self.box_detection_args.dilate_iterations,
                ligth_upper_level=self.box_detection_args.ligth_upper_level
            )
            print("[INFO] Passato a modalità CONNECTED.")
    
        else:
            print("[ERRORE] Modalità non valida. Usa 'chunk' o 'connected'.")
            return
    
        self.box_detection_args = new_args
        

    def handle_show_box_detection_args(self, cmd):
        print("== Parametri box_detection_args ==")
        for attr in dir(self.box_detection_args):
            if attr.startswith("_") or callable(getattr(self.box_detection_args, attr)):
                continue
            print(f"{attr}: {getattr(self.box_detection_args, attr)}")

    def export_cleaned_pages(self, output_folder):
        for index, img in self.cleaned_pages.items():
            path = os.path.join(output_folder, f"page_{index:03d}.png")
            img.save(path)
            print(f"[SAVED] {path}")

    
    def handle_next(self, cmd):
        self.cleaned_pages[self.page_index] = self.current_image
        self.page_index = min(self.page_index + 1, len(self.pages) - 1)
        self.current_image = self.cleaned_pages[self.page_index]
        

    def handle_prev(self, cmd):
        self.cleaned_pages[self.page_index] = self.current_image
        self.page_index = max(self.page_index - 1, 0)
        self.current_image = self.cleaned_pages[self.page_index]

    def handle_quit(self, cmd):
        self.running = False

