# DICOM-BIDS Analysis
Comprehensive MRI DICOM and BIDS data analyses 


## 📂 MRI Data Overview

```text
MRI Data
├── 1. Structural (Anatomical) Scans
│   ├── T1-weighted (T1w)
│   │   ├── (2 - T1w_MPR): Initial T1w scan
│   │   └── 3 - T1w_MPR: Normalized, convert
│   ├── T2-weighted (T2w)
│   │   ├── (4 - T2w_SPC): Initial T2w scan
│   │   └── 5 - T2w_SPC: Normalized, convert
│   ├── High-Resolution T2w for Hippocampus
│   │   ├── (6 - TSE_HiResHp): Raw HiRes scan
│   │   └── 7 - TSE_HiResHp: Normalized, convert
│   └── FLAIR (Fluid-Attenuated Inversion Recovery)
│       ├── (27 - 32_FLAIR_1mm_ipat2_ORIG): Raw series
│       └── 28 - 32_FLAIR_1mm_ipat2: Normalized, convert
│
├── 2. Functional MRI (fMRI)
│   ├── Language Task: Sentence Completion
│   │   ├── (8 - Sentence_Completion_SBRef): Structural reference for motion correction
│   │   └── 9 - Sentence_Completion, convert (~100 volumes)
│   │   └── (10 - PhysioLog): Physiological recording
│   ├── Language Task: Word Generation
│   │   ├── (11,13 - Word Generation): Auxiliary
│   │   └── 12 - Word_Generation:convert
│   └── Fieldmaps (for fMRI distortion correction)
│       ├── 14 - SpinEchoFieldMap_AP
│       └── 15 - SpinEchoFieldMap_PA
│
├── 3. Diffusion MRI (dMRI)
│   ├── Phase Encoding Direction: AP
│   │   ├── (16 - dMRI_dir98_AP_SBref): Structural reference
│   │   └── 17 - dMRI_dir98_AP: convert (~99 volumes)
│   │   └── (18 - PhysioLog): Not required
│   ├── Phase Encoding Direction: PA
│   │   ├── (19,21 - Others): Auxiliary
│   │   └── 20 - dMRI_dir99_PA: convert (~100 volumes)
│   └── (22-26 - Processed): Skip
│
├── 4. Perfusion (ASL)
│   ├── (29-33 - Localizer): Not required
│   ├── 34 - mbPCASLhr_PA: Main ASL sequence (includes M0 image)
│   └── Fieldmaps (for ASL distortion correction)
│       ├── 35 - SpinEchoFieldMap_AP
│       └── 36 - SpinEchoFieldMap_PA
│
└── (1 - Localizer): Planning scan, not required
```

# 🧠 MRI Data Structure and Description

This document provides an intuitive and professional overview of MRI scans extracted from a clinical imaging session. Each modality is described in terms of its role and typical files associated with it.

---

## 1. Structural (Anatomical) Scans

These scans provide detailed views of brain anatomy and serve as reference images for aligning other modalities.

### 🔹 T1-weighted (T1w)
- **2 - T1w_MPR:** High-resolution structural scan showing fine anatomical detail; good gray/white matter contrast.
- **3 - T1w_MPR (Normalized):** Standard-space version of the T1w scan for group analysis and atlas integration.

### 🔹 T2-weighted (T2w)
- **4 - T2w_SPC:** Complementary to T1w; CSF appears bright. Useful for edema or pathology.
- **5 - T2w_SPC (Normalized):** Aligned or normalized version of T2w.

### 🔹 High-Resolution T2w (Hippocampus)
- **6 - TSE_HiResHp:** High-resolution scan of the hippocampal region; critical in epilepsy/neurodegeneration.
- **7 - TSE_HiResHp (Normalized):** Aligned version for analysis.

### 🔹 FLAIR (Fluid-Attenuated Inversion Recovery)
- **27 - 32_FLAIR_1mm_ipat2_ORIG:** Suppresses CSF signal, highlighting white matter lesions.
- **28 - 32_FLAIR_1mm_ipat2 (Normalized):** Preprocessed version for structural comparisons.

---

## 2. Functional MRI (fMRI)

These scans capture brain activity during language tasks.

### 🔹 Sentence Completion Task
- **8 - SBRef:** Single-volume structural reference for motion correction.
- **9 - Sentence_Completion:** BOLD time-series (~100 volumes) during language task.
- **10 - PhysioLog:** Simultaneous physiological data (heart rate, respiration).

### 🔹 Word Generation Task
- **11, 13 - Word Generation:** Auxiliary task files.
- **12 - Word_Generation:** Functional scan used in activation analysis.

### 🔹 Fieldmaps for fMRI
- **14 - SpinEchoFieldMap_AP**
- **15 - SpinEchoFieldMap_PA**

> Used to correct spatial distortions due to magnetic susceptibility in fMRI images.

---

## 3. Diffusion MRI (dMRI)

Used to visualize white matter microstructure and perform tractography.

### 🔹 AP Phase Encoding
- **16 - dMRI_dir98_AP_SBref:** Structural reference volume.
- **17 - dMRI_dir98_AP:** Main diffusion scan (~99 directions).
- **18 - PhysioLog:** Auxiliary, not typically required.

### 🔹 PA Phase Encoding
- **19, 21 - Others:** Auxiliary scans.
- **20 - dMRI_dir99_PA:** Reverse phase-encoded diffusion scan.

### 🔹 Processed Data
- **22–26:** Already processed—can be skipped.

---

## 4. Perfusion Imaging (ASL - Arterial Spin Labeling)

Provides measurements of cerebral blood flow (CBF).

### 🔹 Main ASL Sequence
- **34 - mbPCASLhr_PA:** Pseudocontinuous ASL sequence including M0 image.

### 🔹 Fieldmaps for ASL
- **35 - SpinEchoFieldMap_AP**
- **36 - SpinEchoFieldMap_PA**

### 🔹 Localizers
- **29–33:** Planning scans—can be ignored in analysis.

---

## 5. Localizer
- **1 - Localizer:** Low-resolution scan used only for planning. Not used in analysis.

---

## 🗂 Summary Table

| **Modality**       | **Purpose**                                | **Key Files**                         |
|--------------------|---------------------------------------------|---------------------------------------|
| T1w, T2w, FLAIR    | Structural anatomy, lesion visualization    | 2, 3, 4, 5, 6, 7, 27, 28              |
| fMRI (Language)    | Brain activation during language tasks      | 8, 9, 10, 11, 12, 13, 14, 15          |
| Diffusion (dMRI)   | White matter connectivity (tractography)    | 16–21                                 |
| ASL                | Cerebral perfusion (blood flow)             | 34, 35, 36                            |
| Localizers         | Positioning only                            | 1, 29–33                              |

---

> 🧭 *Note*: Normalization typically refers to alignment to a standard template (e.g., MNI) for group-level analysis.

