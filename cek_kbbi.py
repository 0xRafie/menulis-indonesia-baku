"""Cek bentuk baku kata ke KBBI VI Daring (kbbi.kemendikdasmen.go.id).

Pemakaian: python3 cek_kbbi.py kata1 kata2 ...
Keluaran per kata: "TIDAK BAKU → X", "ADA [CAKAPAN]: makna" (ragam cakapan, hindari di tulisan resmi),
"ADA: makna", atau "TIDAK DITEMUKAN". Uji cepat: python3 cek_kbbi.py --uji
"""
import html
import re
import sys
import time
import urllib.request


def cek(kata, percobaan=2):
    url = f"https://kbbi.kemendikdasmen.go.id/entri/{kata}"
    for i in range(percobaan):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            s = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")
            break
        except Exception as e:  # jaringan lambat: coba sekali lagi
            if i == percobaan - 1:
                return f"GAGAL ({e})"
            time.sleep(2)
    if "tidak ditemukan" in s.lower():
        return "TIDAK DITEMUKAN"
    badan = s[s.find("<h2"):s.find("Pesan Redaksi")] if "<h2" in s else s
    teks = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", badan))).strip()
    rujukan = list(dict.fromkeys(re.findall(r"→\s*([\w\-]+)", teks)))
    # Entri tidak baku hanya berisi rujukan pendek ke bentuk baku.
    if rujukan and len(teks) < 200:
        return f"TIDAK BAKU → {', '.join(rujukan)}"
    # ponytail: label cak dicari lewat regex kelas kata; label ragam lain (kas, ark) belum ditandai
    cak = re.search(r"\b(?:n|v|a|adv|num|p|pron)\s+cak\b", teks)
    makna = teks.split("Tesaurus", 1)[-1].strip()[:140]
    return f"ADA{' [CAKAPAN]' if cak else ''}: {makna}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--uji":
        assert cek("merubah") == "TIDAK BAKU → mengubah"
        assert cek("mengakomodir").startswith("ADA [CAKAPAN]")
        assert cek("analisis").startswith("ADA: ")
        assert cek("asdfqwer") == "TIDAK DITEMUKAN"
        sys.exit("uji lolos")
    for kata in sys.argv[1:]:
        print(f"{kata}: {cek(kata)}")
        time.sleep(0.6)  # sopan terhadap server KBBI
