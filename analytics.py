from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2


class Analytics(object):

    def __init__(self, ga_id, key_file_name):
        self.ga_id = ga_id
        self.key_file_name = key_file_name

    def get_right_now(self):
        scope = ['https://www.googleapis.com/auth/analytics.readonly']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.key_file_name, scopes=scope)
        http = credentials.authorize(httplib2.Http())
        service = build('analytics', 'v3', http=http)
        response = service.data().realtime().get(
            ids='ga:{}'.format(self.ga_id),
            metrics='rt:activeUsers'
        ).execute()
        value = response.get('totalsForAllResults', {}).get('rt:activeUsers', 0)
        return int(value)

    def get_name(self):
        scope = ['https://www.googleapis.com/auth/analytics.readonly']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.key_file_name, scopes=scope)
        http = credentials.authorize(httplib2.Http())
        service = build('analytics', 'v3', http=http)
        response = service.data().realtime().get(
            ids='ga:{}'.format(self.ga_id),
            metrics='rt:activeUsers'
        ).execute()
        return response['profileInfo']['profileName']
