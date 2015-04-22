import unittest
from panda import Panda
from social3 import PandaSocialNetwork
from social3 import PandaAlreadyThere
from social3 import PandasAlreadyFriends


class Test_Network(unittest.TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.network.add_panda(self.ivo)

    def test_init(self):
        self.assertTrue(isinstance(self.network, PandaSocialNehtwork))

    def test_add_panda(self):
        self.assertTrue(self.ivo in self.network.pandas.keys())
        self.assertEqual(len(self.network.pandas[self.ivo]), 0)
        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.ivo)

    def test_has_panda(self):
        self.assertTrue(self.network.has_panda(self.ivo))
        self.assertFalse(self.network.has_panda(self.rado))

    def test_make_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(
            self.rado in self.network.pandas[self.ivo])
        with self.assertRaises(PandasAlreadyFriends):
            self.network.make_friends(self.ivo, self.rado)

    def test_are_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.are_friends(self.ivo, self.rado))
        self.assertFalse(self.network.are_friends(self.ivo, self.ivo))

    def test_friends_of(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertEqual(self.network.friends_of(self.ivo), [self.rado])
        bla = Panda("bla", "rado@pandamail.com", "male")
        self.assertFalse(self.network.friends_of(bla))

    def test_connection_level(self):
        # Wannabe Graph again :D
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        mimi = Panda('mimi', 'mimi@mail.bg', 'female')
        gosho = Panda('gosho', 'gosho@mail.bg', 'male')
        tony = Panda('tony', 'tony@mail.bg', 'female')
        sasho = Panda('sasho', 'sasho@mail.bg', 'male')
        pesho = Panda('pesho', 'pesho@mail.bg', 'male')
        kremena = Panda('kremena', 'kremena@mail.bg', 'female')
        sad = Panda('sad', 'sad@mail.bg', 'male')

        self.network.make_friends(ivo, rado)
        self.network.make_friends(ivo, gosho)
        self.network.make_friends(ivo, mimi)
        self.network.make_friends(rado, mimi)
        self.network.make_friends(rado, tony)
        self.network.make_friends(tony, gosho)
        self.network.make_friends(kremena, pesho)
        self.network.make_friends(kremena, tony)
        self.network.make_friends(kremena, mimi)
        self.network.make_friends(sasho, gosho)

        self.assertEqual(self.network.connection_level(ivo, rado), 1)
        self.assertEqual(self.network.connection_level(kremena, rado), 2)
        self.assertEqual(self.network.connection_level(ivo, sad), -1)
        self.assertEqual(self.network.connection_level(mimi, tony), 2)
        self.assertEqual(self.network.connection_level(pesho, gosho), 3)

    def test_are_connected(self):
        # Wannabe Graph again :D
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        mimi = Panda('mimi', 'mimi@mail.bg', 'female')
        gosho = Panda('gosho', 'gosho@mail.bg', 'male')
        tony = Panda('tony', 'tony@mail.bg', 'female')
        sad = Panda('sad', 'sad@mail.bg', 'male')
        self.network.make_friends(ivo, rado)
        self.network.make_friends(ivo, gosho)
        self.network.make_friends(ivo, mimi)
        self.network.make_friends(rado, mimi)
        self.network.make_friends(rado, tony)
        self.network.make_friends(tony, gosho)

        self.assertFalse(self.network.are_connected(ivo, sad))
        self.assertFalse(self.network.are_connected(rado, sad))
        self.assertTrue(self.network.are_connected(ivo, rado))

    def test_how_many_genders(self):
        # Wannabe Graph again :D
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Rado", "rado@pandamail.com", "male")
        mimi = Panda('mimi', 'mimi@mail.bg', 'female')
        gosho = Panda('gosho', 'gosho@mail.bg', 'male')
        tony = Panda('tony', 'tony@mail.bg', 'female')
        sasho = Panda('sasho', 'sasho@mail.bg', 'male')
        pesho = Panda('pesho', 'pesho@mail.bg', 'male')
        kremena = Panda('kremena', 'kremena@mail.bg', 'female')

        self.network.make_friends(ivo, rado)
        self.network.make_friends(ivo, gosho)
        self.network.make_friends(ivo, mimi)
        self.network.make_friends(rado, mimi)
        self.network.make_friends(rado, tony)
        self.network.make_friends(tony, gosho)
        self.network.make_friends(kremena, pesho)
        self.network.make_friends(kremena, tony)
        self.network.make_friends(kremena, mimi)
        self.network.make_friends(sasho, gosho)

        self.assertEqual(
            self.network.how_many_gender_in_network(1, rado, 'female'), 2)
        self.assertEqual(
            self.network.how_many_gender_in_network(1, rado, 'male'), 1)
        self.assertEqual(
            self.network.how_many_gender_in_network(1, rado, 'female'), 2)
        self.assertEqual(
            self.network.how_many_gender_in_network(2, rado, 'male'), 2)
        self.assertEqual(
            self.network.how_many_gender_in_network(3, kremena, 'male'), 5)

    def test_save(self):
        pass

if __name__ == '__main__':
    unittest.main()
