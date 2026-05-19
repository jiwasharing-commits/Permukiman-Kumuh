#!/usr/bin/env python3
import csv
from pathlib import Path

SRC = Path('data/sumber_data_baru.csv')
EXPECTED_FIELDS = ['RT/RW', 'KAMPUNG', 'DESA', 'KECAMATAN', 'LUAS (Ha)', 'KEWENANGAN', 'Bobot Kumuh']
KEY_FIELDS = EXPECTED_FIELDS

with SRC.open(newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

headers = reader.fieldnames or []
if headers != EXPECTED_FIELDS:
    raise SystemExit(f'ERROR: header CSV tidak sesuai. Ditemukan={headers!r}; diharapkan={EXPECTED_FIELDS!r}')

seen, duplicates = set(), 0
for row in rows:
    key = tuple((row.get(field) or '').strip() for field in KEY_FIELDS)
    if key in seen:
        duplicates += 1
    else:
        seen.add(key)

print(f'source={SRC}')
print(f'source_rows={len(rows)}')
print(f'unique_rows={len(seen)}')
print(f'duplicates_found={duplicates}')
if len(seen) != 602:
    print('WARNING: unique_rows is not 602; please verify the source data completeness.')
