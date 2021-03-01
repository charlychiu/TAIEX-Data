import requests
import json
import time
import os
from datetime import datetime

my_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
filename = datetime.today().strftime('%Y%m01')
y = datetime.today().strftime('%Y')
if not os.path.exists('history/' + str(y)):
    os.makedirs('history/' + str(y))

r = requests.get(
    'https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=' + filename, headers=my_headers)

if 'data' not in r.json():
    print('No contain data')
else:
    print('Got data count: ' + str(len(r.json()['data'])))
    print('Save file: ' + 'history/' + str(y) + '/' + filename + '.json')
    with open('history/' + str(y) + '/' + filename + '.json', 'w') as outfile:
        json.dump(r.json(), outfile)
