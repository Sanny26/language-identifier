# language-identifier


Identifies the language of given text file.

Implementation of this paper: 
> Cavnar, William B., and John M. Trenkle. "N-gram-based text categorization." Ann arbor mi 48113.2 (1994): 161-175.


Dataset used for experiments:
> https://github.com/xprogramer/DLI32-corpus

The above link provides two folders DLI32 and DLI32-2. DLI32 used as train set to produce language profiles for languages.

When tested on DLI32-2, achieved an accuracy of 60% for language profiles of length 50.


#### Usage

For training:
- Download the datasets. Move the dataset and the code into one folder.

- To train, run ```python identifier.py ```

This generates ```lprofiles.pkl``` pickle file which contains the language profiles for 32 langauges.

- To test, run ```python test.py```



Requirements
-Python
-NLTK


