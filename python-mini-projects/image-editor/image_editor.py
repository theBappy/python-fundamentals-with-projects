import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter


class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editing App")
        # Adjusted window size to accommodate image and buttons
        self.root.geometry("1000x600")
        self.root.configure(bg="#e6f7ff")

        self.original_image = None
        self.image = None
        self.image_tk = None

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Load Image Button
        self.load_button = tk.Button(
            self.root, text="Load Image", command=self.load_image, bg="#007bff", fg="white", font=("Arial", 12), padx=10, pady=5
        )
        self.load_button.pack(pady=10)

        # Image Display
        self.image_label = tk.Label(self.root, bg="#e6f7ff")
        self.image_label.pack(pady=10)

        # Filters Section
        self.filters_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.filters_frame.pack(pady=20)

        filters = [
            ("Blur", ImageFilter.BLUR),
            ("Contour", ImageFilter.CONTOUR),
            ("Edge Enhance", ImageFilter.EDGE_ENHANCE),
            ("Emboss", ImageFilter.EMBOSS),
            ("Sharpen", ImageFilter.SHARPEN),
            ("Smooth", ImageFilter.SMOOTH),
        ]

        for filter_name, filter_type in filters:
            tk.Button(
                self.filters_frame, text=filter_name, command=lambda ft=filter_type: self.apply_filter(
                    ft),
                bg="#007bff", fg="white", font=("Arial", 10), padx=10, pady=5
            ).pack(side="left", padx=10, pady=5)

        # Buttons Section
        self.buttons_frame = tk.Frame(self.root, bg="#e6f7ff")
        self.buttons_frame.pack(pady=20)

        # Reset Button
        self.reset_button = tk.Button(
            self.buttons_frame, text="Reset Image", command=self.reset_image, bg="#28a745", fg="white", font=("Arial", 12), padx=10, pady=5
        )
        self.reset_button.pack(side="left", padx=10)

        # Save Image Button
        self.save_button = tk.Button(
            self.buttons_frame, text="Save Image", command=self.save_image, bg="#17a2b8", fg="white", font=("Arial", 12), padx=10, pady=5
        )
        self.save_button.pack(side="left", padx=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            self.original_image = Image.open(file_path)
            self.image = self.original_image.copy()
            self.display_image()

    def display_image(self):
        if self.image:
            aspect_ratio = self.image.width / self.image.height
            new_width = 600
            new_height = int(new_width / aspect_ratio)
            self.image_tk = ImageTk.PhotoImage(
                self.image.resize((new_width, new_height), Image.LANCZOS))
            self.image_label.config(image=self.image_tk)

    def apply_filter(self, filter_type):
        if self.image:
            self.image = self.image.filter(filter_type)
            self.display_image()

    def reset_image(self):
        if self.original_image:
            self.image = self.original_image.copy()
            self.display_image()

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"),
                           ("JPEG files", "*.jpg"), ("All files", "*.*")],
            )
            if file_path:
                self.image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()