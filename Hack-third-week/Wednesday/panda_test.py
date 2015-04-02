import unittest
from panda import Panda


class Test_Panda(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_init(self):
        self.assertTrue(isinstance(self.ivo, Panda))
        self.assertEqual(self.ivo.get_name(), self.ivo.name)
        self.assertEqual(self.ivo.get_email(), self.ivo.email)
        self.assertEqual(self.ivo.get_gender(), self.ivo.gender)
        self.assertEqual(self.ivo.check_isMale(), True)
        self.assertEqual(self.ivo.check_isFemale(), False)
        # email exception
        with self.assertRaises(ValueError):
            ivo = Panda("Ivo", "BLAAAAA", "male")

    def test_eq(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.assertFalse(self.ivo == rado)

    def test_hashed(self):
        self.assertTrue(isinstance(self.ivo.__hash__(), int))

    def test_get_name(self):
        self.assertEqual(self.ivo.get_name(), self.ivo.name)

    def test_get_email(self):
        self.assertEqual(self.ivo.get_email(), self.ivo.email)

    def test_get_gender(self):
        self.assertEqual(self.ivo.get_gender(), self.ivo.gender)

    def test_check_isMale(self):
        self.assertTrue(self.ivo.check_isMale())

    def test_check_isFemale(self):
        self.assertFalse(self.ivo.check_isFemale())

if __name__ == '__main__':
    unittest.main()
