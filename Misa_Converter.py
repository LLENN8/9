import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from moviepy.editor import *

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.editor import concatenate_videoclips,concatenate_audioclips,TextClip,CompositeVideoClip
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize



from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex
#mengapa banyak import manual?, ini karena issue dari library moviepy nya
#lebih lengkap lihat issue di link github berikut
#https://github.com/Zulko/moviepy/issues/591

def convert_mp4_to_mp3(mp4_files, output_folder, progress_label, progress_bar):
    total_files = len(mp4_files)
    progress_step = 100 / total_files
    progress_bar.pack()
    progress_bar.start()
    for i, mp4_file in enumerate(mp4_files, start=1):
        progress = i * progress_step
        progress_bar['value'] = progress
        root.update_idletasks()
        mp3_file = os.path.splitext(os.path.basename(mp4_file))[0] + ".mp3"
        mp3_path = os.path.join(output_folder, mp3_file)

        with VideoFileClip(mp4_file) as video:
            audio = video.audio
            audio.write_audiofile(mp3_path)

        progress_label.config(text=f"Konversi: {i}/{total_files}")
        root.update()
    progress_bar.stop()
    progress_bar.pack_forget()

def select_files():
    files_selected = filedialog.askopenfilenames(
        filetypes=[("Video Files", "*.mp4")],
        title="Pilih File Video"
    )
    listbox.delete(0, tk.END)
    for file_path in files_selected:
        listbox.insert(tk.END, file_path)

def convert_selected():
    selected_videos = listbox.get(0, tk.END)
    if not selected_videos:
        messagebox.showerror("Error", "Pilih setidaknya satu video untuk dikonversi.")
        return
    
    output_folder_selected = os.path.join(os.path.expanduser("~/Videos"), "Misa Converter")
    os.makedirs(output_folder_selected, exist_ok=True)
    convert_mp4_to_mp3(selected_videos, output_folder_selected, progress_label, progress_bar)
    messagebox.showinfo("Konversi Selesai", "Konversi video ke audio selesai!")
    progress_label.pack_forget()


def open_output_folder():
    output_folder = os.path.join(os.path.expanduser("~/Videos"), "Misa Converter")
    os.makedirs(output_folder, exist_ok=True)
    os.startfile(output_folder)

root = tk.Tk()
root.title("Misa Converter")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Convert mp4 to mp3", font=("Arial", 12, "bold")).pack()

tk.Button(frame, text="Open File", command=select_files, font=("Arial", 14)).pack(pady=5)

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, width=75, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Convert", command=convert_selected, font=("Arial", 14)).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Buka Folder Hasil", command=open_output_folder, font=("Arial", 14)).pack(side=tk.LEFT, padx=10)

progress_frame = tk.Frame(root)
progress_frame.pack(pady=10)

progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress_bar.pack(pady=10)
progress_bar.pack_forget()

progress_label = tk.Label(progress_frame, text="")
progress_label.pack()

root.mainloop()
