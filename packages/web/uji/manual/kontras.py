#!/usr/bin/env python3
"""Analisis kontras terender dari pasangan tangkapan A (utuh) dan B (kelompok disembunyikan), keluaran `kontras.mjs`.
Pemakaian: kontras.py <awalan-berkas-tanpa-.json> ...   (butuh numpy dan Pillow)
Metode: rasio luminans WCAG 2.x antara piksel A dan piksel B di posisi yang sama (komposit alfa sudah
terjadi di peramban). Glif: per komponen terhubung, ambil piksel dengan rasio tertinggi (puncak). Garis: p90 rasio
piksel per komponen. Teks: puncak per elemen."""
import json, sys
from collections import deque
import numpy as np
from PIL import Image


def lum(a):
    c = a.astype(np.float64) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def rasio(l1, l2):
    hi = np.maximum(l1, l2)
    lo = np.minimum(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def komponen(mask):
    ys, xs = np.nonzero(mask)
    sisa = set(zip(ys.tolist(), xs.tolist()))
    hasil = []
    while sisa:
        s = sisa.pop()
        q = deque([s])
        piks = [s]
        while q:
            y, x = q.popleft()
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    n = (y + dy, x + dx)
                    if n in sisa:
                        sisa.discard(n)
                        q.append(n)
                        piks.append(n)
        hasil.append(piks)
    return hasil


def pct(v, p):
    return float(np.percentile(v, p)) if len(v) else float("nan")


def analisa(awalan):
    meta = json.load(open(awalan + ".json"))
    out = {"usul": meta["usul"], "port": meta["port"], "tema": meta["tema"], "w": meta["w"], "kel": {}}
    for l in meta["lintasan"]:
        A = np.array(Image.open(f"{awalan}-{l['nama']}-A.png").convert("RGB"))
        B = np.array(Image.open(f"{awalan}-{l['nama']}-B.png").convert("RGB"))
        if A.shape != B.shape:
            out["kel"][l["nama"]] = {"galat": "ukuran A dan B beda"}
            continue
        LA, LB = lum(A), lum(B)
        R = rasio(LA, LB)
        d = np.abs(A.astype(int) - B.astype(int)).max(axis=2)
        if l["tipe"] == "teks":
            res = []
            for r in l["rects"] or []:
                x0, y0 = max(int(r["x"]) - 1, 0), max(int(r["y"]) - 1, 0)
                x1, y1 = min(int(r["x"] + r["w"]) + 2, A.shape[1]), min(int(r["y"] + r["h"]) + 2, A.shape[0])
                reg = R[y0:y1, x0:x1]
                dm = d[y0:y1, x0:x1] >= 8
                if dm.sum() == 0:
                    continue
                res.append({"puncak": float(reg[dm].max()), "p90": float(np.percentile(reg[dm], 90)), "fs": r["fs"] * r.get("sc", 1), "h": r["h"], "t": r["t"], "fw": r["fw"]})
            pk = np.array([x["puncak"] for x in res])
            fsz = np.array([x["fs"] for x in res])
            out["kel"][l["nama"]] = {
                "tipe": "teks", "n": len(res), "puncak_min": float(pk.min()) if len(pk) else None,
                "puncak_med": pct(pk, 50), "puncak_p10": pct(pk, 10), "fs_min": float(fsz.min()) if len(fsz) else None,
                "fs_med": pct(fsz, 50), "contoh_min": min(res, key=lambda x: x["puncak"])["t"] if res else None,
            }
            continue
        mask = d >= 8
        comps = komponen(mask)
        comps = [c for c in comps if len(c) >= int(__import__("os").environ.get("MIN_PIKS", "2"))]
        if l["tipe"] == "glif":
            vals = np.array([max(R[y, x] for y, x in c) for c in comps])
            tinggi = np.array([max(y for y, x in c) - min(y for y, x in c) + 1 for c in comps])
            lebar = np.array([max(x for y, x in c) - min(x for y, x in c) + 1 for c in comps])
            out["kel"][l["nama"]] = {
                "tipe": "glif", "n": len(comps), "puncak_med": pct(vals, 50), "puncak_p10": pct(vals, 10), "puncak_p5": pct(vals, 5), "puncak_min": float(vals.min()) if len(vals) else None,
                "bawah3": int((vals < 3).sum()), "diam_med": pct(np.maximum(tinggi, lebar), 50),
            }
        else:  # garis
            vals = np.array([np.percentile([R[y, x] for y, x in c], 90) for c in comps if len(c) >= 6])
            out["kel"][l["nama"]] = {"tipe": "garis", "n": len(vals), "p90_med": pct(vals, 50), "p90_p10": pct(vals, 10), "p90_min": float(vals.min()) if len(vals) else None, "bawah3": int((vals < 3).sum())}
    return out


if __name__ == "__main__":
    semua = []
    for a in sys.argv[1:]:
        o = analisa(a)
        semua.append(o)
        print(f"== {o['usul']} port={o['port']} tema={o['tema']} w={o['w']}")
        for k, v in o["kel"].items():
            print("  ", k, json.dumps({kk: (round(vv, 2) if isinstance(vv, float) else vv) for kk, vv in v.items()}, ensure_ascii=False))
    import os; json.dump(semua, open(os.environ.get("OUTJ", "/tmp/langit-kontras-hasil.json"), "w"), ensure_ascii=False)
