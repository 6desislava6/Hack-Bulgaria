import requests


class Person:
    def __init__(self, person_info_url):
        person_info = requests.get(person_info_url).json()
        self.login = person_info['login']
        self.url = person_info['url']
        self.following_url = 'https://api.github.com/users/{}?client_id=6171fe8c1c25927a0eac&client_secret=e4c5be73c2caf7d04051266d686cc6dd98a7d913'.format(self.login+'/following')
        self.followers_url = 'https://api.github.com/users/{}?client_id=6171fe8c1c25927a0eac&client_secret=e4c5be73c2caf7d04051266d686cc6dd98a7d913'.format(self.login+'/followers')
        self.followers_json = requests.get(self.followers_url).json()
        self.following_json = requests.get(self.following_url).json()
        self.followers = []
        self.following = []

    def __hash__(self):
        return hash(self.url)

    def __repr__(self):
        return self.login

    def __str__(self):
        return self.login

    def __eq__(self, other):
        return self.login == other.login

    def make_followers_or_following(self, dict_of_followers):
        follow_people = []
        for follower in dict_of_followers:
            url = 'https://api.github.com/users/{}?client_id=6171fe8c1c25927a0eac&client_secret=e4c5be73c2caf7d04051266d686cc6dd98a7d913'.format(follower['login'])
            p = Person(url)
            follow_people.append(p)
        return follow_people

    def make_followers(self):
        self.followers = self.make_followers_or_following(self.followers_json)

    def make_following(self):
        self.following = self.make_followers_or_following(self.following_json)

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following
