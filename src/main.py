import os
from src.class_save import JsonSave, add_vacancy
from src.class_api import HH_API, SJ_API
from src.vacancies import Vacancy

# стираем фаил json из пребедущего цикла если есть
JsonSave.delete_file()

print()
print('Ести не указать ключевых слов, то выведуться все возможные вакании без фильтрации.')
keyword = input('Введите ключевые слова для фильтрации вакансий: ')
print()
print(" '1' - hh.ru\n '2' - superjob.ru\n '3' - на обоих платформах\n")
set_platform = input('Выберите платформу для поиска вакансий: ')
print()
print('если не указать количество вакансий в ТОПЕ, будет выведено первых 20 вакансий.')
numbers_of_vacancies_top = input('Укажите количество выводимых вакансий ТОП:  ')

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
    print('Ваш выбор искать везде')
    JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies'] + sj_vacancies['vacancies']
else:
    print('Ваш выбор не опознан, ищем везде.')
    JsonSave.all_vacancies['vacancies'] = hh_vacancies['vacancies'] + sj_vacancies['vacancies']

print()
# сохраняем в файл json
add_vacancy()
Vacancy.compare_vacancies_by_salary()
vac = Vacancy.print_vacancies(numbers_of_vacancies_top)
print(vac)
# sorted_vacancies = compare_vacancies_by_salary()
# pprint(sorted_vacancies)
# Вывод отсортированных вакансий
# for vacancy in sorted_vacancies:
#     print(f"Наименование: {vacancy.name}, Зарплата: {vacancy.salary}")


# удалить временный файл с данными
# erase = input('Хотите удалить временный файл с данными? да или нет?: ')
# if erase == 'да' or erase == 'yes':
#     if os.path.exists('vacancies.json'):
#         os.remove('vacancies.json')
# else:
#     pass
# pprint(JsonSave.all_vacancies)
