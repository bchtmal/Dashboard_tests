import requests
from .enviroment import *

#Сравнение данных по 3 графикам между собой.

env = dev  #( rcod / test / dev )
start_date = '2024-01-01'
end_date= '2024-07-01'
budget ='184'


def test_planned():
    with requests.Session() as s:
        s.post(f'{env}/login/?', data=admin)
        r_realization = s.get(f'{env}/api/budget_planning/allocation_'
                              f'execution/?budgets={budget}&status=planned_price&start_date={start_date}&end_'
                              f'date={end_date}&is_thousands=False&po=True').json()
        sum_ = 0
        for item in r_realization:
            planned_price = item['planned_price']['rawValue']
            sum_ += planned_price
        r_by_month = s.get(f'{env}/api/budget_planning/allocation_'
                           f'execution/by_month/?budgets={budget}&status=planned_price&start'
                           f'_date={start_date}&end_date={end_date}&is_thousands=False&po=True').json()
        sum_1 = r_by_month[0]['planned_price'][-1]['rawCumsum']
        r_allocation_execution = s.get(f'{env}/api/budget_planning/allocation'
                                       f'_execution/by_month/?budgets={budget}&status=planned_price&start_date='
                                       f'{start_date}&end_date={end_date}&is_thousands=False&po=True').json()

        sum_2 =  r_allocation_execution[0]['planned_price'][-1]['rawCumsum']
        assert sum_.__round__(2) == sum_1.__round__(2) == sum_2.__round__(2)


def test_contract_total_price():
    with requests.Session() as s:
        s.post(f'{env}/login/?', data=admin)
        r_realization = s.get(f'{env}/api/budget_planning/allocation_'
                              f'execution/?budgets={budget}&status=contract_total_price&start_date={start_date}&end_'
                              f'date={end_date}&is_thousands=False&po=True').json()
        sum_ = 0
        for item in r_realization:
            contract_total_price = item['contract_total_price']['rawValue']
            sum_ += contract_total_price
        r_by_month = s.get(f'{env}/api/budget_planning/allocation_'
                           f'execution/by_month/?budgets={budget}&status=contract_total_price&start'
                           f'_date={start_date}&end_date={end_date}&is_thousands=False&po=True').json()

        sum_1 = r_by_month[0]['contract_total_price'][-1]['rawCumsum']
        r_allocation_execution = s.get(f'{env}/api/budget_planning/allocation'
                                       f'_execution/by_month/?budgets={budget}&status=contract_total_price&start_date='
                                       f'{start_date}&end_date={end_date}&is_thousands=False&po=True').json()

        sum_2 = r_allocation_execution[0]['contract_total_price'][-1]['rawCumsum']
        assert sum_.__round__(2) == sum_1.__round__(2) == sum_2.__round__(2)

def test_total_published_price():
    with requests.Session() as s:
        s.post(f'{env}/login/?', data=admin)
        r_realization = s.get(f'{env}/api/budget_planning/allocation_'
                              f'execution/?budgets={budget}&status=total_published_price&start_date={start_date}&end_'
                              f'date={end_date}&is_thousands=False&po=True').json()

        sum_ = 0
        for item in r_realization:
            contract_total_price = item['total_published_price']['rawValue']
            sum_ += contract_total_price
        r_by_month = s.get(f'{env}/api/budget_planning/allocation_'
                           f'execution/by_month/?budgets={budget}&status=total_published_price&start'
                           f'_date={start_date}&end_date={end_date}&is_thousands=False&po=True').json()

        sum_1 = r_by_month[0]['total_published_price'][-1]['rawCumsum']
        r_allocation_execution = s.get(f'{env}/api/budget_planning/allocation'
                                       f'_execution/by_month/?budgets={budget}&status=total_published_price&start_date='
                                       f'{start_date}&end_date={end_date}&is_thousands=False&po=True').json()

        sum_2 = r_allocation_execution[0]['total_published_price'][-1]['rawCumsum']
        assert sum_.__round__(2) == sum_1.__round__(2) == sum_2.__round__(2)

def test_rest_price():
    with requests.Session() as s:
        s.post(f'{env}/login/?', data=admin)
        r_realization = s.get(f'{env}/api/budget_planning/allocation_'
                              f'execution/?budgets={budget}&status=rest_price&start_date={start_date}&end_'
                              f'date={end_date}&is_thousands=False&po=True').json()
        sum_ = 0
        for item in r_realization:
            contract_total_price = item['rest_price']['rawValue']
            sum_ += contract_total_price
        r_by_month = s.get(f'{env}/api/budget_planning/allocation_'
                           f'execution/by_month/?budgets={budget}&status=rest_price&start'
                           f'_date={start_date}&end_date={end_date}&is_thousands=False&po=True').json()
        sum_1 = r_by_month[0]['rest_price'][-1]['rawCumsum']
        r_allocation_execution = s.get(f'{env}/api/budget_planning/allocation'
                                       f'_execution/by_month/?budgets={budget}&status=rest_price&start_date='
                                       f'{start_date}&end_date={end_date}&is_thousands=False&po=True').json()
        sum_2 = r_allocation_execution[0]['rest_price'][-1]['rawCumsum']
        assert sum_.__round__(2) == sum_1.__round__(2) == sum_2.__round__(2)

def test_planned_allocation_limit():
    with requests.Session() as s:
        s.post(f'{env}/login/?', data=admin)
        r_realization = s.get(f'{env}/api/budget_planning/allocation_'
                              f'execution/?budgets={budget}&status=rest_price&start_date={start_date}&end_'
                              f'date={end_date}&is_thousands=False&po=True').json()
        sum_ = 0
        for item in r_realization:
            planned_allocation_limit = item['planned_allocation_limit']['rawValue']
            sum_ += planned_allocation_limit
        r_by_month = s.get(f'{env}/api/budget_planning/allocation_'
                           f'execution/by_month/?budgets={budget}&status=rest_price&start'
                           f'_date={start_date}&end_date={end_date}&is_thousands=False&po=True').json()
        sum_1 = r_by_month[0]['planned_allocation_limit'][-1]['rawCumsum']
        r_allocation_execution = s.get(f'{env}/api/budget_planning/allocation'
                                       f'_execution/by_month/?budgets={budget}&status=rest_price&start_date='
                                       f'{start_date}&end_date={end_date}&is_thousands=False&po=True').json()
        sum_2 = r_allocation_execution[0]['planned_allocation_limit'][-1]['rawCumsum']
        assert sum_.__round__(2) == sum_1.__round__(2) == sum_2.__round__(2)