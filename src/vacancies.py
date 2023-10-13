import json


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


    def instantiate_from_json(self, file_name='vacancy.json'):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)

        for vacancy in data['vacancies']:
            Vacancy.all.append(Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy['exp']))
            return Vacancy.all

    def sort_vacancy(self):
        pass
