import sys
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import tkinter as tk
from tkinter import filedialog, ttk

def pdf_to_txt(input_pdf, output_txt, progress_callback=None):
    images = convert_from_path(input_pdf)
    total_pages = len(images)

    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image)
            txt_file.write(f"Page {i+1}\n")
            txt_file.write(text)
            txt_file.write("\n\n")

            if progress_callback:
                progress_callback((i + 1) * 100 // total_pages)

def browse_input_pdf():
    input_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_pdf_entry.delete(0, tk.END)
    input_pdf_entry.insert(0, input_pdf)

def browse_output_txt():
    output_txt = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    output_txt_entry.delete(0, tk.END)
    output_txt_entry.insert(0, output_txt)

def convert():
    input_pdf = input_pdf_entry.get()
    output_txt = output_txt_entry.get()

    def update_progress(progress):
        progress_bar["value"] = progress
        root.update_idletasks()

    pdf_to_txt(input_pdf, output_txt, progress_callback=update_progress)

root = tk.Tk()
root.title("PDF to Text Converter")

input_pdf_label = tk.Label(root, text="Input PDF:")
input_pdf_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

input_pdf_entry = tk.Entry(root)
input_pdf_entry.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.E))

input_pdf_button = tk.Button(root, text="Browse", command=browse_input_pdf)
input_pdf_button.grid(row=0, column=2, padx=10, pady=10, sticky=tk.E)

output_txt_label = tk.Label(root, text="Output Text:")
output_txt_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

output_txt_entry = tk.Entry(root)
output_txt_entry.grid(row=1, column=1, padx=10, pady=10, sticky=(tk.W, tk.E))

output_txt_button = tk.Button(root, text="Browse", command=browse_output_txt)
output_txt_button.grid(row=1, column=2, padx=10, pady=10, sticky=tk.E)

progress_label = tk.Label(root, text="Progress:")
progress_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=2, column=1, padx=10, pady=10, sticky=(tk.W, tk.E))

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

root.columnconfigure(1, weight=1)

root.mainloop()
