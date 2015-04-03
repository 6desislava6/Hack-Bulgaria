import json
sth = {'blaa': [1, 2, 3], 'shaaaa': [4, 5, 6]}
with open('output2.txt', 'w') as outfile:
            json.dump(sth, outfile)
