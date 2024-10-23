from app.adapter.tesseract_adapter import TesseractOCR
from app.adapter.pdf2image_adpter import PDFConverter

def process_pdf(pdf_path):
    pdf2image = PDFConverter(dev_mode=True)
    extract_images = pdf2image.convert_pdf_to_images(pdf_path)
    return extract_images

def process_image(images):
    custom_config = r"--oem 3 --psm 6"
    ocr = TesseractOCR(dev_mode=True)

    extracted_text = ""
    for image in images:
        text = ocr.image_to_string(image, custom_config)
        extracted_text += text + "\n"

    return extracted_text
