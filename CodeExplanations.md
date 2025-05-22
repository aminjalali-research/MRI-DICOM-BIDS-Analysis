
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



Based on the files you've provided, it seems like `dcm2niix` has already been run, converting the DICOM (`.IMA`) files to NIfTI (`.nii`) and extracting header information into JSON (`.json`) sidecar files. This is helpful as we can analyze the JSON files directly.

Here's the plan:

1. __Analyze JSON Headers:__ I will read the content of the provided JSON files to extract key information like `SeriesDescription`, `ProtocolName`, `ImageType`, and other relevant fields to understand each scan type.
2. __Identify Normalized Scans:__ I will specifically check the `ImageType` field within the JSON files (particularly for T1w and FLAIR scans as requested, but also others) for tags like "NORM", "NORMALIZED", or similar indicators of normalization.
3. __Summarize Findings:__ I'll present a summary of the different scan types found and their characteristics based on the header information.
4. __Propose BIDS Mapping:__ Based on the analysis, I will suggest a mapping of these scans to the appropriate BIDS data types (anat, func, dwi, fmap, perf) and propose a naming convention.
5. __Discuss Next Steps:__ We can then discuss the proposed mapping and decide on the next steps, such as creating a configuration file for BIDS conversion.




need to modify the crushed top of the skull
