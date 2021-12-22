#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:26:59 2021

@author: ricardovieira
"""

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
num_events = 30
#calendar_id = 'primary'
calendar_dict = {"Weather" : "p#weather@group.v.calendar.google.com", "Phases of the Moon" : "ht3jlfaac5lfd6263ulfh4tql8@group.calendar.google.com", "Sunrise and sunset" : "i_194.169.1.99#sunrise@group.v.calendar.google.com", "Ricardo - Public" : "aqe66mnq1ov64j4t7g5tqpo4ao@group.calendar.google.com", "Ricardo Vieira" : "ricardo.ripoll.vieira@gmail.com", "Birthdays" : "addressbook#contacts@group.v.calendar.google.com", "Agarraditos" : "750i4nsgttl70l30u8n6uvutjc@group.calendar.google.com", "Family" : "family06916021744405896399@group.calendar.google.com", "Day of the Year" : "#daynum@group.v.calendar.google.com", "Pais" : "0bi9bq9e68mhl61im886esin1s@group.calendar.google.com", "LSEG" : "jeigdvb66d4kjglfn75ddaqot4@group.calendar.google.com", "Holidays in the United Kingdom" : "en-gb.uk#holiday@group.v.calendar.google.com", "UBS" : "enkdl8c602rg19u5j4r0hiaqcg@group.calendar.google.com", "UST" : "7k1dgffmu4m0mus9egkoeqki9g@group.calendar.google.com", "Credit Suisse" : "djaqum5d2pmvnk3stlolcra5lk@group.calendar.google.com", "UST" : "8fgp7333i5o8t2aafpo1m9slok@group.calendar.google.com", "Credit Suisse" : "d9dqf4rall8ckhcbjdv2m9k0vo@group.calendar.google.com", "RV-12ProMax" : "rt7np4slbaof2m0rnpslelqnb0@group.calendar.google.com"}
calendar_name = "Ricardo Vieira"
calendar_id = calendar_dict[calendar_name]

def main():
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        #now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        #print(str(num_events) + ' events')
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('----------------------------------------------------------------------------------------------------')
        events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                              maxResults=num_events, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next <num_events> events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print("{:30} {:<50}".format(start, event['summary']))
        print('----------------------------------------------------------------------------------------------------')
        print('Total: ' + str(len(events)) + ' events')
        print()

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
# [END calendar_quickstart]

"""
Weather: p#weather@group.v.calendar.google.com
Phases of the Moon: ht3jlfaac5lfd6263ulfh4tql8@group.calendar.google.com
Sunrise and sunset: i_194.169.1.99#sunrise@group.v.calendar.google.com
Ricardo - Public: aqe66mnq1ov64j4t7g5tqpo4ao@group.calendar.google.com
Ricardo Vieira: ricardo.ripoll.vieira@gmail.com
Birthdays: addressbook#contacts@group.v.calendar.google.com
Agarraditos: 750i4nsgttl70l30u8n6uvutjc@group.calendar.google.com
Family: family06916021744405896399@group.calendar.google.com
Day of the Year: #daynum@group.v.calendar.google.com
Pais: 0bi9bq9e68mhl61im886esin1s@group.calendar.google.com
LSEG: jeigdvb66d4kjglfn75ddaqot4@group.calendar.google.com
Holidays in the United Kingdom: en-gb.uk#holiday@group.v.calendar.google.com
UBS: enkdl8c602rg19u5j4r0hiaqcg@group.calendar.google.com
UST: 7k1dgffmu4m0mus9egkoeqki9g@group.calendar.google.com
Credit Suisse: djaqum5d2pmvnk3stlolcra5lk@group.calendar.google.com
UST: 8fgp7333i5o8t2aafpo1m9slok@group.calendar.google.com
Credit Suisse: d9dqf4rall8ckhcbjdv2m9k0vo@group.calendar.google.com
RV-12ProMax: rt7np4slbaof2m0rnpslelqnb0@group.calendar.google.com
"""