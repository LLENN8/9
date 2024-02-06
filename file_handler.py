import os
import tkinter as tk
from tkinter import filedialog, messagebox
from converter import Converter

class FileHandler:
    @staticmethod
    def select_files(listbox):
        files_selected = filedialog.askopenfilenames(
            filetypes=[("Video Files", "*")],
            title="Pilih File Video"
        )
        listbox.delete(0, tk.END)
        for file_path in files_selected:
            listbox.insert(tk.END, file_path)

    @staticmethod
    def open_output_folder():
        output_folder = os.path.join(os.path.expanduser("~/Videos"), "Misa Converter")
        os.makedirs(output_folder, exist_ok=True)
        os.startfile(output_folder)

