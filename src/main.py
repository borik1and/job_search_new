from pprint import pprint

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

JsonSave.all_vacancies = hh_vacancies['vacancies'] + sj_vacancies['vacancies']
# JsonSave.add_vacancy(all_vacancies, '')


# объединить вакансии hh и sj в один общий список с платформ

add_vacancy()

# pprint(JsonSave.all_vacancies)
