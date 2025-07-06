import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox, simpledialog
from utils.merge import merge_pdfs
from utils.encrypt import encrypt_pdf
from utils.decrypt import decrypt_pdf
from utils.compress import compress_pdf
from utils.extract import extract_pages
from utils.watermark import apply_watermark





root = ttk.Window(themename="flatly")  # Try: "darkly", "superhero", "cyborg"
root.title("🛠️ PDF Toolkit")
root.geometry("500x400")

# File selection
selected_files = []

def browse_files():
    global selected_files
    selected_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    messagebox.showinfo("Files Selected", f"{len(selected_files)} file(s) selected.")

def merge():
    if selected_files:
        merge_pdfs(selected_files, "assets/merged_output.pdf")
        messagebox.showinfo("Success", "PDFs merged successfully!")
    else:
        messagebox.showwarning("Warning", "No files selected!")

def encrypt():
    if selected_files:
        encrypt_pdf(selected_files[0], "assets/encrypted_output.pdf", "Rudra2004")
        messagebox.showinfo("Success", "Encrypted with password: Rudra2004")
    else:
        messagebox.showwarning("Warning", "No file selected!")

def decrypt():
    if selected_files:
        decrypt_pdf(selected_files[0], "assets/decrypted_output.pdf", "1234")
        messagebox.showinfo("Success", "Decrypted successfully!")
    else:
        messagebox.showwarning("Warning", "No file selected!")

def compress():
    if selected_files:
        compress_pdf(selected_files[0], "assets/compressed_output.pdf")
        messagebox.showinfo("Success", "PDF compressed successfully!")
    else:
        messagebox.showwarning("Warning", "No file selected!")

def extract():
    if selected_files:
        pages_str = simpledialog.askstring(
            "Extract Pages",
            "Enter pages to extract (e.g., 0,2 for 1st & 3rd):"
        )

        if pages_str:
            try:
                pages = [int(x.strip()) for x in pages_str.split(',')]
                extract_pages(selected_files[0], "assets/extracted_output.pdf", pages)
                messagebox.showinfo("Success", "Pages extracted successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid page input.")
    else:
        messagebox.showwarning("Warning", "No file selected!")

def watermark():
    if selected_files:
        text = simpledialog.askstring(
            "Watermark Text",
            "Enter text to add as watermark:"
        )

        if text:
            apply_watermark(selected_files[0], "assets/watermarked_output.pdf", text)
            messagebox.showinfo("Success", "Watermark added successfully!")
    else:
        messagebox.showwarning("Warning", "No file selected!")


button_style = {
    "width": 25,
    "bootstyle": "success",  
    "padding": 10
}

ttk.Button(root, text="📂 Browse PDF Files", command=browse_files, **button_style).pack(pady=10)
ttk.Button(root, text="➕ Merge PDFs", command=merge, **button_style).pack(pady=5)
ttk.Button(root, text="🔒 Encrypt PDF", command=encrypt, **button_style).pack(pady=5)
ttk.Button(root, text="🔓 Decrypt PDF", command=decrypt, **button_style).pack(pady=5)
ttk.Button(root, text="📉 Compress PDF", command=compress, **button_style).pack(pady=5)
ttk.Button(root, text="📄 Extract Pages", command=extract, **button_style).pack(pady=5)
ttk.Button(root, text="💧 Add Watermark", command=watermark, **button_style).pack(pady=5)


root.mainloop()
