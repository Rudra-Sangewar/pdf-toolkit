from utils.merge import merge_pdfs
from utils.encrypt import encrypt_pdf

# First, merge 2 PDFs
pdfs = ['assets/sample1.pdf', 'assets/sample2.pdf']
merged_file = 'assets/merged_output.pdf'
merge_pdfs(pdfs, merged_file)

# Then, encrypt the merged file
encrypted_file = 'assets/encrypted_output.pdf'
password = 'Rudra2004'
encrypt_pdf(merged_file, encrypted_file, password)
