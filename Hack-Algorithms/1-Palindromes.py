def check_is_palindrome(word):
    return word == word[::-1]


def rotations_of_word(word):
    rotations = []
    for x in range(1, len(word) + 1):
        rotations.append(word[x:] + word[:x])
    return rotations


def main():
    input_string = input('input here> ')
    rotations = rotations_of_word(input_string)
    palindromes = list(filter(lambda x: check_is_palindrome(x), rotations))
    if len(palindromes) == 0:
        print('NONE')
    else:
        for string in rotations:
            print(string)

if __name__ == '__main__':
    main()
