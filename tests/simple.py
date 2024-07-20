import requests
import enviroment
from enviroment import *



env = rcod #( rcod / test / dev )

URL = (f'{env}/issue/api/realization/?page=%s&page_size=50&coordination_ctask_status=passed&publication_'
       f'notification_status=expired&publication_notification_status=planned&publication_notification_status='
       f'not_included&concluded_contract_status=not_included&issue_class=purchase_issue_bill_of_goods_other&issue_'
       f'class=purchase_issue_simple_other&budgets=183&budgets=184&budgets=185&budgets=186&budgets=188&supervising_childs_org=3056'
      )

with requests.Session() as s:
    s.post(f'{env}/login/?', data=admin)

    next, page = True, 1
    total_sum = 0.0

    while next == True:
        response = s.get(URL % page).json()
        current_sum = sum(item['bill_of_goods_total_sum_raw'] for item in response['results'])
        total_sum += current_sum
        print(f'{page} {current_sum.__round__(2)} {total_sum.__round__(2)}')

        next, page = response['next'], page + 1
