from operator import attrgetter


class Bill:
    money_holder = {}

    def __init__(self, amount):
        if amount < 0:
            raise ValueError('Amount cannot be negative')
        elif type(amount) != int:
            raise TypeError('Type of amount should be int')
        else:
            self.amount = amount

            if str(self) in self.money_holder:
                self.money_holder[str(self)] += 1
            else:
                self.money_holder[str(self)] = 1

    def __str__(self):
        return f'A {self.amount}$ bill'

    def __repr__(self):
        return f'A {self.amount}$ bill'

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return self.money_holder[str(self)]


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        count_of_bills = 0
        for bill in self.bills:
            count_of_bills += 1

        return count_of_bills

    def total(self):
        count_of_amount = 0
        for bill in self.bills:
            count_of_amount += bill.amount

        return count_of_amount


class CashDesk:

    def __init__(self):
        self.money_of_bills = []

    def take_money(self, money):
        self.money = money

        # all the bills append to the list of the class
        if type(self.money) is Bill:
            self.money_of_bills.append(self.money)
        else:
            for i in range(len(money)):
                self.money_of_bills.append(self.money[i])

    def total(self):
        count = 0
        for bill in self.money_of_bills:
            count += int(bill)
        return count

    def inspect(self):
        # sort by amount
        self.money_of_bills = sorted(self.money_of_bills, key=attrgetter('amount'))

        print(f'We have a total of {self.total()}$ in the desk')
        print("We have the following count of bills, sorted in ascending order:")

        for i in range(len(self.money_of_bills) - 1):
            # check for repeating bills
            if self.money_of_bills[i] != self.money_of_bills[i + 1]:
                print(f'{self.money_of_bills[i].amount}$ bills - {Bill.money_holder[str(self.money_of_bills[i])]}')

        # print the last one
        last_bill_index = len(self.money_of_bills) - 1
        print(f'{self.money_of_bills[last_bill_index].amount}$ bills - {Bill.money_holder[str(self.money_of_bills[last_bill_index])]}')


def main():
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total())
    desk.inspect()


if __name__ == '__main__':
    main()
