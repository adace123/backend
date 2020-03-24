# Installation Guide
## Environment Installation
### Linux and MacOS

The venv folder contains all dependencies which are needed to run this project. To enter the virtual environment use:

`source venv/bin/activate `

If this is the first time running or if anything in the requirements has changed use:

`virtualenv venv && source venv/bin/activate && pip install -r requirements.txt `

after installing a new package use: 

`pip freeze > requirements.txt `

to update the requirments folder

### Windows
The venv folder contains all dependencies which are needed to run this project. To enter the venv virtual environment use: 

`source venv/bin/activate `

If this is the first time running or if anything in the requirements has changed use:

`virtualenv venv && source venv/Scripts/activate && pip install -r requirements.txt `

#### Important Note
Make sure to have python37 and python37\Scripts added in your environmental path.
Else command such as ```virtualenv venv``` may not work.


