from cashdesk import Bill

a = Bill(10)
b = Bill(5)
c = Bill(10)

int(a) == 10
str(a) == "A 10$ bill"
print(a)  # A 10$ bill

a == b  # False
a == c  # True

money_holder = {}

money_holder[a] = 1  # We have one 10% bill

if c in money_holder:
    money_holder[c] += 1

print(money_holder)  # { "A 10$ bill": 2 }
