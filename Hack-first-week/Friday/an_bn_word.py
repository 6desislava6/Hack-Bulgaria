def is_an_bn(word):
    count = 0
    isanbn = True
    for symbol in word:
        if symbol == 'a':
            count += 1
        else:
            break
    isanbn = word[count:] == 'b'*count
    print(isanbn)

is_an_bn("aaabbb")
is_an_bn("aaabb")
is_an_bn("aaaaabbbbb")
is_an_bn("rado")
is_an_bn("")
