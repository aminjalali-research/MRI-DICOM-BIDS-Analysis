# MRI DICOM and BIDS data analyses 


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
The numbers are not correct all the time. The last one is one we aim to use for any reason they had to abort. 
# MRI Data Description

## 1. Structural (Anatomical) Scans

These scans provide detailed views of brain anatomy and serve as reference images for aligning other modalities.

### 🔹 T1-weighted (T1w)
High-resolution structural scan showing fine anatomical detail; good gray/white matter contrast.
### 🔹 T2-weighted (T2w)
Complementary to T1w; CSF appears bright. Useful for edema or pathology.
### 🔹 High-Resolution T2w (Hippocampus)
TSE_HiResHp: High-resolution scan of the hippocampal region; critical in epilepsy/neurodegeneration.
### 🔹 FLAIR (Fluid-Attenuated Inversion Recovery)
FLAIR_1mm_ipat2_ORIG: Suppresses CSF signal, highlighting white matter lesions.


## 2. Functional MRI (fMRI)
These scans capture brain activity during language tasks.

### 🔹 Sentence Completion Task or Word Generation Task
- SBRef: Single-volume structural reference for motion correction.
- Sentence_Completion: BOLD time-series (~100 volumes) during language task.
- PhysioLog: Simultaneous physiological data (heart rate, respiration).

### 🔹 Fieldmaps for fMRI
- SpinEchoFieldMap_AP and SpinEchoFieldMap_PA: Used to correct spatial distortions due to magnetic susceptibility in fMRI images.

## 3. Diffusion MRI (dMRI)
Used to visualize white matter microstructure and perform tractography.

### 🔹 AP Phase Encoding
- dMRI_dir98_AP_SBref: Structural reference volume.
- dMRI_dir98_AP:** Main diffusion scan (~99 directions).
- PhysioLog: Auxiliary, not typically required.

### 🔹 PA Phase Encoding
- dMRI_dir99_PA:** Reverse phase-encoded diffusion scan.

## 4. Perfusion Imaging (ASL - Arterial Spin Labeling)
Provides measurements of cerebral blood flow (CBF).

- mbPCASLhr_PA:** Pseudocontinuous ASL sequence including M0 image. (Main ASL Sequence)
- Fieldmaps for ASL: SpinEchoFieldMap_AP and SpinEchoFieldMap_PA

## 5. Localizer
- Low-resolution scan used only for planning. Not used in analysis.


## 🗂 Summary Table

| **Modality**       | **Purpose**                                 | 
|--------------------|---------------------------------------------|
| T1w, T2w, FLAIR    | Structural anatomy, lesion visualization    |
| fMRI (Language)    | Brain activation during language tasks      | 
| Diffusion (dMRI)   | White matter connectivity (tractography)    | 
| ASL                | Cerebral perfusion (blood flow)             | 
| Localizers         | Positioning only                            |

