# Serverless website for food co-op

## Instructions to setup local enviornment:

### 1. Get python 2.7 and pip

  * Windows: Goto this link and follow instructions: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

  * Mac: You already have it
### 2. Clone this repo
  * If you have windows install git: https://git-scm.com/download/win
  * Open up a terminal and run `git clone https://github.com/mkerrig/food-coop.git`


### 3. Get virtualenv and source into your new virtual enviornment
  * Open up a terminal and run `pip install virtualenv`
  * Then use the `cd` command to change into the directory that you just cloned the repo into
  * Then run `virtualenv --no-site-packages venv`
  * Then run `source venv/bin/activate` or I believe `source venv\bin\activate` on Windows

### 4. Run `pip install -r requirements.txt`

### 5. Change the necessary HTML and other static files in `templates/` and `static/`
  * Test the your local version of the site by running `python food_coop.py` then open http://127.0.0.1:5000/ in your browser
  * Put all new static files in static, otherwise uploads won't work
  * To upload static files to our S3 bucket that you are referring to in the HTML run `python upload_static_resources.py`
  * Make the source links in the following format: static/INSERT-FILENAME-HERE

### 6. Make a pull request to this repo so I can upload your changes to the live site

Live site is up at: https://jqb7m64ze7.execute-api.us-east-1.amazonaws.com/dev

Nothing there really right now, awaiting your guy's changes

Flask's HTML supports jinja2 http://jinja.pocoo.org/docs/dev/
