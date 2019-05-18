import urllib.request, json
import csv
with urllib.request.urlopen("https://data.adb.org/api/3/action/package_show?id=21d52d3b-e545-4268-a0cd-02864b8be2c4") as url:
    data = json.loads(url.read().decode())
    with open('data.json', 'w') as outfile:
    	json.dump(data, outfile)