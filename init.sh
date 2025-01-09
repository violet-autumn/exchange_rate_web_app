## Make a virtual env and activate it
python3 -m venv .venv
source .venv/bin/


## Upgrade pip and install packages
python3 -m pip install -U pip
pip install requests python-dotenv Flask waitress


## Create requirements file
pip freeze > requirements.txt


## Create folder and file structure 
# templates for html templates
# static/styles for css 
# .gitignore 
# .env for environment variables
# currency.py for the defining the functiom calling the API
# server.py for routing/serving using the flask framework  