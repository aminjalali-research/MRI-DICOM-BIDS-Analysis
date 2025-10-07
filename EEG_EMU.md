# EEG-EMU (Epilepsy Monitoring Machine)

1. Nicolet NicVue bought by Natus (short recordings). File types are:

- .e or .eeg – primary EEG data
- .erd – raw EEG binary (used by Neuroworks / Xltek systems)
- .ent – annotations/notes metadata
- .NPA – metadata wrapper used by NicVue

Can these files be read or anonymized? 
The .erd formats are compressed and proprietary, and there is no publicly documented Python library. Users convert to EDF via the Natus GUI instead.
- .erd can be read by unofficial code in Archived XltekDataReader (Python) [(Link)](https://github.com/nyuolab/XltekDataReader)

I asked Natus: " We are currently using XLTEK Neuroworks (Natus) in our EMU. I am reaching out to inquire if it is possible to export anonymised EEG data using an API."
Their response: We do not have an API, but you can use UI or EDFExport.exe. 

Natus provided a Platform Migration Utility to migrate data from legacy NicVue systems into a NeuroWorks database
[download.xltek.com](https://download.xltek.com/eeg/Software/Neuroworks/DOC-020491%20REV%2005%20-%20Platform%20Migration%20Utility%20User%20Guide.pdf#:~:text=from%20legacy%20source%20systems%20such,Database%20application%2C%20used%20with%20NeuroWorks). 

# Requested
- We are trying to batch-export via the command line using EDFExport.exe:
c:\NeuroWorks>edfexport -f "C:\Users\Nicolete\Desktop\TEST\EDFExport\Subject_1.txt" -o "C:\Users\Nicolete\Desktop\TEST\EDFExport"

- Could you please advise on how to specify a template when calling edfexport from the command line (e.g., a flag like -t or a config file path)? - Are there examples or a reference for acceptable template fields and syntax outside the UI?
- Does the command-line tool support anonymization/de-identification (e.g., removing patient name/ID, date of birth, study date/time offsets)?
- If so, what flags or template settings enable this, and can they be applied in batch mode?
- Is there a command-line user guide or man page for EDFExport.exe that covers templates/anonymization?

--------
# Natus 8.5 (long recordings)

Natus’s software suite includes a batch export tool, EDFExport.exe, for converting proprietary files to EDF/EDF+.
- https://data2bids.greydongilmore.com/run_data2bids/04_neuroworks_export
  (Create a workflow and put it here to explain)

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
In research contexts, the usual approach is to export EEG recordings to EDF via NicVue/NeuroWorks itself, rather than parse .NPA in code. 
(Notably, the Temple University Hospital EEG Corpus was originally in Natus proprietary format and was converted to EDF using NicVue software
[par.nsf.gov](https://par.nsf.gov/servlets/purl/10199699#:~:text=,proprietary%20NicVue%20software%20tool).

----------

# Catwell Arc 3.1.534, waiting for the new App.



