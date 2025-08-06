# Database: TUH EEG Event Corpus
Dataset contains events including periodic lateralized epileptiform discharge, generalized periodic epileptiform discharge,
spike and/or sharp wave discharges, artifact, and eye movement. 


00002275_00000001.edf: The actual edf file. 
		      00002275: a reference to the train index. 
		      00000001: indicating that this is the first file in
		      associated with this patient. 

There are six types of files in this release:

 *.edf: the EEG sampled data in European Data Format (edf) 

 *.htk: feature extraction based on the approach explained in "Improved EEG 
        Event Classification Using Differential Energy".

 *.lab: annotation file with a label given for every 10 microseconds. named 
        according to channel number. 

 *.rec: annotation file with labels given in seconds. 

lab files use 4 letter codes: 

 spsw: spike and slow wave
 gped: generalized periodic epileptiform discharge
 pled: periodic lateralized epileptiform dischage
 eyem: eye movement
 artf: artifact
 bckg: background

In the format:

 117100000 117200000 eyem

The fields are: start and stop time in 10s of microseconds and label

rec files use numeric codes:

 1: spsw
 2: gped
 3: pled
 4: eyem
 5: artf
 6: bckg

In the format: 13,90.4,91.4,6
The fields are: channel number, start time in seconds, stop time in seconds, and label. 

The channel number in .rec and .lab files refers to the channels
defined using a standard ACNS TCP montage. This is our preferred way
of viewing seizure data. The montage is defined as follows:

 montage =  0, FP1-F7: EEG FP1-REF --  EEG F7-REF
 montage =  1, F7-T3:  EEG F7-REF  --  EEG T3-REF
 montage =  2, T3-T5:  EEG T3-REF  --  EEG T5-REF
 montage =  3, T5-O1:  EEG T5-REF  --  EEG O1-REF
 montage =  4, FP2-F8: EEG FP2-REF --  EEG F8-REF
 montage =  5, F8-T4 : EEG F8-REF  --  EEG T4-REF
 montage =  6, T4-T6:  EEG T4-REF  --  EEG T6-REF
 montage =  7, T6-O2:  EEG T6-REF  --  EEG O2-REF
 montage =  8, A1-T3:  EEG A1-REF  --  EEG T3-REF
 montage =  9, T3-C3:  EEG T3-REF  --  EEG C3-REF
 montage = 10, C3-CZ:  EEG C3-REF  --  EEG CZ-REF
 montage = 11, CZ-C4:  EEG CZ-REF  --  EEG C4-REF
 montage = 12, C4-T4:  EEG C4-REF  --  EEG T4-REF
 montage = 13, T4-A2:  EEG T4-REF  --  EEG A2-REF
 montage = 14, FP1-F3: EEG FP1-REF --  EEG F3-REF
 montage = 15, F3-C3:  EEG F3-REF  --  EEG C3-REF
 montage = 16, C3-P3:  EEG C3-REF  --  EEG P3-REF
 montage = 17, P3-O1:  EEG P3-REF  --  EEG O1-REF
 montage = 18, FP2-F4: EEG FP2-REF --  EEG F4-REF
 montage = 19, F4-C4:  EEG F4-REF  --  EEG C4-REF
 montage = 20, C4-P4:  EEG C4-REF  --  EEG P4-REF
 montage = 21, P4-O2:  EEG P4-REF  --  EEG O2-REF

For example, channel 1 is a difference between electrodes F7 and T3,
and represents an arithmetic difference of the channels
(F7-REF)-(T3-REF), which are channnels contained in the EDF file.

Finally, here are some basic descriptive statistics about the data:

EVALUATION SET:

files: 159
       containing spsw: 9
       containing gped: 28
       containing pled: 33
       containing artf: 46
       containing eyem: 35 
       containing bckg: 89

TRAINING SET:

files: 359
       containing spsw: 27
       containing gped: 51
       containing pled: 48
       containing artf: 164
       containing eyem: 46 
       containing bckg: 211


