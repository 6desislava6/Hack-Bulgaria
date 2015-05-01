from BigCrawler import BigCrawler
import json
from DataMaker_urls import DataMaker
from Histogram import Histogram
import matplotlib.pyplot as plt
import operator


def make_json_urls(filename):
    crawler = BigCrawler()
    url = 'http://start.bg/'
    soup_box = BigCrawler.get_soup_box(url)
    crawler.get_links(soup_box)
    # servers = BigCrawler.get_servers(links)

    for url in crawler.inner_links:
        soup_box = BigCrawler.get_soup_box(url)
        crawler.get_links(soup_box)

    with open(filename, 'w') as outfile:
        json.dump(crawler.links, outfile, indent=4)
        # json.dump(crawler.inner_links, outfile, indent=4)


def load_urls(filename):
    with open(filename) as data_file:
        return json.load(data_file)


def complete_histogram(bg_histogram, servers):
    for line in servers:
        bg_histogram.add(line['server'])


def main():
    bg_histogram = Histogram()
    db = DataMaker('mydb-servers')
    # make_json_urls('all_urls.json')
    # urls = load_urls('all_urls.json')
    # BigCrawler.get_servers(urls, db)

    servers = db.list_urls_servers()
    complete_histogram(bg_histogram, servers)

    # Making histogram
    bg_histogram_dict = bg_histogram.get_dict()
    sorted_x = sorted(bg_histogram_dict.items(), key=operator.itemgetter(1))

    keys = []
    values = []

    lenght = len(sorted_x)
    for i in range(1, 7):
        keys.append(sorted_x[lenght - i][0])
        values.append(sorted_x[lenght - i][1])

    X = list(range(len(keys)))

    plt.bar(X, values, align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig("all_sites.png")

if __name__ == '__main__':
    main()
