class BankAccount:

    def __init__(self, name, amount, currency):
        self.amount = amount
        self.name = name
        self.currency = currency
        self.account_history = ['Account was created']

    def history(self):
        return self.account_history

    def balance(self):
        current_history = 'Balance check -> ' + str(self.amount) + self.currency
        self.account_history.append(current_history)
        return self.amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.amount += amount
            current_history = 'Deposited ' +str(amount) + self.currency
            self.account_history.append(current_history)

    def withdraw(self, amount):
        if amount >= self.amount:
            current_history = 'Withdraw for {}{} failed.'.format(
                amount, self.currency)
            self.account_history.append(current_history)
            return False
        else:
            self.amount -= amount
            current_history = str(amount) + self.currency + \
                ' was withdrawed'
            self.account_history.append(current_history)
            return True

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.amount, self.currency)

    def __int__(self):
        current_history = '__int__ check -> ' + str(self.amount) + self.currency
        self.account_history.append(current_history)
        return self.amount

    def transfer_to(self, other, money):
        if self.currency != other.currency or self.amount < money:
            return False
        else:
            self.amount -= money
            trueString_Rado = 'Transfer to {} for {}{}'.format(
                other.name, money, self.currency)
            trueString_Ivo = 'Transer from {} for {}{}'.format(
                self.name, money, other.currency)
            other.amount += money
            self.account_history.append(trueString_Rado)
            other.account_history.append(trueString_Ivo)
            return True

def main():
    rado = BankAccount('Rado', 1000, '$')
    ivo = BankAccount('Ivo', 1000, '$')
    rado.transfer_to(ivo, 500)
    print(rado.history())

if __name__ == '__main__':
    main()
