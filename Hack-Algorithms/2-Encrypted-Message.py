FINAL_MESSAGE = 'Your original message is: {}'


def reverse_from_middle(string):
    middle = len(string) // 2
    if len(string) % 2 == 1:
        return string[middle:] + string[middle + 1] + string[:middle]
    return string[middle:] + string[:middle]


def get_numbers_from_string(string):
    #  Returns the length of the alphabet, the length of the key
    # and the alphabet + encrypted+key in the same order
    data = string.split('~')
    return {'length_alpha': int(data[0]), 'length_key': int(data[2]), 'alpha_message_key': data[1]}


def get_data_from_string(length_alpha, length_key, alphabet_message_key):
    end_index_alphabet = length_alpha
    begin_index_key = - length_key
    alphabet = alphabet_message_key[:end_index_alphabet]
    key = alphabet_message_key[begin_index_key:]
    message = alphabet_message_key[end_index_alphabet:begin_index_key]
    return {'alphabet': alphabet, 'key': key, 'message': message}


def get_indices(alphabet, string):
    return [alphabet.index(x) for x in string]


def find_original_message(indices_encrypted, indices_key, alphabet):
    indices_key_repeated = []
    resulting_indices = []
    length_key = len(indices_key)

    # repeating the key if neccessary
    for x in range(len(indices_encrypted)):
        indices_key_repeated.append(indices_key[x % length_key])

    # finding out what the true message was
    for x in range(len(indices_encrypted)):
        element = indices_encrypted[x] - indices_key_repeated[x]
        # if it's negative, we know we've taken the remainder of the devision
        # by the length of the alphaber
        if element < 0:
            element += len(alphabet)
        resulting_indices.append(element)
    return ''.join([alphabet[x] for x in resulting_indices])


def main():
    input_string = input('Type encrypted message here> ')

    # Reversing the message
    input_string = reverse_from_middle(input_string)

    # Finding out the numbers and alphabet+ message+ key
    numbers_string = get_numbers_from_string(input_string)
    length_alpha = numbers_string['length_alpha']
    length_key = numbers_string['length_key']
    alphabet_message_key = numbers_string['alpha_message_key']

    # Finding out what's the alphabet, key and message
    data_string = get_data_from_string(
        length_alpha, length_key, alphabet_message_key)
    alphabet = data_string['alphabet']
    key = data_string['key']
    message_encrypted = data_string['message']

    # Final steps
    indices_encrypted = get_indices(alphabet, message_encrypted)
    indices_key = get_indices(alphabet, key)
    print(FINAL_MESSAGE.format(
        find_original_message(indices_encrypted, indices_key, alphabet)))

if __name__ == '__main__':
    main()
