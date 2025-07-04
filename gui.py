import tkinter as tk
from tkinter import filedialog, messagebox
from utils.merge import merge_pdfs
from utils.encrypt import encrypt_pdf
from utils.decrypt import decrypt_pdf

# window
root = tk.Tk()
root.title("PDF Toolkit GUI")
root.geometry("600x400")

selected_files = []

# Functions
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
        encrypt_pdf(selected_files[0], "assets/encrypted_output.pdf", "1234")
        messagebox.showinfo("Success", "PDF encrypted with password: 1234")
    else:
        messagebox.showwarning("Warning", "No file selected!")

def decrypt():
    if selected_files:
        decrypt_pdf(selected_files[0], "assets/decrypted_output.pdf", "1234")
        messagebox.showinfo("Success", "PDF decrypted successfully!")
    else:
        messagebox.showwarning("Warning", "No file selected!")

# GUI Layout
btn_style = {"width": 25, "height": 2, "font": ("Helvetica", 12)}

tk.Button(root, text="Browse PDF Files", command=browse_files, **btn_style).pack(pady=10)
tk.Button(root, text="Merge PDFs", command=merge, **btn_style).pack(pady=5)
tk.Button(root, text="Encrypt PDF", command=encrypt, **btn_style).pack(pady=5)
tk.Button(root, text="Decrypt PDF", command=decrypt, **btn_style).pack(pady=5)


tk.Button(
    root,
    text="PDF toolkit",
    command=browse_files,
    width=25,
    height=2,
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",            # Green
    fg="white",              # White text
    activebackground="#388E3C"  # Darker green when clicked
).pack(pady=10)



root.mainloop()






