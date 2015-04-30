import requests
from bs4 import BeautifulSoup
import re
import json


class Crawler:

    @staticmethod
    def get_soup_box(url):
        site_response = requests.get(url)
        soup_all = BeautifulSoup(site_response.text)

        box_with_links = soup_all.find(id='boxes')
        return BeautifulSoup(str(box_with_links))

    @staticmethod
    def get_links(soup_box):
        links = []

        for link in soup_box.find_all('a'):
            link = str(link.get('href'))
            if 'link.php?id=' in link:
                links.append('http://register.start.bg/' + link)
        return links

    @staticmethod
    def get_servers(links):
        servers = []
        invalid_links = 0
        for link in links:
            try:
                r = requests.head(link, timeout=1, allow_redirects=True)
                server_type = r.headers['server']
                m = re.search(r"\w+(-)*\w+", server_type)
                server = m.group()
                servers.append(server)
            except:
                invalid_links += 1
        return servers

    @staticmethod
    def save_data_in_file(filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
