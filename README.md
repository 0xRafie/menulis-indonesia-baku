# menulis-indonesia-baku

Skill untuk agen AI seperti Claude Code, Codex, Factory Droid, dan Grok CLI agar menulis serta menyunting teks bahasa Indonesia sesuai kaidah resmi. Skill ini bisa dipakai oleh agen apa pun yang membaca `SKILL.md`.

## Isi

- `SKILL.md`: daftar kaidah yang paling sering dilanggar beserta alur pemeriksaannya.
- `referensi.md`: rincian struktur kalimat (SPOK), kalimat efektif, imbuhan meN-/peN-, pilihan kata, ejaan EYD V, dan daftar kata baku KBBI, lengkap dengan contoh dan sumbernya.
- `cek_kbbi.py`: pemeriksa kata ke KBBI VI Daring tanpa dependensi tambahan.

## Sumber

- Keputusan Kepala Badan Pengembangan dan Pembinaan Bahasa Nomor 0424/I/BS.00.01/2022 tentang Ejaan Bahasa Indonesia yang Disempurnakan (EYD V).
- Badan Pengembangan dan Pembinaan Bahasa (2019). *Kalimat*. Seri Penyuluhan Bahasa Indonesia.
- Mustakim (2019). *Bentuk dan Pilihan Kata*. Seri Penyuluhan Bahasa Indonesia.
- KBBI VI Daring: https://kbbi.kemendikdasmen.go.id

Contoh kalimat di `referensi.md` dikutip dari sumber di atas dengan menyebut sumbernya.

## Pemasangan

Untuk Claude Code:

```bash
git clone https://github.com/0xRafie/menulis-indonesia-baku ~/.claude/skills/menulis-indonesia-baku
```

Agen lain cukup diberi symlink ke hasil clone yang sama:

```bash
ln -s ~/.claude/skills/menulis-indonesia-baku ~/.agents/skills/menulis-indonesia-baku   # Codex
ln -s ~/.claude/skills/menulis-indonesia-baku ~/.factory/skills/menulis-indonesia-baku  # Factory Droid
ln -s ~/.claude/skills/menulis-indonesia-baku ~/.grok/skills/menulis-indonesia-baku     # Grok CLI
```

Skill aktif otomatis saat agen menulis atau menyunting teks bahasa Indonesia. Di Claude Code, skill ini juga bisa dipanggil dengan `/menulis-indonesia-baku`.

## Memeriksa kata ke KBBI

```console
$ python3 cek_kbbi.py merubah mengakomodir analisis
merubah: TIDAK BAKU → mengubah
mengakomodir: ADA [CAKAPAN]: v cak mengakomodasi
analisis: ADA: n penyelidikan terhadap suatu peristiwa (karangan, perbuatan, dan sebagainya) ...
```

Perintah `python3 cek_kbbi.py --uji` menjalankan uji cepat. Pemeriksa ini mengambil halaman KBBI satu per satu dengan jeda, jadi gunakan secukupnya.

## Gaya pribadi

Aturan gaya Anda sendiri, misalnya istilah yang tidak boleh diterjemahkan, bisa ditulis di berkas `gaya-pribadi.md` di folder skill. Agen membacanya sebelum menulis, dan aturannya menang bila berbeda dengan kaidah resmi. Berkas itu tercantum di `.gitignore` sehingga tidak ikut ter-*push*.

## Lisensi

[MIT](LICENSE)
