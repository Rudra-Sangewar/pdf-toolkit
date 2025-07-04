import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
import io

def create_text_watermark(watermark_text, watermark_file='assets/watermark_temp.pdf'):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    can.saveState()
    can.translate(300, 400)           # Move origin to center-ish
    can.rotate(45)                    # Rotate text 45 degrees
    can.setFont("Helvetica-Bold", 60) # Large bold font
    can.setFillColor(Color(0.7, 0.7, 0.7, alpha=0.2))  # Light transparent gray
    can.drawCentredString(0, 0, watermark_text)
    can.restoreState()

    can.save()
    packet.seek(0)

    with open(watermark_file, 'wb') as f:
        f.write(packet.read())

def apply_watermark(input_pdf, output_pdf, watermark_pdf):
    try:
        with open(input_pdf, 'rb') as file, open(watermark_pdf, 'rb') as watermark_file:
            reader = PdfReader(file)
            watermark = PdfReader(watermark_file)
            watermark_page = watermark.pages[0]
            writer = PdfWriter()

            for page in reader.pages:
                page.merge_page(watermark_page)
                writer.add_page(page)

            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)

        print(f" Watermark applied and saved to {output_pdf}")

    except Exception as e:
        print(f"Error applying watermark: {e}")
