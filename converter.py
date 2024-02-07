import os
import ffmpeg

class Converter:
    @staticmethod
    def convert_mp4_to_format(files, output_folder, selected_conversion, progress_label, root):
        total_files = len(files)
        for i, mp4_file in enumerate(files, start=1):
            if selected_conversion == "MP4 to MP3":
                output_extension = ".mp3"
                output_path = os.path.splitext(mp4_file)[0] + output_extension
                ffmpeg.input(mp4_file).output(output_path, format='mp3', codec='copy').run()
            elif selected_conversion == "MP4 to MKV":
                output_extension = ".mkv"
                output_path = os.path.splitext(mp4_file)[0] + output_extension
                ffmpeg.input(mp4_file).output(output_path, codec='copy').run()
                
            progress_label.config(text=f"Konversi: {i}/{total_files}")
            root.update()

    @staticmethod
    def convert_format_to_mp4(files, output_folder, progress_label, root):
        total_files = len(files)
        for i, input_file in enumerate(files, start=1):
            output_file = os.path.splitext(os.path.basename(input_file))[0] + ".mp4"
            output_path = os.path.join(output_folder, output_file)
            
            # Using ffmpeg-python for format to MP4 conversion
            ffmpeg.input(input_file).output(output_path, codec='copy').run()
            
            progress_label.config(text=f"Konversi: {i}/{total_files}")
            root.update()
