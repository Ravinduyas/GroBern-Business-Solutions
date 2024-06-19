import os
import fnmatch
import tkinter as tk
from tkinter import filedialog, messagebox

def search_files_and_folders(directory, pattern):
    matches = []
    for root, dirs, files in os.walk(directory):
        # Search in directories
        for dir_name in dirs:
            if fnmatch.fnmatch(dir_name, pattern):
                matches.append(os.path.join(root, dir_name))
        # Search in files
        for file_name in files:
            if fnmatch.fnmatch(file_name, pattern):
                matches.append(os.path.join(root, file_name))
    return matches

#

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)

def start_search():
    directory = entry_directory.get()
    pattern = entry_pattern.get()
    if not directory or not pattern:
        messagebox.showwarning("Input Error", "Please provide both directory and search pattern.")
        return
    
    results = search_files_and_folders(directory, pattern)
    listbox_results.delete(0, tk.END)
    for match in results:
        listbox_results.insert(tk.END, match)

# Create the main window
root = tk.Tk()
root.title("File and Folder Search")

# Create and place the directory entry and button
frame_directory = tk.Frame(root)
frame_directory.pack(padx=10, pady=5, fill=tk.X)
label_directory = tk.Label(frame_directory, text="Directory:")
label_directory.pack(side=tk.LEFT)
entry_directory = tk.Entry(frame_directory, width=50)
entry_directory.pack(side=tk.LEFT, padx=5)
button_browse = tk.Button(frame_directory, text="Browse", command=browse_directory)
button_browse.pack(side=tk.LEFT)

# Create and place the pattern entry
frame_pattern = tk.Frame(root)
frame_pattern.pack(padx=10, pady=5, fill=tk.X)
label_pattern = tk.Label(frame_pattern, text="Folder Name:")
label_pattern.pack(side=tk.LEFT)
entry_pattern = tk.Entry(frame_pattern, width=50)
entry_pattern.pack(side=tk.LEFT, padx=5)

# Create and place the search button
button_search = tk.Button(root, text="Search", command=start_search)
button_search.pack(pady=10)

# Create and place the results listbox with a scrollbar
frame_results = tk.Frame(root)
frame_results.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame_results, orient=tk.VERTICAL)
listbox_results = tk.Listbox(frame_results, yscrollcommand=scrollbar.set, width=80, height=20)
scrollbar.config(command=listbox_results.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_results.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
