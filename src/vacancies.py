import json
from src.class_save import JsonSave


class Vacancy:
    all = []

    def __init__(self, name, url, salary, exp):
        self.name = name
        self.url = url
        self.salary = salary
        self.exp = exp

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.url}', '{self.salary}', '{self.exp}')"

    def __str__(self):
        return (f"{self.__class__.__name__}('Професия: {self.name}', 'Страничка оъявления: {self.url}',"
                f" 'Зарплата: {self.salary}', 'Опыт: {self.exp}')")

    def __ge__(self, other):
        # Сравнение по зарплате для текущей вакансии и другой вакансии (other)
        return self.salary >= other.salary

    def __lt__(self, other):
        # Сравнение по зарплате для текущей вакансии и другой вакансии (other)
        return self.salary < other.salary

    def __eq__(self, other):
        # Сравнение по зарплате для текущей вакансии и другой вакансии (other)
        return self.salary == other.salary

    @staticmethod
    def instantiate_from_json():
        data = JsonSave.get_vacancies

        for vacancy in data['vacancies']:
            Vacancy.all.append(Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy['exp']))
            return Vacancy.all

    def sort_vacancy(self):
        pass

# def compare_vacancies_by_salary():
#     # Функция для сравнения вакансий по зарплате
#     data = JsonSave.get_vacancies  # Вызываем функцию, чтобы получить данные
#     vacancies = [Vacancy(v['name'], v['url'], v['salary'], v['experience']) for v in data]
#
#     # Сортировка вакансий по зарплате (по убыванию)
#     sorted_vacancies = sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)
#     return sorted_vacancies
