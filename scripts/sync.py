from datetime import datetime
from airtable import Airtable

import requests
import os


AIRTABLE_API_KEY = os.environ['AIRTABLE_KEY']
AIRTABLE_BASE_IDS = {
    "Exercise": "apps9I8lYxsuqtna3",
    "Finances": "appyzt6LXbkj6sKTR",
    "Reading": "app8MVTdSDI1VoBtY",
    "Photography": "appYfWdQzjVRlwGFr",
    "Personal CRM": "appLKmLPONPn638mT",
    "Travel": "appuSOwhmqDDgqaKU",
    "Chess": "appcZLQut8wlUHNoJ",
    "Spanish": "appOuYQYYUo4615YH",
}

CHESS_URL = "https://api.chess.com/pub/player/zadvanced/stats"
DUOLINGO_URL = 'https://www.duolingo.com/2017-06-30/users/22531064'


def pull_chess():
    chess_data = requests.get(CHESS_URL).json()
    return chess_data

def pull_duo():
    duo_data = requests.get(DUOLINGO_URL).json()
    return duo_data

def push_airtable():
    pass

if __name__ == "__main__":
    print(pull_chess())
    print(pull_duo())