import requests
import json


class GetResources:
    def __init__(self):
        self.API_URL = 'URL GOES HERE'
        self.KEY = 'KEY GOES HERE'

        self.ddlinks = {}
        self.are_pulled = False

    def init_download_links(self):
        self.are_pulled = True
        try:
            self.extract_data()
        except requests.exceptions.ConnectionError:
            self.are_pulled = False

    def extract_data(self):
        headers = {
            'api-key': self.KEY,
            'user-agent': 'software-downloader.desktop'
        }

        data = requests.get(self.API_URL, headers=headers).text
        self.ddlinks = json.loads(data)['results']
