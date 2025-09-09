import pytesseract
from PIL import Image

# Windows path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)
