# aconnexion_test
A single GET API in Flask that renders specific content

# Setup
- Create a virtual environment using virtualenv
- virtualenv /path/to/your/env
- source /path/to/your/env/bin/activate
- pip install -r requirements.txt

# To start the Flask web server run
- python renderer.py

# Sample API calls

- http://localhost:5000/v1/get-html-content
- http://localhost:5000/v1/get-html-content?fileName=file1.txt
- http://localhost:5000/v1/get-html-content?fileName=file1.txt&start=7&end=15

