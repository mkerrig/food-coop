from flask import Flask, render_template
from flask_s3 import FlaskS3

s3 = FlaskS3()
def start_app():
    app = Flask(__name__)
    app.config['FLASKS3_BUCKET_NAME'] = 'zappa-mkerrig'
    # Set to False to debug using local resources
    app.config['FLASKS3_ACTIVE'] = True
    s3.init_app(app)
    return app

app = start_app()

@app.route('/')
def index():
    return render_template('basic.html')

# We only need this for local development.
if __name__ == '__main__':
    app.run()
