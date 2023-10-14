import os
from src.class_save import JsonSave, add_vacancy
# from pprint import pprint
from src.class_api import HH_API, SJ_API
from src.vacancies import Vacancy

keyword = input('Введите слово для поиска вакансий: ')
print()
print("'1' - hh.ru, '2' - superjob.ru, '3' - на обоих платформах")
set_platform = input('Выберите платформу для поиска вакансий: ')

hh = HH_API(keyword)
hh_vacancies = hh.format_vacancies(hh.get_vacancies())

sj = SJ_API(keyword)
sj_vacancies = sj.format_vacancies(sj.get_vacancies())

if set_platform == '1':
    print('Ваш выбор искать на hh.ru')
    JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies']
elif set_platform == '2':
    print('Ваш выбор искать на superjob.ru')
    JsonSave.all_vacancies['vacancies'] = sj_vacancies['vacancies']
elif set_platform == '3':
    print('Ваш выбор искать на везде')
    JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies'] + sj_vacancies['vacancies']
else:
    print('Ваш выбор не опознан, ищем везде.')
    JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies'] + sj_vacancies['vacancies']

# объединить вакансии hh и sj в один общий список с платформ
# JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies'] + sj_vacancies['vacancies']

# сохраняем в файл json
add_vacancy()
# Vacancy.instantiate_from_json

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
