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
    def __init__(self, keyword, area):
        self.keyword = keyword
        self.area = area
