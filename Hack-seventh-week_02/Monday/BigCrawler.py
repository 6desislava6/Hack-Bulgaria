import requests
from bs4 import BeautifulSoup
import re
import json
from DataMaker_urls import DataMaker


class BigCrawler:

    SITE = 'http://www.start.bg/'

    def __init__(self):
        self.inner_links = []
        self.links = []

    @staticmethod
    def get_soup_box(url):
        site_response = requests.get(url, timeout=1, allow_redirects=True)
        soup_all = BeautifulSoup(site_response.text)
        return soup_all

    def get_links(self, soup_box):
        for link in soup_box.find_all('a'):
            link = str(link.get('href'))
            isNotSubstring = 'javascript' not in link and 'None' not in link and '#top' not in link and not link.startswith(
                '#')
            if isNotSubstring:
                if 'start.bg' in link:
                    self.inner_links.append(link)
                elif 'link.php?' in link or link.startswith('/'):
                    self.links.append(BigCrawler.SITE + link)

        self.links = list(set(self.links))
        self.inner_links = list(set(self.inner_links))
        return [self.links, self.inner_links]

    @staticmethod
    def get_servers(links, db):
        invalid_links = 0
        for link in links:
            try:
                r = requests.head(link, timeout=1, allow_redirects=True)
                server_type = r.headers['server']
                m = re.search(r"\w+(-)*\w+", server_type)
                server = m.group()
                db.add_server(link, server)
            except:
                invalid_links += 1

    @staticmethod
    def save_data_in_file(filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
