import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, END
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.root.geometry("600x600")

        # Listbox to show selected PDFs
        self.file_listbox = Listbox(root, selectmode=tk.SINGLE, width=60, height=15)
        self.file_listbox.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add PDFs", command=self.add_pdfs).pack(pady=5)
        tk.Button(root, text="Remove Selected", command=self.remove_pdf).pack(pady=5)
        tk.Button(root, text="Move Up", command=self.move_up).pack(pady=2)
        tk.Button(root, text="Move Down", command=self.move_down).pack(pady=2)
        tk.Button(root, text="Merge PDFs", command=self.merge_pdfs, bg="green", fg="white").pack(pady=15)

        self.pdf_files = []

    def add_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.file_listbox.insert(END, file.split("/")[-1])

    def remove_pdf(self):
        selected = self.file_listbox.curselection()
        if selected:
            index = selected[0]
            self.file_listbox.delete(index)
            self.pdf_files.pop(index)

    def move_up(self):
        selected = self.file_listbox.curselection()
        if selected and selected[0] > 0:
            index = selected[0]
            self.pdf_files[index], self.pdf_files[index-1] = self.pdf_files[index-1], self.pdf_files[index]
            self.refresh_listbox()
            self.file_listbox.selection_set(index-1)

    def move_down(self):
        selected = self.file_listbox.curselection()
        if selected and selected[0] < len(self.pdf_files)-1:
            index = selected[0]
            self.pdf_files[index], self.pdf_files[index+1] = self.pdf_files[index+1], self.pdf_files[index]
            self.refresh_listbox()
            self.file_listbox.selection_set(index+1)

    def refresh_listbox(self):
        self.file_listbox.delete(0, END)
        for file in self.pdf_files:
            self.file_listbox.insert(END, file.split("/")[-1])

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("Error", "No PDF files selected!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if save_path:
            merger = PdfMerger()
            for pdf in self.pdf_files:
                merger.append(pdf)
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved as:\n{save_path}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
