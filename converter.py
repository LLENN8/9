import os
import ffmpeg

class Converter:
    @staticmethod
    def convert_files(files, output_folder, selected_conversion, progress_label, root):
        total_files = len(files)
        for i, input_file in enumerate(files, start=1):
            output_file = os.path.splitext(os.path.basename(input_file))[0]
            if selected_conversion == "MP4 to MP3":
                output_extension = ".mp3"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, format='mp3', codec='copy', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "MKV to MP3":
                output_extension = ".mp3"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, format='mp3', codec='copy', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "AVI to MP3":
                output_extension = ".mp3"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, format='mp3', codec='copy', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "MP4 to MKV":
                output_extension = ".mkv"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, codec='copy', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "MKV to MP4":
                output_extension = ".mp4"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, codec='copy', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "AVI to MP4":
                output_extension = ".mp4"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, codec='copy', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "MP4 to AVI":
                output_extension = ".avi"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, vcodec='libx264', acodec='mp3', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "MKV to AVI":
                output_extension = ".avi"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, vcodec='libx264', acodec='mp3', y='-y').run(capture_stdout=True, capture_stderr=True)
            elif selected_conversion == "AVI to MKV":
                output_extension = ".mkv"
                output_path = os.path.join(output_folder, output_file + output_extension)
                ffmpeg.input(input_file).output(output_path, vcodec='libx264', acodec='mp3', y='-y').run(capture_stdout=True, capture_stderr=True)
            
            if progress_label.winfo_exists():
                progress_label.config(text=f"Konversi: {i}/{total_files}")
                root.update()

