from cashdesk import Bill, BillBatch, CashDesk

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()
desk.take_money(Bill(10))
desk.take_money(batch)


print(desk.total())  # 390
desk.inspect()

# We have a total of 390$ in the desk
# We have the following count of bills, sorted in ascending order:
# 10$ bills - 2
# 20$ bills - 1
# 50$ bills - 1
# 100$ bills - 3
