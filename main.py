import tkinter as tk
from tkinter import filedialog, messagebox
from sorter import sort_files, preview_files

def choose_folder():
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        folder_path.set(selected_folder)
        btn_sort.config(state="normal")
        status_label.config(text = "Folder selected. Ready to sort.")


def make_preview_text(summary):
    return "\n".join([f"{k}: {v} files" for k, v in summary.items()])


def make_skipped_text(skipped):
    if skipped:
        return ", ".join(skipped)
    return "None"

def run_sort():
    if not folder_path.get():
        status_label.config(text = "Please select a folder first.")
        return
    
    category_summary = preview_files(folder_path.get())
    preview_text = make_preview_text(category_summary)

    confirm = messagebox.askyesno(
        "Preview",
        f"{preview_text}\n\nProceed?"
    )
        
    if not confirm:
        status_label.config(text = "Sorting Cancelled.")
        return
    
    moved, skipped_files, renamed = sort_files(folder_path.get())
    skipped_text = make_skipped_text(skipped_files)
   

    messagebox.showinfo(
        "Sorting complete",
        f"Moved: {moved}\nSkipped: {skipped_text}\nRenamed: {renamed}"
    )

root = tk.Tk()
root.title("File Sorter")
root.geometry("700x350")

folder_path = tk.StringVar(value = "No Folder selected.")

title = tk.Label(root, text = "File Sorter", font=("Arial", 16))
title.pack(pady=10)

btn_choose = tk.Button(root, text = "Choose Folder", command = choose_folder)
btn_choose.pack(pady=5)

folder_label = tk.Label(root, textvariable = folder_path)
folder_label.pack(pady=5)

btn_sort = tk.Button(root, text = "Sort Files", command = run_sort, state = "disabled")
btn_sort.pack(pady=10)

status_label = tk.Label(root, text="", wraplength=700, justify="center")
status_label.pack(pady=10)
root.mainloop()