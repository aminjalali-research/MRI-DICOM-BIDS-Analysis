# EEG-EMU

1. Nicolet NicVue bought by Natus (short recordings). File types are:

- .e or .eeg – primary EEG data
- .erd – raw EEG binary (used by Neuroworks / Xltek systems)
- .ent – annotations/notes metadata
- .NPA – metadata wrapper used by NicVue

Can these files be read or anonymized? 
The .erd formats are compressed and proprietary, and there is no publicly documented Python library. Users convert to EDF via the Natus GUI instead.
- .erd can be read by unofficial code in Archived XltekDataReader (Python) [(Link)](https://github.com/nyuolab/XltekDataReader)


Natus provided a Platform Migration Utility to migrate data from legacy NicVue systems into a NeuroWorks database
[download.xltek.com](https://download.xltek.com/eeg/Software/Neuroworks/DOC-020491%20REV%2005%20-%20Platform%20Migration%20Utility%20User%20Guide.pdf#:~:text=from%20legacy%20source%20systems%20such,Database%20application%2C%20used%20with%20NeuroWorks). 

In research contexts, the usual approach is to export EEG recordings to EDF via NicVue/NeuroWorks itself, rather than parse .NPA in code. 
(Notably, the Temple University Hospital EEG Corpus was originally in Natus proprietary format and was converted to EDF using NicVue software
[par.nsf.gov](https://par.nsf.gov/servlets/purl/10199699#:~:text=,proprietary%20NicVue%20software%20tool).

------
Read EEG data from Natus Neuroworks systems:
```python
# Installation:
# pip install xltek-data-reader numpy

import os
import numpy as np
from xltek_data_reader import read_xltek_data

# Set the path to your Neuroworks EEG study folder
study_folder = '/path/to/natus_study_folder/'

# Read EEG data from Neuroworks files (.eeg, .erd, .ent)
eeg_data = read_xltek_data(study_folder)

# Access metadata
study_info = eeg_data['StudyInfo']
channel_names = eeg_data['ChannelNames']
annotations = eeg_data['Annotations']
eeg_signals = eeg_data['EEG']  # NumPy array of EEG data
sampling_rate = eeg_data['SamplingRate']

# Display basic metadata
print("Study Information:")
for key, value in study_info.items():
    print(f"{key}: {value}")

print("\nChannel Names:")
print(channel_names)

print("\nSampling Rate:", sampling_rate)
print("\nAnnotations (notes):")
for annotation in annotations:
    print(annotation)

# Example: Save EEG signals to a NumPy file for further analysis
np.save('eeg_signals.npy', eeg_signals)
np.save('channel_names.npy', channel_names)

# Optional Anonymization:
# Before saving or exporting data, manually anonymize identifiable metadata
study_info_anonymized = study_info.copy()
study_info_anonymized['PatientName'] = 'Anonymized'
study_info_anonymized['PatientID'] = '000000'
study_info_anonymized['DOB'] = '1900-01-01'

# Save anonymized metadata to a JSON file
import json
with open('study_info_anonymized.json', 'w') as f:
    json.dump(study_info_anonymized, f)

print("EEG data loaded and anonymized metadata saved.")
```

--------
# Natus 8.5 (long recordings)

Natus’s software suite includes a batch export tool, EDFExport.exe, for converting proprietary files to EDF/EDF+.
- https://data2bids.greydongilmore.com/run_data2bids/04_neuroworks_export 

- Users first create an export template (.exp file) within NeuroWorks: this template defines which channels to include and to de-identify patient info.
- The template is saved under the Neuroworks Settings directory and must remain there for the exporter to use it. 
- Once the template is prepared, batch conversion is done via command-line. One writes a text file listing the studies (paths to the .eeg files), then runs EDFExport with the template, for example:

```text
"C:\Neuroworks\EDFExport.exe" -f "studies_list.txt" -o "output_folder\"
```
This will output EDF/EDF+ files for each study. 
The EDFExport utility relies on the Natus software environment (not open-source).
EDFExport command-line utility:

```php
Usage:
  EDFExport -s /path-to-study-folder -t path-to-template -o path-to-output_dir
```
- template (likely JSON or XML) to specify header contents and event inclusion. With a custom template, one can remove or anonymize a patient's name, ID, DOB, etc. Without -t, EDFExport won't know how to omit or include metadata fields.

EDFExport- How to use templates with the command? Does it allow anonymisation? 

```phd
c:\NeuroWorks>edfexport -d \\10.40.15.131\public\Archive -edfplus -o "C:\Users\Nicolete\Desktop\GAVINTEST\EDFExport"

c:\NeuroWorks>edfexport -f "C:\Users\Nicolete\Desktop\GAVINTEST\EDFExport\Subject_1.txt"  -o "C:\Users\Nicolete\Desktop\GAVINTEST\EDFExport"
```
----------

# Codes under consideration for EEG analysis
Sent the request form to access TUH dataset
  
- https://github.com/UnitedHolmes/seizure_detection_EEGs_transformer_BHI_2023
- https://github.com/pulp-bio/Artifact-Seizure

# Catwell Arc 3.1.534, waiting for the new App.



