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
    def convert_selected(listbox, progress_label, progress_bar, root):
        selected_videos = listbox.get(0, tk.END)
        if not selected_videos:
            messagebox.showerror("Error", "Pilih setidaknya satu video untuk dikonversi.")
            return
        output_folder_selected = os.path.join(os.path.expanduser("~/Videos"), "Misa Converter")
        os.makedirs(output_folder_selected, exist_ok=True)
        Converter.convert_mp4_to_mp3(selected_videos, output_folder_selected, progress_label,
                                      progress_bar, root)
        messagebox.showinfo("Konversi Selesai", "Konversi video ke audio selesai!")
        progress_label.pack_forget()

    @staticmethod
    def open_output_folder():
        output_folder = os.path.join(os.path.expanduser("~/Videos"), "Misa Converter")
        os.makedirs(output_folder, exist_ok=True)
        os.startfile(output_folder)
