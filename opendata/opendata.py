import requests, json, csv
import os

from config.settings import OPENDATA_APP_TOKEN, OPENDATA_URLS, OPENDATA_COLUMNS
APP_TOKEN = os.getenv("OPENDATA_APP_TOKEN") or OPENDATA_APP_TOKEN

if __name__ == '__main__':
    pass
