def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


def is_credit_card_valid(number):
    number = str(number)
    is_valid = len(number) % 2 == 1
    if not is_valid:
        return False
    numbers = [int(x) for x in number]
    sum = 0
    index = 0
    for num in numbers:
        if index % 2 == 1:
            sum += sum_of_digits(num * 2)
        else:
            sum += num
        index += 1
    if sum % 10 != 0:
        is_valid = False
    return is_valid

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))