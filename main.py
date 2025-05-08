import os
import csv
import re
import pydicom
from collections import defaultdict

# 1. Define your BIDS mapping rules as (regex, BIDS_label) tuples:
MAPPING_RULES = [
    (re.compile(r"T1w.*", re.IGNORECASE),        "anat/T1w"),
    (re.compile(r"T2w.*", re.IGNORECASE),        "anat/T2w"),
    (re.compile(r"FLAIR.*", re.IGNORECASE),      "anat/FLAIR"),
    (re.compile(r"Sentence\s*Completion", re.IGNORECASE), "func/sentence"),
    (re.compile(r"Word\s*Generation", re.IGNORECASE),     "func/wordgen"),
    (re.compile(r"SpinEchoFieldMap", re.IGNORECASE),      "fmap/epi"),
    (re.compile(r"dMRI", re.IGNORECASE),                "dwi/dMRI"),
    (re.compile(r"(PCASL|mbPCASL)", re.IGNORECASE),      "asl/PCASL"),
    # … add more rules as needed …
]

# 2. Function to decide if a series is "normalized"
def is_normalized(ds: pydicom.Dataset) -> bool:
    img_type = ds.get("ImageType", [])
    desc     = ds.get("SeriesDescription", "")
    return any("NORM" in t.upper() for t in img_type) or \
           bool(re.search(r"Norm|Normalized", desc, re.IGNORECASE))

def categorize(series_desc: str):
    for pattern, label in MAPPING_RULES:
        if pattern.search(series_desc):
            return label
    return "unknown"

def scan_dicom_folder(root_dir):
    # group by SeriesInstanceUID so we inspect one file per series
    series_map = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            full = os.path.join(dirpath, fname)
            try:
                ds = pydicom.dcmread(full, stop_before_pixels=True)
            except Exception:
                continue
            uid = ds.SeriesInstanceUID
            # keep the first file we see for each series
            if uid not in series_map:
                series_map[uid] = {
                    "path": dirpath,
                    "desc": ds.SeriesDescription or "",
                    "mod":  ds.Modality or "",
                    "norm": is_normalized(ds)
                }
    return series_map

def write_summary_csv(series_map, out_csv="dicom_summary.csv"):
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["SeriesInstanceUID","Path","Description","Modality","Normalized","BIDS_label"])
        w.writeheader()
        for uid, info in series_map.items():
            label = categorize(info["desc"])
            # optionally skip non-normalized T1w:
            if "T1w" in info["desc"] and not info["norm"]:
                continue
            w.writerow({
                "SeriesInstanceUID": uid,
                "Path":               info["path"],
                "Description":        info["desc"],
                "Modality":           info["mod"],
                "Normalized":         info["norm"],
                "BIDS_label":         label
            })
    print(f"Wrote summary to {out_csv}")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("dicom_root", help="Root folder containing DICOMs")
    p.add_argument("--out", default="dicom_summary.csv", help="Output CSV file")
    args = p.parse_args()

    series = scan_dicom_folder(args.dicom_root)
    write_summary_csv(series, args.out)
