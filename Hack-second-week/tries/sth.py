class Panda:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def _get_buff(self):
        if self.weight < 1000:
            self.weight += 1

    def eat_bamboo(self):
        self._get_buff()
        return "Nomm nomm nomm!"

    def __str__(self):
        return "I am a panda - {}".format(self.name)

bebe = Panda('Bebe', 10, 10)
print(str(bebe))
