#To install virtual environment
pip install virtualenv

#create virtual environment
python -m venv env

#Run the activate.bat file - either by going to ./scripts folder 
## through CMD
./env\Scripts\activate.bat
## through powershell
./env\Scripts\Activate.ps1

#install fastapi on virtual environment
pip install fastapi

#install sqlAlchemy orm
pip install sqlalchemy

#install server
pip install uvicorn

#to run server
uvicorn main:app --reload
