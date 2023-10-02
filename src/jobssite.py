# from abc import ABC, abstractmethod
#
#
# class JobSiteAPI(ABC):
#     def __init__(self, api_key):
#         self.api_key = api_key
#
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def get_jobs(self, keywords, location):
#         pass
#
#
# class MainJob(JobSiteAPI):
#     def __init__(self, api_key):
#         super().__init__(api_key)
#
#     pass


import requests




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
