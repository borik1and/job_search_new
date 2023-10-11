from pprint import pprint

from src.class_api import HH_API, SJ_API

# sj_api = SJ_API()
#
# pprint(sj_api.get_vacancies())
# print('Введите слово для поиска вакансий')

keyword = input('Введите слово для поиска вакансий: ')

hh = HH_API(keyword)
hh_vacancies = hh.format_vacancies(hh.get_vacancies())

sj = SJ_API(keyword)
sj_vacancies = sj.format_vacancies(sj.get_vacancies())

# объединить вакансии hh и sj в один общий список с платформ

vacancies = []
