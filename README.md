# Right Now Alerts
Script to check if the Right Now value of Google Analytics drops and notify via SES

## Configuration
It needs a few environment variables to work, no DB needed.

```
AWS_ACCESS_KEY_ID = 'YOUR-AWS-KEY-ID'
AWS_SECRET_ACCESS_KEY = 'YOUR-AWS-SECRET-KEY'
AWS_REGION = 'YOUR-AWS-REGION'
FROM_EMAIL = 'THE-EMAIL-YOU-WANT-TO-SEND-ALERTS-FROM'
ALERTS = """[{
    "ga_id": 99999999,
    "email": "alert@me.com",
    "percentage": 10
}]"""
ANALYTICS_KEY_NAME = 'analytics.key'  <= Path to your JSON key file
```

More info on how to get the Analytics key [here](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py).
