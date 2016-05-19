import os

INTERVAL = int(os.environ.get('INTERVAL', 60))
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION = os.environ.get('AWS_REGION', 'us-west-2')
ALERTS = os.environ['ALERTS']
ANALYTICS_KEY_NAME = os.environ['ANALYTICS_KEY_NAME']
FROM_EMAIL = os.environ['FROM_EMAIL']
