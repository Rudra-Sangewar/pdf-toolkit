import PyPDF2

def extract_pages(input_pdf, output_pdf, pages_to_extract):
    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            for page_num in pages_to_extract:
                writer.add_page(reader.pages[page_num - 1])  # -1 for 0-based index

            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)

        print(f" Extracted pages saved to {output_pdf}")
    except FileNotFoundError:
        print(" Input file not found.")
    except IndexError:
        print(" One or more page numbers are out of range.")
    except Exception as e:
        print(f" Error while extracting pages: {e}")
