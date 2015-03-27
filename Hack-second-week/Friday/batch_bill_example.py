from cashdesk import Bill, BillBatch

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)

print(batch.total())
# A 10$ bill
# A 20$ bill
# A 50$ bill
# A 100$ bill
