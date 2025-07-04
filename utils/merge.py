import PyPDF2

def merge_pdfs(pdf_list, output_file):
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print(f"File not found: {pdf}")
        except Exception as e:
            print(f"Error while merging {pdf}: {e}")

    merger.write(output_file)
    merger.close()
    print(f"PDFs merged successfully into {output_file}")
