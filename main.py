from utils.merge import merge_pdfs
from utils.encrypt import encrypt_pdf
from utils.decrypt import decrypt_pdf

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