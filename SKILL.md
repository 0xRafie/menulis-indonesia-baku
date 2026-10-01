---
name: menulis-indonesia-baku
description: Use when writing, editing, translating, or reviewing any Indonesian-language text, especially academic prose (skripsi, tugas akhir, proposal, abstrak, laporan, tugas kuliah, draf paper), or when unsure about kata baku, imbuhan meN-/peN-, tanda koma, huruf miring istilah asing, penulisan angka, struktur SPOK, atau kalimat efektif.
---

# Menulis Bahasa Indonesia Baku

## Overview

Tulisan harus memenuhi kaidah resmi: EYD V (2022), KBBI VI Daring, dan buku penyuluhan Badan Bahasa (2019). Rincian, contoh, dan sumber ada di `referensi.md`.

**Kalau folder skill ini memuat `gaya-pribadi.md`, baca berkas itu sebelum menulis.** Isinya gaya pribadi penulis yang lebih ketat daripada kaidah resmi, dan aturannya menang bila keduanya berbeda.

Kata yang meragukan dicek ke KBBI dengan `python3 <folder skill ini>/cek_kbbi.py kata1 kata2`. Hasil `TIDAK BAKU → X` berarti bentuk bakunya X. Hasil `[CAKAPAN]` berarti kata itu ragam cakapan dan tidak dipakai di tulisan resmi, misalnya mengakomodir (→ mengakomodasi) dan dikarenakan (→ disebabkan, karena).

## Kaidah resmi yang paling sering dilanggar

| Kaidah | Benar | Salah |
|---|---|---|
| Subjek tidak didahului preposisi | Penelitian ini membahas … | Dalam penelitian ini membahas … |
| Tanpa koma bila induk kalimat mendahului anak kalimat | … cepat sehingga mampu … | … cepat, sehingga mampu … |
| Koma sebelum *tetapi*, *melainkan*, *sedangkan* dan sesudah ungkapan antarkalimat | …, tetapi … / Oleh karena itu, … | … tetapi … |
| *Di mana* dan *yang mana* bukan kata penghubung | kota tempat ia kuliah | kota di mana ia kuliah |
| *Daripada* hanya untuk perbandingan | terbuat dari kayu | terbuat daripada kayu |
| Tanpa kata mubazir | merupakan … / membahas masalah / beberapa temuan | adalah merupakan / membahas tentang / beberapa temuan-temuan |
| meN-: *k, p, t, s* luluh, gugus konsonan tidak | memengaruhi, mengubah, menerjemahkan, mengonsumsi, memproduksi, mengkritik | mempengaruhi, merubah, menterjemahkan, mengkonsumsi |
| Kata baku KBBI | analisis, risiko, praktik, sistem, metode, aktivitas, kualitas | analisa, resiko, praktek, sistim, metoda, aktifitas, kwalitas |
| Kata depan terpisah, awalan serangkai | di dalam, ke luar, diambil | didalam, di ambil |
| Istilah asing dimiringkan, nama diri tidak | metode *random forest*, YOLOv8 | metode random forest |
| Imbuhan dengan unsur asing menggunakan tanda hubung | *decoder*-nya, pasca-*training* | decodernya |
| Bilangan satu kata ditulis huruf, selebihnya angka | tiga kali, 12 titik, 0,55 mm, 2.000 citra | dua belas titik, 0.55 mm |
| Kalimat tidak diawali angka | Sebanyak 2.500 citra … | 2.500 citra … |

## Alur

1. Tulis drafnya.
2. Periksa kalimat per kalimat terhadap tabel di atas, dan terhadap `gaya-pribadi.md` bila ada.
3. Cek kata yang meragukan dengan `cek_kbbi.py`.
4. Baca pasangan kalimat berurutan. Pastikan tidak ada kalimat yang muncul tiba-tiba, klausa yang diulang di dua kalimat, atau hubungan sebab-akibat yang dipaksakan.

## Kesalahan yang pernah muncul saat uji

- Koma sebelum *sehingga*.
- "12" diubah menjadi "dua belas". Ini salah, karena bilangan yang butuh dua kata tetap ditulis angka.
