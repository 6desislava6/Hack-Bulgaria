import json
from panda import Panda


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = {}

    def add_panda(self, panda):
        if panda in self.pandas:
            raise PandaAlreadyThere
        else:
            self.pandas[panda] = []

    def has_panda(self, panda):
        return panda in self.pandas

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if panda2 in self.pandas[panda1]:
            raise PandasAlreadyFriends
        else:
            self.pandas[panda1].append(panda2)
            self.pandas[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda2 in self.pandas[panda1]:
            return True
        else:
            return False

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.pandas[panda]

    def connection_level(self, panda1, panda2):
        # Wannnabe Dijkstra
        ways = {}
        pandas_to_be_visited = []
        visited_pandas = [panda1]
        # All others - making them infinity
        for panda_hash in self.pandas:
            if panda_hash != panda1:
                ways.update({panda_hash: float('inf')})
                pandas_to_be_visited.append(panda_hash)
        # The friends of the first panda
        for panda in self.friends_of(panda1):
            ways[panda] = 1

        while len(pandas_to_be_visited) != 0:
            bestPanda = get_key_with_min_val(ways, pandas_to_be_visited)
            bestValue = ways[bestPanda] + 1
            pandas_to_be_visited.remove(bestPanda)
            visited_pandas.append(bestPanda)

            # the friends of out 'best' panda - the one with min value
            for panda in self.pandas[bestPanda]:
                hash_panda = panda
                if hash_panda not in visited_pandas:
                    if ways[hash_panda] > bestValue:
                        ways[hash_panda] = bestValue

        if panda2 not in ways:
            return -1
        else:
            return ways[panda2]

    def are_connected(self, panda1, panda2):
        isConnection = self.connection_level(panda1, panda2) != -1
        return isConnection

    def how_many_gender_in_network(self, level, panda, gender):
        discovered = []
        to_be_visited = [panda]
        genders_levels = {}
        discovered.append(panda)

        # Breadth-first-search counting all pandas from 'gender' gender
        while len(to_be_visited) > 0:
            current_panda = to_be_visited[0]
            to_be_visited = to_be_visited[1:]
            discovered.append(current_panda)
            for friend_panda in self.friends_of(current_panda):
                if friend_panda not in discovered:
                    to_be_visited.append(friend_panda)
                    discovered.append(friend_panda)
                    if friend_panda.get_gender() == gender:
                        connection = self.connection_level(
                            panda, friend_panda)
                        if connection in genders_levels:
                            genders_levels[connection] += 1
                        else:
                            genders_levels.update({connection: 1})
        # I have found for all pandas, connected to 'panda',
        # of gender 'gender' their connection level.
        # I will sum all, which have connection level <= 'level'
        count = 0
        for i in range(1, level + 1):
            count += genders_levels[i]
        return count

    def save(self, file_name):
        with open(file_name, 'w') as outfile:
            json.dump(self.remap_keys(), outfile)

    def load(self, file_name):
        with open(file_name, 'r') as infile:
            self.pandas = json.loads(infile.read(), object_hook=object_decoder)

# Thus I find the not visited panda with smalletst value!


def get_key_with_min_val(ways, pandas_to_be_visited):
    bestkey = None
    bestValue = float('inf')
    for key in ways.keys():
        if ways[key] < bestValue and key in pandas_to_be_visited:
            bestValue = ways[key]
            bestkey = key
    return bestkey


def object_decoder(obj):
    network = {}
    for panda in obj:
        current_panda = eval(panda)
        friends = [eval(friend_panda) for friend_panda in obj[panda]]
        network.update({current_panda: friends})
    return network

# No tests this time :D


def main():
    filename = 'output.txt'

    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    mimi = Panda('mimi', 'mimi@mail.bg', 'female')
    gosho = Panda('gosho', 'gosho@mail.bg', 'male')
    tony = Panda('tony', 'tony@mail.bg', 'female')
    sasho = Panda('sasho', 'sasho@mail.bg', 'male')
    pesho = Panda('pesho', 'pesho@mail.bg', 'male')
    kremena = Panda('kremena', 'kremena@mail.bg', 'female')

    network.make_friends(ivo, rado)
    network.make_friends(ivo, gosho)
    network.make_friends(ivo, mimi)
    network.make_friends(rado, mimi)
    network.make_friends(rado, tony)
    network.make_friends(tony, gosho)
    network.make_friends(kremena, pesho)
    network.make_friends(kremena, tony)
    network.make_friends(kremena, mimi)
    network.make_friends(sasho, gosho)

    network.save(filename)
    network1 = PandaSocialNetwork()
    network1.load(filename)
    print(network1.how_many_gender_in_network(3, kremena, 'male'))


if __name__ == '__main__':
    main()
