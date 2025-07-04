import PyPDF2

def decrypt_pdf(input_pdf, output_pdf, password):
    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            if reader.is_encrypted:
                if reader.decrypt(password):
                    writer = PyPDF2.PdfWriter()

                    for page in reader.pages:
                        writer.add_page(page)

                    with open(output_pdf, 'wb') as output_file:
                        writer.write(output_file)

                    print(f" PDF decrypted and saved as {output_pdf}")
                else:
                    print(" Incorrect password. Cannot decrypt.")
            else:
                print("ℹ File is not encrypted.")

    except FileNotFoundError:
        print(" Input file not found.")
    except Exception as e:
        print(f" Error while decrypting PDF: {e}")
