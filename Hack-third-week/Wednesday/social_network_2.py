class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = {}

    def add_panda(self, panda):
        if hash(panda) in self.pandas:
            raise PandaAlreadyThere
        else:
            self.pandas[hash(panda)] = []

    def has_panda(self, panda):
        return hash(panda) in self.pandas

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if panda2 in self.pandas[hash(panda1)]:
            raise PandasAlreadyFriends
        else:
            self.pandas[hash(panda1)].append(panda2)
            self.pandas[hash(panda2)].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda2 in self.pandas[hash(panda1)]:
            return True
        else:
            return False

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.pandas[hash(panda)]

    def connection_level(self, panda1, panda2):
        # Wannnabe Dijkstra
        ways = {}
        pandas_to_be_visited = []
        visited_pandas = [hash(panda1)]
        # All others - making them infinity
        for panda_hash in self.pandas:
            if panda_hash != hash(panda1):
                ways.update({panda_hash: float('inf')})
                pandas_to_be_visited.append(panda_hash)
        # The friends of the first panda
        for panda in self.friends_of(panda1):
            ways[hash(panda)] = 1

        while len(pandas_to_be_visited) != 0:
            bestPanda = get_key_with_min_val(ways, pandas_to_be_visited)
            bestValue = ways[bestPanda] + 1
            pandas_to_be_visited.remove(bestPanda)
            visited_pandas.append(bestPanda)

            # the friends of out 'best' panda - the one with min value
            for panda in self.pandas[bestPanda]:
                hash_panda = hash(panda)
                if hash_panda not in visited_pandas:
                    if ways[hash_panda] > bestValue:
                        ways[hash_panda] = bestValue

        if hash(panda2) not in ways:
            return -1
        else:
            return ways[hash(panda2)]

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


# Thus I find the not visited panda with smalletst value!
def get_key_with_min_val(ways, pandas_to_be_visited):
    bestkey = None
    bestValue = float('inf')
    for key in ways.keys():
        if ways[key] < bestValue and key in pandas_to_be_visited:
            bestValue = ways[key]
            bestkey = key
    return bestkey
