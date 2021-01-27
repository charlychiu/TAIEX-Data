import requests
import json
import time

my_headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
count = 0
for y in range(2002, 2021):
  for m in range(1, 13):
    filename = "{0}{1:0>2d}01".format(y, m)
    r = requests.get('https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=' + filename, headers=my_headers)
    with open(filename + '.json', 'w') as outfile:
      json.dump(r.json(), outfile)
    time.sleep(2)
    print(filename)
    count += 1