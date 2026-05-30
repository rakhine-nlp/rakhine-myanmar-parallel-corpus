import csv

# -------------------------
# FILE PATHS
# -------------------------
rakhine_file = "raw_data/rakhine_text.txt"
myanmar_file = "raw_data/myanmar_text.txt"

output_file = "data/train.csv"


# -------------------------
# READ FILES
# -------------------------
with open(rakhine_file, "r", encoding="utf-8") as f:
    rakhine_lines = [line.strip() for line in f if line.strip()]

with open(myanmar_file, "r", encoding="utf-8") as f:
    myanmar_lines = [line.strip() for line in f if line.strip()]


# -------------------------
# ALIGN SENTENCES
# -------------------------
pairs = []

min_len = min(len(rakhine_lines), len(myanmar_lines))

for i in range(min_len):
    r = rakhine_lines[i]
    m = myanmar_lines[i]

    pairs.append([r, m])


# -------------------------
# WRITE CSV OUTPUT
# -------------------------
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    # header
    writer.writerow(["rakhine", "myanmar"])

    # data rows
    for r, m in pairs:
        writer.writerow([r, m])

print(f"Done! Created {output_file} with {len(pairs)} sentence pairs.")
