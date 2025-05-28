# MRI DICOM Analysis & BIDS Conversion Pipeline

This repository contains scripts and documentation for processing MRI DICOM data, extracting metadata, and converting it into [BIDS (Brain Imaging Data Structure)](https://bids.neuroimaging.io/) format using `dcm2niix` and `dcm2bids`.

---

## 📁 Project Structure

```bash
MRIProjects/
├── data/                  # Input directory containing raw DICOM files
├── output/                # Output directory for NIfTI and JSON files from dcm2niix
├── scripts/
│   └── convert_dicom.py   # Main script for conversion and metadata analysis
└── dcm2bids_config.json   # Configuration for BIDS conversion
```

# Overview
🎯 Objective
- Convert raw MRI DICOM files to NIfTI format.
- Extract and analyze DICOM header metadata (from JSON sidecars).
- Select representative scans using a priority-based strategy.
- Prepare the dataset for BIDS conversion using dcm2bids.

🧠 Modalities Processed
- Structural (T1w, T2w, FLAIR, HiRes hippocampus)
- Functional MRI (fMRI) with task and fieldmaps
- Diffusion MRI (dMRI)
- Perfusion (ASL)

# 🔍 Metadata Selection Strategy
We follow a priority-based selection strategy for each scan type:

1. First, we select the last available series whose ImageType contains both "DERIVED" and "SECONDARY".
2. If not available, we choose a series containing "DERIVED" and "PRIMARY".
3. If neither are found, we fall back to the "ORIGINAL" + "PRIMARY" series.

This ensures we only convert high-quality, preprocessed scans (e.g., motion-corrected, normalized), avoiding partial or raw acquisitions.


# Usage
1. Convert DICOM to NIfTI + JSON
Run the provided Python script:

```bash
python scripts/convert_dicom.py
```
This will:
- Recursively search for .dcm or .IMA files in ~/MRIProjects/data/.
- Convert DICOM files using dcm2niix.
- Save NIfTI (.nii.gz) and metadata (.json) in ~/MRIProjects/output/.

2. Inspect Derived Headers
Automatically filters and displays all series marked with "DERIVED" in the ImageType field.

3. Priority-Based Selection
The script groups series by SeriesDescription and ProtocolName, then applies the selection strategy. The output is displayed in an interactive table.

# BIDS Conversion
After generating dcm2bids_config.json, run:
```bash
dcm2bids -d ~/MRIProjects/data/ -p P001 -s 01 -c dcm2bids_config.json -o bids_output --clobber --force_dcm2bids
```

# 📊 Example Output
| SeriesNumber | SeriesDescription    | ProtocolName   | ImageType                         |
| ------------ | -------------------- | -------------- | --------------------------------- |
| 3            | T1w\_MPR             | T1w\_MPR       | DERIVED, SECONDARY, MPR, ND, NORM |
| 9            | Sentence\_Completion | fMRI\_Language | DERIVED, SECONDARY, NORM, FM      |
| 34           | mbPCASLhr\_PA        | ASL\_Perfusion | DERIVED, SECONDARY, MPR, ND, NORM |

# Requirements
- Python 3.8+
- dcm2niix (install via conda or system package manager)
- pandas
- dcm2bids (for final BIDS conversion)

