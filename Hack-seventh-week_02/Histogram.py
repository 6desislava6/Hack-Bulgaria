class Histogram:

    def __init__(self):
        self.__servers_type = {}

    def add(self, type_server):
        if type_server in self.__servers_type:
            self.__servers_type[type_server] += 1
        else:
            self.__servers_type.update({type_server: 1})

    def count(self, type_server):
        return self.__servers_type[type_server]

    def items(self):
        pass

    def get_dict(self):
        return self.__servers_type

    def keys(self):
        return self.__servers_type.keys()

    def values(self):
        return self.__servers_type.values()
