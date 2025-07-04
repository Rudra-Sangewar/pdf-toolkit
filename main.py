from utils.merge import merge_pdfs
from utils.encrypt import encrypt_pdf
from utils.decrypt import decrypt_pdf
from utils.extract import extract_pages
from utils.compress import compress_pdf

pdfs = ['assets/sample1.pdf', 'assets/sample2.pdf']
merged_file = 'assets/merged_output.pdf'
merge_pdfs(pdfs, merged_file)

encrypted_file = 'assets/encrypted_output.pdf'
password = 'Rudra2004'
encrypt_pdf(merged_file, encrypted_file, password)

input_pdf ='assets/encrypted_output.pdf'
output_pdf = 'assets/decrypted_output.pdf'
password = 'Rudra2004'
decrypt_pdf(input_pdf, output_pdf, password)

input_pdf = 'assets/merged_output.pdf'
output_pdf = 'assets/extracted_output.pdf'
pages_to_extract = [1, 2] 
extract_pages(input_pdf, output_pdf, pages_to_extract)

input_pdf = 'assets/sample1.pdf'   
output_pdf = 'assets/compressed_output.pdf'
compress_pdf(input_pdf, output_pdf)