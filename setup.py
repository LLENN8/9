import sys
from cx_Freeze import setup, Executable

setup(
    name="Misa Converter",
    version="0.1",
    description="Convert mp4 to mp3",
    executables=[Executable("Misa_Converter.py",  target_name="Misa Converter.exe", base="Win32GUI")]
)