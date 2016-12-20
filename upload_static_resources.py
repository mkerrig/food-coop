import json
import flask_s3
from food_coop import app

with open('aws_settings.json', 'r') as aws_settings_stream:
    aws_settings = json.loads(aws_settings_stream.read())
# Get Flask_S3 settings
for key, value in aws_settings.iteritems():
    app.config[key] = value

flask_s3.create_all(app)
