## DICOM Header Analysis and BIDS Preparation

1. **Identify Key DICOM Tags**  
   - **SeriesDescription** (`(0008,103E)`)  
   - **Modality** (`(0008,0060)`)  
   - **ImageType** (`(0008,0008)`)  
   - **ProtocolName** (`(0018,1030)`) or **SequenceName** (`(0018,0024)`)  
   - **SeriesInstanceUID** (`(0020,000E)`)

2. **Filter for “Normalized” Scans**  
   Look for strings like `NORM`, `Norm`, `NormImage`, or `Normalized` in:  
   - **ImageType** entries  
   - **SeriesDescription**  

3. **Define a Mapping from DICOM Series → BIDS Entities**  
   ```yaml
   anatomical:
     T1w      <- SeriesDescription contains "T1w"  & ImageType includes "NORM"
     T2w      <- SeriesDescription contains "T2w"
     FLAIR    <- SeriesDescription contains "FLAIR"
   func:
     sentence <- SeriesDescription contains "Sentence Completion"
     wordgen  <- SeriesDescription contains "Word Generation"
   dwi:
     dMRI     <- ProtocolName or SeriesDescription contains "dMRI"
   fmap:
     fieldmap <- SeriesDescription contains "SpinEchoFieldMap"
   asl:
     pcASL    <- SeriesDescription contains "PCASL" or "mbPCASL"
   ```

4. **Use a BIDS-Aware Conversion Tool**
dcm2niix to convert DICOM → NIfTI
heudiconv, dcm2bids, or a custom heuristic script to organize into BIDS


## Next Steps
- Review the Generated CSV to verify that each series has the correct label.

- Run dcm2niix on each folder listed in the CSV to create NIfTI files.

- Execute a BIDS converter (e.g., heudiconv --files dicom_summary.csv --heuristic my_heuristic.py …) to assemble the final BIDS directory structure.
