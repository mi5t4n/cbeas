import pyrebase

config = {
  "apiKey"           : "AIzaSyDWqZmqXJ8EOT8BhN2I_TM1JL9PrpJAdq0",
  "authDomain"       : "eloquent-drive-110521.firebaseapp.com",
  "databaseURL"      : "https://eloquent-drive-110521.firebaseio.com",
  "projectId"        : "eloquent-drive-110521",
  "storageBucket"    : "eloquent-drive-110521.appspot.com",
  "messagingSenderId": "917806153189",
  "appId"            : "1:917806153189:web:b4f1782fcfdb0bad53030c",
  "measurementId"    : "G-5X20RHBLP4"
};

firebase = pyrebase.initialize_app(config)

auth = firebase.auth();

# try :
auth.create_user_with_email_and_password("the@the.com", "the123")
# except:
#     print("User already registered")