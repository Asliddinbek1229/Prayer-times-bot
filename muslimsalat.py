# Code author: Dagaraliyev Asliddinbek.

import requests

# url = "https://muslimsalat.com/namangan/daily/07-04-2023/true.json?key=f30d81618094dbaaca225fa709f2c094"
#
# r = requests.get(url)
# res = r.json()
#print(res)
#print(res['items'][0])

def prayer_times():
     url = "https://muslimsalat.com/namangan.json?key=f30d81618094dbaaca225fa709f2c094"

     r = requests.get(url)
     res = r.json()
     p_times = {}
     p_times['🕓 Bomdod'] = res['items'][0]['fajr']
     p_times['🕔 Shuroq'] = res['items'][0]['shurooq']
     p_times['🕛 Peshin'] = res['items'][0]['dhuhr']
     p_times['🕟 Asr'] = res['items'][0]["asr"]
     p_times['🕡 Shom'] = res['items'][0]['maghrib']
     p_times['🕤 Hufton'] = res['items'][0]['isha']
     return p_times




