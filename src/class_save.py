import json


class JsonSave:
    all_vacancies = {}

    def __init__(self):
        self.file_name = 'vacancies.json'

    @staticmethod
    def delete_file(self):
        with open(self.file_name, 'w'):
            pass
    @staticmethod
    def get_vacancies(self):
        with open(self.file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


def add_vacancy():
    with open('vacancies.json', 'a', encoding='utf-8') as json_file:
        json.dump(JsonSave.all_vacancies, json_file, indent=4, ensure_ascii=False)
