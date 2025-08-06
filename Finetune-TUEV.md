# Database: TUH EEG Event Corpus

Dataset contains events including periodic lateralized epileptiform discharge, generalized periodic epileptiform discharge, spike and/or sharp wave discharges, artifact, and eye movement.

## File Naming Convention

**Example:** `00002275_00000001.edf`
- `00002275`: Reference to the train index
- `00000001`: Indicates this is the first file associated with this patient
- `.edf`: The actual EDF file containing EEG data

## File Types

There are six types of files in this release:

| Extension | Description |
|-----------|-------------|
| `*.edf` | EEG sampled data in European Data Format (EDF) |
| `*.htk` | Feature extraction based on "Improved EEG Event Classification Using Differential Energy" |
| `*.lab` | Annotation file with labels for every 10 microseconds, named by channel number |
| `*.rec` | Annotation file with labels given in seconds |

## Label Codes

### Lab Files (4-letter codes)

| Code | Description |
|------|-------------|
| `spsw` | Spike and slow wave |
| `gped` | Generalized periodic epileptiform discharge |
| `pled` | Periodic lateralized epileptiform discharge |
| `eyem` | Eye movement |
| `artf` | Artifact |
| `bckg` | Background |

**Format:** `117100000 117200000 eyem`
- Fields: start time, stop time (in 10s of microseconds), label

### Rec Files (numeric codes)

| Code | Description |
|------|-------------|
| 1 | spsw (spike and slow wave) |
| 2 | gped (generalized periodic epileptiform discharge) |
| 3 | pled (periodic lateralized epileptiform discharge) |
| 4 | eyem (eye movement) |
| 5 | artf (artifact) |
| 6 | bckg (background) |

**Format:** `13,90.4,91.4,6`
- Fields: channel number, start time (seconds), stop time (seconds), label

## Channel Montage (ACNS TCP)

The channel numbers in `.rec` and `.lab` files refer to channels defined using a standard ACNS TCP montage:

| Channel | Name | Definition |
|---------|------|------------|
| 0 | FP1-F7 | EEG FP1-REF -- EEG F7-REF |
| 1 | F7-T3 | EEG F7-REF -- EEG T3-REF |
| 2 | T3-T5 | EEG T3-REF -- EEG T5-REF |
| 3 | T5-O1 | EEG T5-REF -- EEG O1-REF |
| 4 | FP2-F8 | EEG FP2-REF -- EEG F8-REF |
| 5 | F8-T4 | EEG F8-REF -- EEG T4-REF |
| 6 | T4-T6 | EEG T4-REF -- EEG T6-REF |
| 7 | T6-O2 | EEG T6-REF -- EEG O2-REF |
| 8 | A1-T3 | EEG A1-REF -- EEG T3-REF |
| 9 | T3-C3 | EEG T3-REF -- EEG C3-REF |
| 10 | C3-CZ | EEG C3-REF -- EEG CZ-REF |
| 11 | CZ-C4 | EEG CZ-REF -- EEG C4-REF |
| 12 | C4-T4 | EEG C4-REF -- EEG T4-REF |
| 13 | T4-A2 | EEG T4-REF -- EEG A2-REF |
| 14 | FP1-F3 | EEG FP1-REF -- EEG F3-REF |
| 15 | F3-C3 | EEG F3-REF -- EEG C3-REF |
| 16 | C3-P3 | EEG C3-REF -- EEG P3-REF |
| 17 | P3-O1 | EEG P3-REF -- EEG O1-REF |
| 18 | FP2-F4 | EEG FP2-REF -- EEG F4-REF |
| 19 | F4-C4 | EEG F4-REF -- EEG C4-REF |
| 20 | C4-P4 | EEG C4-REF -- EEG P4-REF |
| 21 | P4-O2 | EEG P4-REF -- EEG O2-REF |

> **Note:** Channel 1 represents the difference between electrodes F7 and T3, calculated as (F7-REF)-(T3-REF), where both channels are contained in the EDF file.

## Dataset Statistics

### Evaluation Set
- **Total files:** 159
  - containing `spsw`: 9
  - containing `gped`: 28
  - containing `pled`: 33
  - containing `artf`: 46
  - containing `eyem`: 35
  - containing `bckg`: 89

### Training Set
- **Total files:** 359
  - containing `spsw`: 27
  - containing `gped`: 51
  - containing `pled`: 48
  - containing `artf`: 164
  - containing `eyem`: 46
  - containing `bckg`: 211
 
# Other Datasets:
- TUEP (Epilepsy classification - binary), TUSZ (Seizure type classification - multiclass)
- CHB-MIT (Peadiatric seizure detection - binary): Population 23
- MAYO (Seizure detection and multi-class classification): Population 39
- FNUSA (Seizure detection and multi-class classification)
- SeizIt1: population 14

# Cuda mismatch
I installed Driver Version: 575.64.05 and CUDA Version: 12.9 (this is compatible with your RTX 5070 Ti!), and for the conda environment pytorch-cuda=11.8:
- conda remove pytorch torchvision torchaudio pytorch-cuda
- conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia


# LaBraM Fine-tuning Results on TUEV Dataset
- Model: LaBraM Base (labram_base_patch200_200)
- Task: 6-class EEG event classification
- Parameters: 5.82M trainable parameters

## Training Results

| Epoch | Train Loss | Train Acc | Val Acc | Test Acc | Val F1 | Test F1 | Cohen's κ |
|-------|------------|-----------|---------|----------|--------|---------|-----------|
| 0     | 1.065      | 76.3%     | 77.3%   | 81.9%    | 78.1%  | 81.8%   | 0.632     |
| 1     | 0.557      | 94.4%     | 80.7%   | 79.9%    | 81.6%  | 81.1%   | 0.693     |
| 2     | 0.502      | 96.7%     | 73.1%   | 79.0%    | 73.0%  | 79.9%   | 0.580     |
| 3     | 0.488      | 97.3%     | 78.1%   | 77.2%    | 79.3%  | 78.8%   | 0.660     |
| 4     | 0.481      | 97.6%     | 72.5%   | 81.2%    | 71.2%  | 81.9%   | 0.567     |
| **5** | **0.472**  | **98.0%** | **83.3%** | **81.9%** | **83.9%** | **82.5%** | **0.734** |
| 6     | 0.467      | 98.2%     | 74.6%   | 80.8%    | 75.7%  | 81.7%   | 0.605     |

## Training Configuration
- Batch Size: 64
- Learning Rate: 5e-4
- Weight Decay: 0.05
- Warmup Epochs: 5
- Total Epochs: 50 
- Layer Decay: 0.65
- Drop Path: 0.1
