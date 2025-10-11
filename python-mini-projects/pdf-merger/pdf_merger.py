import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f4f7")

        self.pdf_file = []

        self.create_widgets()

    def create_widgets(self):
        # title label
        title_label = tk.Label(
            self.root,
            text="PDF Merger",
            font=("Arial", 12),
            bg="#f0f4f7",
            fg="#333"
        )
        title_label.pack(pady=10)

        # listbox to display selected PDF files
        self.listbox = tk.Listbox(
            self.root, selectmode=tk.MULTIPLE, width=50, height=10, font=("Arial", 12)
        )
        self.listbox.pack(pady=10)

        # button frame
        button_frame = tk.Frame(self.root, bg="#f0f4f7")
        button_frame.pack(pady=10)

        # add file button
        add_file_button = tk.Button(
            button_frame,
            text="Add Files",
            command=self.add_files,
            bg="#007bff",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        add_file_button.pack(pady=10)

        # remove file button
        remove_file_button = tk.Button(
            button_frame,
            text="Remove Selected",
            command=self.remove_selected,
            bg="#dc3545",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        remove_file_button.pack(side="left", padx=5)

        # merge pdf button
        merge_button = tk.Button(
            self.root,
            text="Merge PDFs",
            command=self.merge_pdf,
            bg="#28a745",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10
        )
        merge_button.pack(pady=20)

    def add_files(self):
        files = filedialog.askopenfilenames(
            filetypes=[("PDF Files", "*.pdf")],
            title="Select PDF Files"
        )
        for file in files:
            if file not in self.pdf_file:
                self.pdf_file.append(file)
                self.listbox.insert(tk.END, file)

    def remove_selected(self):
        selected_indices = self.listbox.curselection()
        for index in reversed(selected_indices):
            self.pdf_file.pop(index)
            self.listbox.delete(index)

    def merge_pdf(self):
        if not self.pdf_file:
            messagebox.showwarning("No files", "Please add at least two PDF files to merge.")
            return
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[
                ("PDF Files", "*.pdf")
            ],
            title="Save Merged PDF as"
        )
        if not save_path:
            return
        
        try:
            merger = PdfMerger()
            for pdf in self.pdf_file:
                merger.append(pdf)
            merger.write(save_path)
            merger.close()

            messagebox.showinfo("Success", f"Merged PDF saved to:\n{save_path}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while merging PDFs:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()