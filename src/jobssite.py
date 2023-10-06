from abc import ABC, abstractmethod


class JobSiteAPI(ABC):
    def __init__(self, api_key='', client_id='', client_cecret=''):
        self.api_key = api_key
        self.client_id = client_id
        self.client_cecret = client_cecret

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_jobs(self, keywords, location):
        pass


class MainJob(JobSiteAPI):
    def __init__(self, api_key='', client_id='', client_cecret=''):
        super().__init__(api_key, client_id, client_cecret)

    pass


import requests
from requests.auth import HTTPBasicAuth


class JodSearch:
    def __init__(self, keyword, location):
        self.keyword = keyword
        self.location = location

    def superjob_search(self):
        api_token = KEY_API
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

            # Вывод результатов
            for vacancy in data['objects']:
                print(f"Название вакансии: {vacancy['profession']}")

                # Проверка наличия поля 'payment'
                if 'payment' in vacancy:
                    print(f"Зарплата: {vacancy['payment']}")
                else:
                    print("Зарплата не указана")

                print(f"Город: {vacancy['town']['title']}")
                print(f"Ссылка: {vacancy['link']}")
                print()

        except requests.exceptions.HTTPError as e:
            print(f"Произошла ошибка при запросе к API: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def hh_api_search(self):

        # данные аутентификации
        client_id = 'J53D8HKIPP1HV1F82IPVO5QF97NVO901RCQ72ID6UAFV6QV85FVGNL131O2NH2GI'
        client_secret = 'H4289AFGCNFTEK9ATRTV9Q130US9VA7Q8LNE1TRQQ5GNJV0OBTBGR40SEKQOQ4IU'

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

            if response.status_code == 200:
                vacancies = response.json()
                for vacancy in vacancies['items']:
                    print(f"Название вакансии: {vacancy['name']}")

                    # Проверяем наличие информации о зарплате
                    if vacancy['salary']:
                        salary_range = (f"{vacancy['salary']['from']}"
                                        f" - {vacancy['salary']['to']} {vacancy['salary']['currency']}")
                    else:
                        salary_range = "Информация о зарплате отсутствует"

                    print(f"Зарплата: {salary_range}")
                    print(f"Ссылка: {vacancy['alternate_url']}")
                    print("\n")
            else:
                print(f'Ошибка при выполнении запроса к API: {response.status_code}')
        else:
            print(f'Ошибка при получении токена доступа: {response.status_code}')
