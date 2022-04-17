from __future__ import print_function

import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def test_calendar():

    flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json', SCOPES)
    creds = flow.run_local_server(host='localhost')

    try:
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print('Getting the upcoming 100 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=100, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        newTest = []

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            id_event = event['id']
            summary_event = event['summary']
            varTest = {"start": {"date": repr(start)}, "id_event": repr(id_event), "summary":repr(summary_event)}
            newTest.append(varTest)

    except HttpError as error:
        print('An error occurred: %s' % error)
    
    return newTest
