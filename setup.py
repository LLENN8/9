import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("Misa_Converter.py", base=base)
]

setup(
    name="MisaConverter",
    version="0.1",
    description="Media Converter Program",
    executables=executables
)
