import collections


class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, another):
        return self.amount == another.amount

    def __hash__(self):
        return hash(self.__str__())


class BillBatch:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __total_amount(self):
        amount = 0
        for bill in self.bills:
            amount += int(bill)
        return amount

    def total(self):
        return self.__total_amount()

    def __getitem__(self, index):
        return self.bills[index]

'''     def __iter__(self):
        for bill in self.bills:
            yield bill
'''


class CashDesk:

    def __init__(self):
        self.total_amount = 0
        self.bills = {}

    def take_money(self, money):
        if isinstance(money, Bill):
            if money.amount in self.bills:
                self.bills.money += 1
            else:
                self.bills.update({money.amount: 1})
        else:
            for bill in money:
                if bill.amount in self.bills:
                    self.bills[bill.amount] += 1
                else:
                    self.bills.update({bill.amount: 1})

    def __sum_total_amount(self):
        for bill in self.bills:
            self.total_amount += int(self.bills[bill] * bill)
        return self.total_amount

    def total(self):
        return self.__sum_total_amount()

    def inspect(self):
        sorted_bills = collections.OrderedDict(sorted(self.bills.items()))
        for bill in sorted_bills:
            print('{}$ bills - {}'.format(bill, self.bills[bill]))
