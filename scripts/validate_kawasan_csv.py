#!/usr/bin/env python3
import csv
from pathlib import Path

SRC = Path('data/lokasi_kewenangan_kabupaten.csv')
OUT = Path('data/lokasi_kewenangan_kabupaten.cleaned.csv')
KEY_FIELDS = ['rt_rw','kampung','desa','kecamatan','luas_ha','kewenangan','bobot_kumuh']

with SRC.open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

cleaned, seen = [], set()
for r in rows:
    norm = {k:(r.get(k,'').strip()) for k in KEY_FIELDS}
    key = tuple(norm[k] for k in KEY_FIELDS)
    if key in seen:
        continue
    seen.add(key)
    cleaned.append(norm)

with OUT.open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=KEY_FIELDS)
    w.writeheader(); w.writerows(cleaned)

print(f'source_rows={len(rows)}')
print(f'unique_rows={len(cleaned)}')
print(f'duplicates_removed={len(rows)-len(cleaned)}')
print(f'output={OUT}')
if len(cleaned) != 602:
    print('WARNING: unique_rows is not 602; please provide full source file if truncated.')
