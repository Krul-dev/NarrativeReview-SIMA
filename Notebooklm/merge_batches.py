import csv
from pathlib import Path

folder = Path(__file__).parent
files = sorted(folder.glob("Q1_bat*_??.csv"))

header = None
rows = []

for f in files:
    with open(f, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        file_header = next(reader)
        if header is None:
            header = file_header
        for row in reader:
            rows.append(row)

out = folder / "Q1_all_batches.csv"
with open(out, "w", newline="", encoding="utf-8") as fh:
    writer = csv.writer(fh)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Merged {len(files)} files -> {len(rows)} rows -> {out.name}")
