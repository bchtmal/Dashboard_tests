import requests
import enviroment
from enviroment import *

env = dev #( rcod / test / dev )

url = ('http://kis.dev.sfup-test.netrika/api/issue/realization/?org=3056&type=none&start_date=2024-01-01&'
       'end_date=2024-07-11&is_thousands=False&po=True&year=2024')

with requests.Session() as s:
    s.post(f'{env}/login/?', data=admin)
    r_realization = s.get(url).json()

    raw_values = [item["rawValue"] for item in r_realization]

    del raw_values[8]

    print(sum(raw_values).__round__(2))




