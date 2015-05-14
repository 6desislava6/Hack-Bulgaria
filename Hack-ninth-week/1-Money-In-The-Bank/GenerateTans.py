import hashlib
import random


class GenerateTans:
    @staticmethod
    def generate_tans(count):
        tans = []
        for x in range(count):
            rand = random.randint(1000000, 10000000)
            hash_object = hashlib.sha1(bytearray(rand))
            hex_dig = hash_object.hexdigest()
            tans.append(hex_dig)
        return tans

