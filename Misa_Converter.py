import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog, messagebox
from file_handler import FileHandler
from converter import Converter


class TkinterApp:
    listbox = None
    progress_label = None
    

    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Misa Converter")
        self.root.geometry("600x600")
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        conversion_options = [
            "MP4 to MP3",
            "MP4 to MKV",
            "MKV to MP4"
        ]
        self.selected_conversion = tk.StringVar()

        option_menu = ttk.OptionMenu(frame, self.selected_conversion,conversion_options[0], *conversion_options)
        option_menu.pack(pady=5)
        self.selected_conversion.set("Pilih Konversi...")
        menu = option_menu["menu"]
        menu.config(font=("Arial", 12, "bold"))

        tk.Button(frame, text="Open File", command=lambda: FileHandler.select_files(self.listbox),
                  font=("Arial", 14)).pack(pady=5)

        listbox_frame = tk.Frame(self.root)
        listbox_frame.pack(pady=10)
        TkinterApp.listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, width=95, height=20)
        TkinterApp.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        scrollbar.config(command=TkinterApp.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        TkinterApp.listbox.config(yscrollcommand=scrollbar.set)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Convert", command=self.convert_selected_files,
                  font=("Arial", 14)).pack(
            side=tk.LEFT,
            padx=10)
        tk.Button(button_frame, text="Buka Folder Hasil", command=FileHandler.open_output_folder,
                  font=("Arial", 14)).pack(side=tk.LEFT, padx=10)

        self.progress_frame = tk.Frame(self.root)
        self.progress_frame.pack(pady=10)

        TkinterApp.progress_label = tk.Label(self.progress_frame, text="")
        TkinterApp.progress_label.pack()

    def convert_selected_files(self):
        selected_videos = TkinterApp.listbox.get(0, tk.END)
        if not selected_videos:
            messagebox.showerror("Error", "Pilih setidaknya satu file untuk dikonversi.")
            return

        output_folder_selected = os.path.join(os.path.expanduser("~/Videos"), "Misa Converter")
        os.makedirs(output_folder_selected, exist_ok=True)

        selected_conversion = self.selected_conversion.get()
        if selected_conversion == "MP4 to MP3":
            Converter.convert_mp4_to_mp3(selected_videos, output_folder_selected, TkinterApp.progress_label, self.root)
        elif selected_conversion == "MP4 to MKV":
            Converter.convert_mp4_to_mkv(selected_videos, output_folder_selected, TkinterApp.progress_label, self.root)
        elif selected_conversion == "MKV to MP4":
            Converter.convert_mkv_to_mp4(selected_videos, output_folder_selected, TkinterApp.progress_label, self.root)

        messagebox.showinfo("Konversi Selesai", "Konversi selesai!")
        TkinterApp.progress_label.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()

