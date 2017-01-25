from flask import Flask, render_template
from flask_s3 import FlaskS3
from flask import request
import boto3
import time
dynamodb = boto3.resource('dynamodb')
table =  dynamodb.Table('Users')

s3 = FlaskS3()
def start_app():
    app = Flask(__name__)
    app.config['FLASKS3_BUCKET_NAME'] = 'zappa-mkerrig'
    # Set to False to debug using local resources
    app.config['FLASKS3_ACTIVE'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True # Local dev only
    s3.init_app(app)
    return app

app = start_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/1/users/addUser')
def add_user():
    email = request.args.get('email')
    if not email:
        return 'Must include email in request args', 404
    epochCreated = int(time.time())
    try:
        table.put_item(
        Item={
        'email': email,
        'epochCreated': epochCreated
        })
    except Exception as e:
        return 'Account could not be created, error: {}'.format(e), 404
    return 'Account created succesfully!'


# We only need this for local development.
if __name__ == '__main__':
    app.run()
"""
All you have to do to render a new page/route for flask is copy and paste, and
then fill in for the following:

@app.route('/<INSERT URL SUFFIX HERE>')
def index():
    return render_template('<FILENAME THAT IS IN templates/ HERE>')
"""
