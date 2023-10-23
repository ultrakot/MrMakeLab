# use creds to create a client to interact with the Google Drive API


#creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.path.dirname(__file__), 'client_secret.json'), scope)
#client = gspread.authorize(creds)

#get text from google doc file and return it as a string