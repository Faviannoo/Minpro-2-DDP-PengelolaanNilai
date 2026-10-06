# Minpro-2-DDP-PengelolaanNilai

Nama: Muhammad Favian Daffa<br>
Kelas: 26A<br>
NIM: 2609116021<br>
<br>
Penjelasan kode :<br>

1. Import Library dan Data Awal

| Library | Penjelasan |
| --- | --- |
| `PrettyTable` | Membuat tabel untuk menampilkan data agar lebih rapi di terminal |
| `pwinput` | Menyembunyikan input password saat pengguna mengetik |
| `os` | Digunakan untuk menjalankan perintah sistem, seperti membersihkan layar terminal |

<img width="251" height="85" alt="Screenshot 2026-10-06 001754" src="https://github.com/user-attachments/assets/daec4b85-3141-416d-ba0d-4ad14ad69571" />

Bagian ini merupakan awal program. import os, PrettyTable, dan pwinput digunakan untuk memanggil library yang dibutuhkan dalam program. Kemudian data_mahasiswa = [] digunakan untuk membuat list kosong sebagai tempat penyimpanan data mahasiswa<br>
<br>

2. Function OS
<img width="209" height="47" alt="Screenshot 2026-10-06 001803" src="https://github.com/user-attachments/assets/b3b554dc-dba4-4264-aa87-ce45725381dd" />

Bagian ini digunakan untuk membuat fungsi bersihkan_layar(). Fungsi tersebut menggunakan os.system("cls") untuk membersihkan tampilan layar pada Windows agar setiap menu yang ditampilkan terlihat lebih rapi<br>
<br>

3. Data Akun

| Akun | Password | Role |
| --- | --- | --- |
| `dosen` | `dosen123` | `admin` |
| `mahasigma` | `user123` | `user` |

<img width="227" height="157" alt="Screenshot 2026-10-06 001815" src="https://github.com/user-attachments/assets/a2f85904-3fe3-43b7-ab73-d816f9b7b4fc" />

Bagian ini digunakan untuk menyimpan data akun yang dapat digunakan untuk login. Setiap akun memiliki username, password, dan role. Role digunakan untuk membedakan hak akses antara admin dan user<br>
<br>

4. Function Login
<img width="454" height="290" alt="Screenshot 2026-10-06 001832" src="https://github.com/user-attachments/assets/e9b245c9-a8ea-44d0-b485-daa03ba536c7" />

Bagian ini digunakan untuk melakukan proses login. Pengguna memasukkan username dan password, kemudian program akan mencocokkannya dengan data akun. Jika benar, pengguna akan masuk ke dalam program sesuai dengan role yang dimiliki<br>
<br>

5. Function Tambah Nilai
<img width="305" height="478" alt="Screenshot 2026-10-06 002009" src="https://github.com/user-attachments/assets/0952cb51-8e65-46f1-9167-3350f7955fed" />

Bagian ini digunakan untuk menambahkan data mahasiswa. Pengguna memasukkan nama, nilai tugas, UTS, dan UAS. Setiap nilai diperiksa agar berada pada rentang 0 sampai 100, kemudian data disimpan ke dalam data_mahasiswa<br>
<br>

6. Function Tampilkan Nilai
<img width="235" height="486" alt="Screenshot 2026-10-06 002025" src="https://github.com/user-attachments/assets/a9994d4a-4183-4227-a87a-83412385df0d" />

Bagian ini digunakan untuk menampilkan seluruh data mahasiswa dalam bentuk tabel menggunakan PrettyTable. Program juga menghitung nilai akhir berdasarkan bobot tugas 30%, UTS 30%, dan UAS 40%, kemudian menentukan grade dari A sampai E<br>
<br>

7. Function Ubah Nilai
<img width="353" height="510" alt="Screenshot 2026-10-06 002041" src="https://github.com/user-attachments/assets/889703aa-e404-47c6-a804-b57e7f9fbcd3" />

Bagian ini digunakan untuk mengubah nilai mahasiswa yang sudah tersimpan. Program mencari data berdasarkan nama mahasiswa, kemudian pengguna dapat memasukkan nilai tugas, UTS, dan UAS yang baru<br>
<br>

8. Function Hapus Nilai
<img width="313" height="212" alt="Screenshot 2026-10-06 002049" src="https://github.com/user-attachments/assets/1cdb749a-40c3-4387-88e2-74d01873dd0c" />

Bagian ini digunakan untuk menghapus data mahasiswa. Pengguna memasukkan nama mahasiswa yang ingin dihapus, kemudian program mencari data tersebut dan menghapusnya dari list data_mahasiswa<br>
<br>

9. Function Menu
<img width="275" height="449" alt="Screenshot 2026-10-06 002100" src="https://github.com/user-attachments/assets/220313e6-f321-4155-a8a9-80b1dcfcb004" />

Bagian ini digunakan untuk menampilkan menu berdasarkan role pengguna. Admin memiliki akses untuk menambah, menampilkan, mengubah, dan menghapus nilai, sedangkan user hanya memiliki akses untuk menampilkan nilai. Menu akan terus berjalan sampai pengguna memilih keluar<br>
<br>

10. Program Utama
<img width="263" height="156" alt="Screenshot 2026-10-06 002105" src="https://github.com/user-attachments/assets/1146740e-e628-4dd1-bfa4-d181a7b26e6c" />

Bagian ini merupakan bagian yang menjalankan keseluruhan program. Fungsi main() memanggil proses login, kemudian menampilkan menu sesuai role pengguna. Setelah logout, pengguna dapat memilih untuk kembali login atau keluar dari program.<br>
<br>

OUTPUT :<br>

<img width="161" height="124" alt="Screenshot 2026-10-06 004432" src="https://github.com/user-attachments/assets/a3253ab7-b35f-4aaf-ab16-8dcfb4a8b0f9" /><br>
<img width="158" height="110" alt="Screenshot 2026-10-06 004441" src="https://github.com/user-attachments/assets/58921cd9-46dd-43c9-9ca8-01d3c7b145cf" /><br>
<img width="158" height="119" alt="Screenshot 2026-10-06 004536" src="https://github.com/user-attachments/assets/467d08cf-0dd5-490f-a240-af3425dab5d1" /><br>
<img width="250" height="110" alt="Screenshot 2026-10-06 004545" src="https://github.com/user-attachments/assets/a41eefbb-572d-42d5-acad-6ba8d1f8221c" /><br>
<img width="190" height="130" alt="Screenshot 2026-10-06 004607" src="https://github.com/user-attachments/assets/2a144398-ed0e-4752-b5fc-836c331d1f27" /><br>
<img width="223" height="54" alt="Screenshot 2026-10-06 004616" src="https://github.com/user-attachments/assets/f2cf893e-1a96-4c46-ad08-5f280fd8dbdf" /><br>

<br>
<br>
<br>

FLOWCHART:<br>

<img width="2537" height="1431" alt="MINPROO2 drawio (3)" src="https://github.com/user-attachments/assets/a08606bb-12ec-4909-b7b8-9b4f0de86b69" />











