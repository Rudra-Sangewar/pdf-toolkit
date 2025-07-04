import PyPDF2

def reorder_pages(input_pdf, output_pdf, new_order):
    try:
        with open(input_pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            total_pages = len(reader.pages)

            for page_num in new_order:
                if 1 <= page_num <= total_pages:
                    writer.add_page(reader.pages[page_num - 1])
                else:
                    print(f"⚠️ Page number {page_num} is out of range and will be skipped.")

            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)

        print(f" Reordered PDF saved to {output_pdf}")
    except FileNotFoundError:
        print(" Input file not found.")
    except Exception as e:
        print(f" Error while reordering PDF: {e}")
