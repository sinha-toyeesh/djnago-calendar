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
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'E:\\Dev-Works\\django_test\\apiTest\\main_app\\client_secrets.json', SCOPES)
            creds = flow.run_local_server(host='localhost')
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 100 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=100, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        newTest = []

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            id_event = event['id']
            summary_event = event['summary']
            varTest = {"start": {"date": repr(start)}, "id_event": repr(id_event), "summary":repr(summary_event)}
            newTest.append(varTest)

    except HttpError as error:
        print('An error occurred: %s' % error)
    
    return newTest



# def test_calendar():
#     print("RUNNING TEST_CALENDAR()")

#     credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#     service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

#     # CREATE A NEW EVENT
#     new_event = {
#     'summary': "Ben Hammond Tech's Super Awesome Event",
#     'location': 'Denver, CO USA',
#     'description': 'https://benhammond.tech',
#     'start': {
#         'date': f"{datetime.date.today()}",
#         'timeZone': 'America/New_York',
#     },
#     'end': {
#         'date': f"{datetime.date.today() + datetime.timedelta(days=3)}",
#         'timeZone': 'America/New_York',
#     },
#     }
#     service.events().insert(calendarId=CAL_ID, body=new_event).execute()
#     print('Event created')

#  # GET ALL EXISTING EVENTS
#     events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
#     events = events_result.get('items', [])

#     # LOG THEM ALL OUT IN DEV TOOLS CONSOLE
#     for e in events:

#         print(e)

#     #uncomment the following lines to delete each existing item in the calendar
#     #event_id = e['id']
#         # service.events().delete(calendarId=CAL_ID, eventId=event_id).execute()


#     return events
