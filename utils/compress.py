import fitz 

def compress_pdf(input_pdf, output_pdf, quality=75):
    try:
        doc = fitz.open(input_pdf)
        for page in doc:
            pix = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
            page.clean_contents()
        doc.save(output_pdf, garbage=4, deflate=True)
        print(f" Compressed PDF saved as {output_pdf}")
    except Exception as e:
        print(f" Error while compressing PDF: {e}")
