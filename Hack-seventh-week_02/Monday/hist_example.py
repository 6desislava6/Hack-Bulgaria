from Histogram import Histogram
import matplotlib.pyplot as plt
from Crawler import Crawler
# import json
import operator


def main():
    bg_histogram = Histogram()

    url = 'http://register.start.bg/'
    soup_box = Crawler.get_soup_box(url)
    links = Crawler.get_links(soup_box)
    servers = Crawler.get_servers(links)

    Crawler.save_data_in_file('servers.json', servers)
    Crawler.save_data_in_file('links.json', links)

    # with open('servers.json') as data_file:
    #    servers = json.load(data_file)

    for server in servers:
        bg_histogram.add(server)

    Crawler.save_data_in_file('histogram.json', bg_histogram.get_dict())

    bg_histogram_dict = bg_histogram.get_dict()

    sorted_x = sorted(bg_histogram_dict.items(), key=operator.itemgetter(1))

    keys = []
    values = []

    lenght = len(sorted_x)
    for i in range(1, 7):
        keys.append(sorted_x[lenght - i][0])
        values.append(sorted_x[lenght - i][1])

    # keys = list(bg_histogram.keys())
    # values = list(bg_histogram.values())

    X = list(range(len(keys)))

    plt.bar(X, values, align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig("histogram_not_all.png")

if __name__ == '__main__':
    main()
