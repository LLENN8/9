# Misa Converter
<img src="Screenshot.png" width="400">

Misa Converter adalah program media converter dengan kualitas seadanya menggunakan python.

> Ayahku terlalu tua untuk menggunakan aplikasi converter diluaran dengan penggunaanya yang kompleks. aku cukup frustasi mencari aplikasi converter yang cocok untuknya. Setelah mencoba beberapa aplikasi converter dan ia menolak, aku memutuskan membuat sendiri dengan tampilan dan alur penggunaan yang mudah. Approved by my Father.

## Konversi Format yang di support
* mp4 ke mp3
* mp4 ke mkv
* mkv ke mp4

📝 [Catatan]: Jika ayahku meminta format lain, aku akan mempertimbangkan menambahkan konversi format lain


## Instalasi

### Menjalankan Langsung Misa_Converter.py

1. **Menginstall Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Menjalankan Program:**
    ```bash
    python Misa_Converter.py
    ```

### Membuat Executable untuk Windows

1. **Menginstall Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Menginstall cx_Freeze:**
    ```bash
    pip install cx_Freeze
    ```

3. **Membuat Executable:**
    ```bash
    python setup.py build
    ```

4. **Menjalankan Program:**
    Jalankan file Misa_Converter.exe yang ada di folder `..\build\exe.win-amd64-3.11`

📝 **Catatan**: Misa Converter hanya diuji pada Windows 10 dan 11. Kemungkinan tidak kompatibel dengan sistem operasi lainnya.

## Penggunaan
<img src="Screenshot_2.png" width="400">

1. Jalankan program
2. klik "Pilih Konversi... ▼" untuk memilih jenis konversi
2. Klik tombol "Open File" untuk memilih file video yang ingin dikonversi 
3. Klik tombol "Convert" untuk memulai konversi
4. Setelah konversi selesai, Anda dapat membuka folder tempat hasil konversi disimpan dengan mengklik tombol "Buka Folder Hasil".

📝 [Catatan]: Folder untuk hasil output yang sudah terkonversi harusnya berada pada folder Videos bawaan pada os Windows `C:\Users\NameOfUser\Videos\Misa Converter`.

## Lisensi

Program ini dilisensikan di bawah [MIT License](LICENSE).






