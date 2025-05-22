
"SeriesDescription": "FLAIR_TRA",
"ProtocolName": "32_FLAIR_1mm_ipat2",
ImageType": ["DERIVED", "SECONDARY", "MPR", "CSA MPR", "CSAPARALLEL", "M", "ND", "NORM", "FM", "FIL"],	
"RawImage": false,

"SeriesDescription": "32_FLAIR_1mm_ipat2_ORIG",
"ProtocolName": "32_FLAIR_1mm_ipat2",
"ImageType": ["ORIGINAL", "PRIMARY", "M", "ND", "NORM"],

"SeriesDescription": "AAHScout_MPR_sag",
"ProtocolName": "AAHScout",
"ImageType": ["DERIVED", "PRIMARY", "MPR", "ND", "NORM"],
"RawImage": false,


can you tell me the series numbers whose "ImageType" contains "DERIVED" information or the "RawImage" is "false"?
Can you use SpinEchoFieldMap files to correct the MRI images? create a separate python file?
i would like to push all the files in the /src folder into the github repository. I do not want to push the data.

analyze the DICOM header information (extracted into the provided JSON files) from the Patient/ directory to understand the different MRI modalities present, identify normalized scans (especially T1w and FLAIR), and determine how to categorize these scans according to the BIDS standard.

I need the complete code of converting DICOMs (.IMA) to NIfTI(.nii) and extracting header infromation into JSON(.json) sidecar files. Then to BIDS either using dcm2niix or other methods in jupyter notebook with .ipython file.

Here's the plan:

1. __Analyze JSON Headers:__ I will read the content of the provided JSON files to extract key information like `SeriesDescription`, `ProtocolName`, `ImageType`, "RawImage", and other relevant fields to understand each scan type. We check the Series of each modality, if the "ImageType" contains ["DERIVED", "SECONDARY"] then we only convert that series. otherwise we check if ["DERIVED", "PRIMARY"] is avaiable. If not we convert the ["ORIGINAL"] series. Therefore, we intend to convert only the last "DERIVED" series of each modality and not all of them. 
2. __Summarize Findings:__ I'll present a summary of the different scan types found and their characteristics based on the header information.
3. __Propose BIDS Mapping:__ Based on the analysis, I will suggest a mapping of these scans to the appropriate BIDS data types (anat, func, dwi, fmap, perf) and propose a naming convention.





need to modify the crushed top of the skull
