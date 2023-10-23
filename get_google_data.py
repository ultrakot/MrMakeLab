#get information form google sheet

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json
import os
from googleapiclient.discovery import build 
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


#get client_secret.json file from current directory
path = os.path.join(os.path.dirname(__file__), 'client_secret.json')

creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
client = gspread.authorize(creds)

#open google sheet
sheet = client.open('MrMakeLab').sheet1

#extract and print all of the values
list_of_hashes = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(list_of_hashes)

#extract and print all of the values
list_of_hashes = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(list_of_hashes)

#extract and print all of the values
list_of_hashes = sheet.get_all_records()