from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_MODELS = Path(r"D:\decimo\VAunidad1\MODELOS FINALES")
MODEL_DIR = PROJECT_ROOT / "models"
METRICS_PATH = MODEL_DIR / "comparison_results.csv"
CLASS_NAMES_PATH = MODEL_DIR / "class_names.json"
MODEL_FILES = {
    "CNN from scratch": "cnn_scratch_best.pth",
    "MobileNetV2": "mobilenetv2_transfer_best.pth",
    "Vision Transformer": "vit_b16_transfer_best.pth",
}
MODEL_INPUTS = {
    "CNN from scratch": (128, [0.5] * 3, [0.5] * 3),
    "MobileNetV2": (224, [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    "Vision Transformer": (224, [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
}

def load_class_names():
    source_path = SOURCE_MODELS / "class_names.json"
    path = CLASS_NAMES_PATH if CLASS_NAMES_PATH.exists() else source_path
    if not path.is_file():
        raise FileNotFoundError(f"No se encontró class_names.json en {path}")
    names = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(names, list) or len(names) != 10 or not all(isinstance(x, str) for x in names):
        raise ValueError("class_names.json debe contener la lista ordenada de diez clases.")
    return names
