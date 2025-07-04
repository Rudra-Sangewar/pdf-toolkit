import PyPDF2

def encrypt_pdf(input_pdf, output_pdf, password):
    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)

        print(f"Encrypted PDF saved as {output_pdf}")
    except FileNotFoundError:
        print(" Input file not found.")
    except Exception as e:
        print(f" Error while encrypting PDF: {e}")
