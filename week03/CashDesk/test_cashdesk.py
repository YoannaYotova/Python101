import unittest
from cashdesk import Bill, BatchBill, CashDesk


class TestBill(unittest.TestCase):
    def test_with_valid_amount(self):
        Bill.money_holder = {}
        a = Bill(10)

        self.assertEqual(a.amount, 10)

    def test_the_amount_is_negative_number_and_rase_value_error(self):
        exc = None

        try:
            Bill(-10)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Amount cannot be negative')

    def test_type_the_amount_is_not_int_and_raise_type_error(self):
        exc = None

        try:
            Bill(2.5)
        except TypeError as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Type of amount should be int')

    def test_representions_as_string(self):
        Bill.money_holder = {}
        a = Bill(10)

        self.assertEqual(str(a), "A 10$ bill")

    def test_converting_the_object_into_the_amount_with_int(self):
        Bill.money_holder = {}
        a = Bill(10)

        self.assertEqual(int(a), 10)

    def test_two_bills_are_equel_if_they_have_same_amount(self):
        Bill.money_holder = {}
        a = Bill(100)
        b = Bill(100)

        self.assertTrue(a == b, 'Bills are not equal')

    def test_hashing_how_many_bills_are_in_the_money_holder(self):
        Bill.money_holder = {}
        a = Bill(20)
        c = Bill(20)

        self.assertEqual(Bill.money_holder[str(a)], 2)


class TestBatchBill(unittest.TestCase):
    def test_getting_item_from_list_of_bills(self):
        Bill.money_holder = {}
        a = Bill(10)
        b = Bill(20)

        batch = BatchBill([a, b])

        self.assertEqual(batch[0], a)

    def test_counting_the_numbers_of_bills_in_the_batch(self):
        Bill.money_holder = {}
        a = Bill(10)
        b = Bill(20)

        batch = BatchBill([a, b])

        self.assertEqual(len(batch), 2)

    def test_total_amount_of_all_bills_in_the_batch(self):
        Bill.money_holder = {}
        a = Bill(10)
        b = Bill(20)

        batch = BatchBill([a, b])

        self.assertEqual(batch.total(), 30)


class TestCashDesk(unittest.TestCase):

    def test_total_amount_of_money_in_the_desk_with_bills(self):
        Bill.money_holder = {}

        a = Bill(10)
        b = Bill(20)
        c = Bill(30)

        desk = CashDesk()

        desk.take_money(a)
        desk.take_money(b)
        desk.take_money(c)

        total = desk.total()

        self.assertEqual(total, 60)

    def test_total_amount_of_money_in_the_desk_with_batches(self):
        Bill.money_holder = {}

        a = Bill(10)
        b = Bill(20)
        c = Bill(40)

        batch = BatchBill([a, b, c])

        desk1 = CashDesk()

        desk1.take_money(batch)

        total = desk1.total()

        self.assertEqual(total, 70)

    def test_total_amount_of_money_in_the_desk_with_bills_and_batches(self):
        Bill.money_holder = {}

        a = Bill(10)
        b = Bill(20)
        c = Bill(40)

        batch = BatchBill([a, b, c])
        desk = CashDesk()

        desk.take_money(batch)
        desk.take_money(a)

        total = desk.total()

        self.assertEqual(total, 80)


if __name__ == '__main__':
    unittest.main()
