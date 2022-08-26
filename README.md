# MetadataCollection
August 2021, Laura Cooper, CAMDU@warwick.ac.uk

An app to prompt users to collect minimal metadata for microscopy images. Metadata is stored in a .csv file.

## Install 
### conda:

conda create -n myenv python=3.8\
conda activate myenv\
conda install pyqt

To build standalone app:\
conda install pyinstaller

### venv:
Install python 3.8 and then run:

python3 -m venv myenv\
. myenv/bin/activate\
pip install pyqt5

To build standalone app:\
pip install pyinstaller

## To run
python MetaCollection.py

## To build 
### Windows 10
pyinstaller --icon="path\to\square_black.ico" --add-data="path\to\info.png";. MetaCollection.py

### Ubuntu 20
pyinstaller MetaCollection.py
