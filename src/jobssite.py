import json
from abc import ABC, abstractmethod
import requests
from requests.auth import HTTPBasicAuth
import os


class JobSiteAPI(ABC):
    def __init__(self):
        self.api_token = os.getenv('API_TOKEN')
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_jobs(self):
        pass


def save_to_json(file):
    with open('src/job.json', 'w') as j_f:
        json.dump(file, j_f)


class JobSearch(JobSiteAPI):
    def __init__(self, keyword, location):
        super().__init__()
        self.keyword = keyword
        self.location = location

    def connect(self):
        # Реализуйте настройку соединения здесь (например, получение токена доступа)
        pass

    def get_jobs(self):
        pass

    @property
    def superjob_search(self):
        api_token = self.api_token
        # URL для доступа к API superjob.ru
        url = 'https://api.superjob.ru/2.0/vacancies/'
        # Параметры запроса
        params = {
            'keyword': self.keyword,
            'town': self.location,
            'page': 1,  # Номер страницы результатов (начиная с 1)
        }
        # Заголовки запроса с вашим API-токеном
        headers = {
            'X-Api-App-Id': api_token,
        }
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()  # Проверка на наличие ошибок
            data = response.json()  # Преобразование ответа в формат JSON
            return data  # Возвращаем результат

        except requests.exceptions.HTTPError as e:
            print(f"Произошла ошибка при запросе к API: {e}")
            return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None

    @property
    def hh_api_search(self):

        # данные аутентификации
        client_id = 'J53D8HKIPP1HV1F82IPVO5QF97NVO901RCQ72ID6UAFV6QV85FVGNL131O2NH2GI'
        client_secret = 'H4289AFGCNFTEK9ATRTV9Q130US9VA7Q8LNE1TRQQ5GNJV0OBTBGR40SEKQOQ4IU'
        # client_id = self.client_id
        # client_secret = self.client_secret

        # Запрос на получение токена доступа (токена OAuth2)
        token_url = 'https://hh.ru/oauth/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Выполняем запрос на получение токена
        response = requests.post(token_url, data=data, auth=HTTPBasicAuth(client_id, client_secret))

        if response.status_code == 200:
            access_token = response.json().get('access_token')

            # Пример запроса к API с использованием токена доступа
            api_url = 'https://api.hh.ru/vacancies'
            params = {
                'text': 'Python Developer',  # Ваш запрос по ключевым словам
                'area': 1,  # Код региона (например, 1 для Москвы)
                'per_page': 100  # Количество результатов на странице
            }

            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            response = requests.get(api_url, params=params, headers=headers)
            vacancies = response.json()
            return vacancies

        else:
            print(f'Ошибка при получении токена доступа: {response.status_code}')


# Создание экземпляра класса JobSearch и выполнение поиска
job_search = JobSearch('python', 'Москва')
super_job_data = job_search.superjob_search
hh_data = job_search.hh_api_search

# Теперь вы можете обработать результаты поиска, например, вывести их на экран
if super_job_data:
    for vacancy in super_job_data['objects']:
        print(f"Название вакансии: {vacancy['profession']}")
        # print(vacancy['url'])
        try:
            print(f'Зарплата: {vacancy["salary"][0]["from"]} - '
                  f'{vacancy["salary"][0]["to"]} {vacancy["salary"][0]["currency"]}')
        except KeyError:
            print("Отсутствуют данные")

if hh_data:
    for vacancy in hh_data['items']:
        print(f"Название вакансии: {vacancy['name']}")
        print(vacancy['url'])
