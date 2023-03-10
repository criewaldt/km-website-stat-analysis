import requests, json, csv
import os

import pprint

from config.settings import OPENDATA_APP_TOKEN, OPENDATA_COLUMNS, OPENDATA_URLS
APP_TOKEN = os.getenv("OPENDATA_APP_TOKEN") or OPENDATA_APP_TOKEN

class GetDataByJOB():
    def __init__(self,):
        pass
        #self.bis = self.bis()
        #self.now = self.now()

    def bis(self,):
        url = OPENDATA_URLS['bis']
        payload = {
            "$$app_token" : APP_TOKEN,
            "$limit" : 1000000000
            }
        r = requests.get(url, params=payload)
        print('Grabbed {} BIS apps'.format(len(r.json())))
        

    def now(self,):
        url = OPENDATA_URLS['now']
        payload = {
            "$$app_token" : APP_TOKEN,
            "$limit" : 1000000000
            }
        r = requests.get(url, params=payload)
        print('Grabbed {} NOW apps'.format(len(r.json())))

        

    def get_data(self, dataset, job):
        
        url = OPENDATA_URLS[dataset]
        job_number_column = OPENDATA_COLUMNS[dataset]['job']

        payload = {
            "$$app_token" : APP_TOKEN,
            }

        if dataset == 'bis':
            payload[job_number_column] = job
            payload['doc__'] = '01'
        else:
            payload['$where'] = "{} LIKE '%{}-I1%'".format(job_number_column, job)
        
        r = requests.get(url, params=payload)

        return_data = []

        for col in OPENDATA_COLUMNS[dataset]:
            try:
                return_data.append(r.json()[0][OPENDATA_COLUMNS[dataset][col]])

            except KeyError:
                return_data.append('n/a')

        return return_data

if __name__ == '__main__':
    pass
