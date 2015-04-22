from Net import Net
from Person_in_Github import Person


def main():
    str_template = 'https://api.github.com/users/{}?client_id=6171fe8c1c25927a0eac&client_secret=e4c5be73c2caf7d04051266d686cc6dd98a7d913'
    person_desi = Person(str_template.format('6desislava6'))
    person_kremena = Person(str_template.format('KremenaVasileva'))
    person_peter = Person(str_template.format('peter359'))
    net = Net()
    net.build_network_for(person_desi, 2)
    print('Do I follow?')
    print(net.do_you_follow(person_kremena))
    print('Does she follow me?')
    print(net.does_he_she_follows(person_kremena))
    print(net.who_follows_you_back())
    print('Do I follow Peter?')
    print(net.do_you_follow_indirectly(person_peter))

if __name__ == '__main__':
    main()
