#!/usr/bin/env python3
# tinh-dong-thuan.py — Tính % đồng thuận giữa 2 người chấm từ file CSV.
#
# Cách dùng:
#   python tinh-dong-thuan.py diem-cham.csv
#
# File CSV cần có 2 cột: nguoi_1, nguoi_2 (điểm mỗi dòng).
# File mẫu: diem-cham-mau.csv

import csv
import sys


def main(path):
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows or "nguoi_1" not in rows[0] or "nguoi_2" not in rows[0]:
        print("CSV cần có 2 cột: nguoi_1, nguoi_2")
        return
    tong = len(rows)
    trung = sum(1 for r in rows if r["nguoi_1"].strip() == r["nguoi_2"].strip())
    print(f"Tổng mẫu: {tong}")
    print(f"Trùng nhau: {trung}")
    print(f"% đồng thuận: {trung / tong * 100:.1f}%")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python tinh-dong-thuan.py diem-cham.csv")
    else:
        main(sys.argv[1])
