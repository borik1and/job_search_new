import json



class JsonSave:
    all_vacancies = {}

    def delete_file(self, file_name):
        with open(file_name, 'w'):
            pass

    def get_vacancies(self, file_name='vacancy.json'):
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


def add_vacancy():
    with open('vacancies.json', 'a', encoding='utf-8') as json_file:
        json.dump(JsonSave.all_vacancies, json_file, indent=4, ensure_ascii=False)