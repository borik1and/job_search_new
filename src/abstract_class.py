from abc import ABC, abstractmethod


class API(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    # @abstractmethod
    # def load_jobs(self, keywords, location):
    #     pass

    @abstractmethod
    def format_vacancies(self, all_vacancies):
        pass

# class IndeedAPI(API):
#
#     def connect(self):
#         print(f"Connecting to Indeed API with API key: {self.api_key}")
#         # Здесь можно выполнить логику подключения к API сайта Indeed
#
#     def get_jobs(self, keywords, location):
#         print(f"Fetching jobs from Indeed API for keywords: {keywords}, location: {location}")
#         # Здесь можно выполнить логику получения вакансий с сайта Indeed
#
#
# class LinkedInAPI(API):
#
#     def connect(self):
#         print(f"Connecting to LinkedIn API with API key: {self.api_key}")
#         # Здесь можно выполнить логику подключения к API сайта LinkedIn
#
#     def get_jobs(self, keywords, location):
#         print(f"Fetching jobs from LinkedIn API for keywords: {keywords}, location: {location}")
#         # Здесь можно выполнить логику получения вакансий с сайта LinkedIn
#
#     def format_metod(self):
#         pass
#

# Пример использования

# indeed_api = IndeedAPI("YOUR_INDEED_API_KEY")
# linkedin_api = LinkedInAPI("YOUR_LINKEDIN_API_KEY")
#
# indeed_api.connect()
# indeed_api.get_jobs("Python Developer", "New York")
#
# linkedin_api.connect()
# linkedin_api.get_jobs("Data Scientist", "San Francisco")
