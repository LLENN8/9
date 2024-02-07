# Misa Converter
<img src="Screenshot.png" width="400">

Misa Converter adalah program media converter menggunakan FFmpeg dan python.

> Ayahku sudah tua dan kesulitan menggunakan aplikasi converter dengan ui kompleks di luar sana, sehingga saya membuatkan program dengan interface yang mudah. Approved by my Father.

## Konversi Format yang di support
* MP4 ke MP3
* MKV ke MP3
* AVI ke MP3
* MP4 ke MKV
* MP4 ke AVI
* MKV ke MP4
* MKV ke AVI
* AVI ke MP4
* AVI ke MKV

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


⚠️ **Peringatan**: Misa Converter menggunakan FFmpeg. Pastikan FFmpeg sudah terinstall pada sistem. Untuk instalasi FFmpeg dapat didownload [disini](https://www.ffmpeg.org/download.html)

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






