import os

INPUT = "NARA_FULL_DUMP.txt"
OUT_DIR = "dump_parts"
CHUNK_SIZE = 40000  # 20 KB safe

os.makedirs(OUT_DIR, exist_ok=True)

with open(INPUT, "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

parts = [data[i:i+CHUNK_SIZE] for i in range(0, len(data), CHUNK_SIZE)]

for idx, part in enumerate(parts, 1):
    path = os.path.join(OUT_DIR, f"part_{idx:02d}.txt")
    with open(path, "w", encoding="utf-8") as out:
        out.write(part)

print(f"Done: {len(parts)} parts written to {OUT_DIR}/")
