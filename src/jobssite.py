from abc import ABC, abstractmethod


class JobSiteAPI(ABC):
    def __init__(self, api_key):
        self.api_key = api_key

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_jobs(self, keywords, location):
        pass


class MainJob:
    pass
