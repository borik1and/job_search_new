from pprint import pprint
import os
from src.vacancies import compare_vacancies_by_salary

from src.class_save import JsonSave, add_vacancy

# from pprint import pprint

from src.class_api import HH_API, SJ_API

# sj_api = SJ_API()

# pprint(sj_api.get_vacancies())
# print('Введите слово для поиска вакансий')

keyword = input('Введите слово для поиска вакансий: ')

hh = HH_API(keyword)
hh_vacancies = hh.format_vacancies(hh.get_vacancies())
# JsonSave.add_vacancy(hh_vacancies, 'hh_vacancie.json')

sj = SJ_API(keyword)
sj_vacancies = sj.format_vacancies(sj.get_vacancies())

# объединить вакансии hh и sj в один общий список с платформ
JsonSave.all_vacancies = hh_vacancies['vacancies'] + sj_vacancies['vacancies']

# сохраняем в файл json
add_vacancy()

# sorted_vacancies = compare_vacancies_by_salary()
# pprint(sorted_vacancies)
# Вывод отсортированных вакансий
# for vacancy in sorted_vacancies:
#     print(f"Наименование: {vacancy.name}, Зарплата: {vacancy.salary}")

# удалить временный файл с данными
erase = input('Хотите удалить временный файл с данными? да или нет?: ')
if erase == 'да' or erase == 'yes':
    if os.path.exists('vacancies.json'):
        os.remove('vacancies.json')
else:
    pass
# pprint(JsonSave.all_vacancies)
