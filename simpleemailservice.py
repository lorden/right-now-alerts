import boto.ses


class SimpleEmailService(object):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region):
        self.conn = boto.ses.connect_to_region(
            region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key)

    def send(self, sender, recipients, subject, body):
        self.conn.send_email(sender, subject, body, recipients)
