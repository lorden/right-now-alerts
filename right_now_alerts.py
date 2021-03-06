import json
import time
import sys
import settings
import logging
from analytics import Analytics
from simpleemailservice import SimpleEmailService


class RightNowAlert(object):
    def __init__(self, ga_id, emails, percentage=10):
        self.percentage = percentage
        self.analytics = Analytics(ga_id, settings.ANALYTICS_KEY_NAME)
        self.previous_value = self.analytics.get_right_now()
        self.emails = emails.split(',')
        self.name = self.analytics.get_name()
        self.message = ''

    def is_triggered(self):
        current_value = self.analytics.get_right_now()
        if self.previous_value:
            current_percentage = (float(current_value) / float(self.previous_value)) * 100
            if current_percentage < 100 - self.percentage:
                self.message = '{} -> {}'.format(self.previous_value, current_value)
                self.previous_value = current_value
                return True
            self.previous_value = current_value


if __name__ == '__main__':

    right_now_alerts = []

    try:
        alerts = json.loads(settings.ALERTS)
        for alert in alerts:
            right_now_alerts.append(
                RightNowAlert(
                    alert['ga_id'],
                    alert['email'],
                    percentage=alert.get('percentage', 10),
                )
            )
    except json.decoder.JSONDecodeError:
        sys.exit('Your configuration has an invalid format')

    logging.basicConfig(filename=settings.LOG_FILE, filemode='w', level=logging.INFO)
    logging.info('Starting Right Now Alerts')
    while True:
        for alert in right_now_alerts:
            trigger = alert
            if alert.is_triggered():
                ses = SimpleEmailService(
                    settings.AWS_ACCESS_KEY_ID,
                    settings.AWS_SECRET_ACCESS_KEY,
                    settings.AWS_REGION,
                )

                subject = 'Alert for {}!'.format(alert.name)
                message = 'Big drop for {} in {} seconds: {}.'.format(alert.name, settings.INTERVAL, alert.message)

                ses.send(settings.FROM_EMAIL, alert.emails, subject, message)
                logging.info('Email sent!')
        time.sleep(settings.INTERVAL)
