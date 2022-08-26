# MetadataCollection
August 2021, Laura Cooper, CAMDU@warwick.ac.uk

An app to prompt users to collect minimal metadata for microscopy images. Metadata is stored in a .csv file.

### Install packages, conda:

conda create -n myenv python=3.8\
conda activate myenv\
conda install pyqt\

To build standalone app:\
conda install pyinstaller\

### Install packages, venv:

For omero-py only:\
Install python 3.8 and then run:

python3 -m venv myenv\
. myenv/bin/activate\
pip install pyqt5

To build standalone app:\
pip install pyinstaller\
