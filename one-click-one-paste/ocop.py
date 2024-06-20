import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from playwright.sync_api import sync_playwright

class ImagePasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Paster")
        
        self.folder_path = None
        self.image_files = []
        self.current_index = 0
        
        # Create GUI elements
        self.label = tk.Label(root, text="Select a folder containing images:")
        self.label.pack(pady=10)
        
        self.select_folder_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=5)
        
        self.copy_images_button = tk.Button(root, text="Copy Images", command=self.copy_images)
        self.copy_images_button.pack(pady=5)
        
        self.paste_image_button = tk.Button(root, text="Paste Image", command=self.paste_image)
        self.paste_image_button.pack(pady=5)
        
        # Initialize Playwright
        self.browser = None
        with sync_playwright() as playwright:
            self.browser = playwright.chromium.launch()

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.image_files = [os.path.join(self.folder_path, file) for file in os.listdir(self.folder_path)
                                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            messagebox.showinfo("Images Found", f"{len(self.image_files)} images found in selected folder.")
        else:
            messagebox.showwarning("No Folder Selected", "Please select a folder containing images.")

    def copy_images(self):
        if not self.image_files:
            messagebox.showwarning("No Images", "Please select a folder with images first.")
            return
        
        # Perform the copying of images (optional step depending on how you handle copying)
        # Here you can choose to load images into memory or perform any other preparation steps.
        
        messagebox.showinfo("Images Copied", "Images copied successfully.")

    def paste_image(self):
        if not self.image_files:
            messagebox.showwarning("No Images", "Please select a folder with images first.")
            return
        
        if self.current_index < len(self.image_files):
            image_path = self.image_files[self.current_index]
            image = Image.open(image_path)
            image_width, image_height = image.size
            
            # Use Playwright to paste the image at current mouse position
            with self.browser.new_context() as context:
                page = context.new_page()
                page.set_viewport_size({"width": image_width, "height": image_height})
                page.goto("about:blank")
                
                # Upload image to a temporary location on the page
                input_file = page.query_selector('input[type="file"]')
                input_file.set_input_files(image_path)
                
                # Click to paste the image
                page.click('input[type="file"]')
                
                self.current_index += 1
                messagebox.showinfo("Image Pasted", f"Pasted image {self.current_index}/{len(self.image_files)}")
        else:
            messagebox.showinfo("All Images Pasted", "All images have been pasted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImagePasterApp(root)
    root.mainloop()
