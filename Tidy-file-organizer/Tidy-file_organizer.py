import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

class FileOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Tidy-File Organizer")

        self.default_directory = r"C:\Users\Insight\Downloads"
        
        self.frame_directory = tk.Frame(root)
        self.frame_directory.pack(padx=10, pady=5, fill=tk.X)

        self.label_directory = tk.Label(self.frame_directory, text="Downloads Directory:")
        self.label_directory.pack(side=tk.LEFT)

        self.entry_directory = tk.Entry(self.frame_directory, width=50)
        self.entry_directory.pack(side=tk.LEFT, padx=5)
        self.entry_directory.insert(0, self.default_directory)

        self.button_browse = tk.Button(self.frame_directory, text="Browse", command=self.browse_directory)
        self.button_browse.pack(side=tk.LEFT)

        self.button_organize = tk.Button(root, text="Organize", command=self.organize_files)
        self.button_organize.pack(pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.entry_directory.delete(0, tk.END)
            self.entry_directory.insert(0, directory)

    def organize_files(self):
        directory = self.entry_directory.get()
        if not directory:
            messagebox.showwarning("Input Error", "Please provide the Downloads directory.")
            return

        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path) and item.startswith("Tidy-"):
                # Skip folders that are already sorted
                continue

            if os.path.isfile(item_path) or os.path.isdir(item_path):
                creation_time = os.path.getctime(item_path)
                creation_date = datetime.fromtimestamp(creation_time).strftime('%Y%m%d')
                destination_folder = os.path.join(directory, f"Tidy-{creation_date}")
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(item_path, os.path.join(destination_folder, item))
                
        messagebox.showinfo("Success", "Files have been organized by creation date.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizer(root)
    root.mainloop()
