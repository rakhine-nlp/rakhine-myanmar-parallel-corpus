{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import csv\
\
# -------------------------\
# FILE PATHS\
# -------------------------\
rakhine_file = "raw_data/rakhine_text.txt"\
myanmar_file = "raw_data/myanmar_text.txt"\
\
output_file = "data/train.csv"\
\
\
# -------------------------\
# READ FILES\
# -------------------------\
with open(rakhine_file, "r", encoding="utf-8") as f:\
    rakhine_lines = [line.strip() for line in f if line.strip()]\
\
with open(myanmar_file, "r", encoding="utf-8") as f:\
    myanmar_lines = [line.strip() for line in f if line.strip()]\
\
\
# -------------------------\
# ALIGN SENTENCES\
# -------------------------\
pairs = []\
\
min_len = min(len(rakhine_lines), len(myanmar_lines))\
\
for i in range(min_len):\
    r = rakhine_lines[i]\
    m = myanmar_lines[i]\
\
    pairs.append([r, m])\
\
\
# -------------------------\
# WRITE CSV OUTPUT\
# -------------------------\
with open(output_file, "w", encoding="utf-8", newline="") as f:\
    writer = csv.writer(f)\
\
    # header\
    writer.writerow(["rakhine", "myanmar"])\
\
    # data rows\
    for r, m in pairs:\
        writer.writerow([r, m])\
\
print(f"Done! Created \{output_file\} with \{len(pairs)\} sentence pairs.")}