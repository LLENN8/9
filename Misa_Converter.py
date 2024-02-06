import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from file_handler import FileHandler
from converter import Converter


class TkinterApp:
    listbox = None
    progress_label = None
    progress_bar = None

    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Misa Converter")
        self.root.geometry("500x400")
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        tk.Label(frame, text="Convert mp4 to mp3", font=("Arial", 12, "bold")).pack()
        tk.Button(frame, text="Open File", command=lambda: FileHandler.select_files(self.listbox),
                  font=("Arial", 14)).pack(pady=5)

        listbox_frame = tk.Frame(self.root)
        listbox_frame.pack(pady=10)
        TkinterApp.listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, width=75, height=10)
        TkinterApp.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        scrollbar.config(command=TkinterApp.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        TkinterApp.listbox.config(yscrollcommand=scrollbar.set)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Convert",
                  command=lambda: FileHandler.convert_selected(self.listbox, self.progress_label, self.progress_bar, self.root),
                  font=("Arial", 14)).pack(
            side=tk.LEFT,
            padx=10)
        tk.Button(button_frame, text="Buka Folder Hasil", command=FileHandler.open_output_folder,
                  font=("Arial", 14)).pack(side=tk.LEFT, padx=10)

        self.progress_frame = tk.Frame(self.root)
        self.progress_frame.pack(pady=10)
        TkinterApp.progress_bar = ttk.Progressbar(self.progress_frame, orient=tk.HORIZONTAL, length=300,
                                                   mode='determinate')
        TkinterApp.progress_bar.pack(pady=10)
        TkinterApp.progress_bar.pack_forget()
        TkinterApp.progress_label = tk.Label(self.progress_frame, text="")
        TkinterApp.progress_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()
