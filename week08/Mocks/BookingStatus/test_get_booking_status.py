import unittest
from unittest.mock import Mock, patch
from get_booking_status import get_booking_status
from datetime import datetime


class TestGetBookingStatus(unittest.TestCase):
    def test_get_booking_status_if_it_is_cancelled_returns_message_cancelled(self):
        booking = Mock(cancelled=True)
        res = get_booking_status(booking)

        self.assertEqual(res, 'Cancelled')

    @patch('get_booking_status.datetime')
    def test_get_booking_status_if_every_condition_is_false_returns_message_waiting_taxes(self, datetime_mock):
        booking = Mock(cancelled=False, start=datetime(year=2020, month=4, day=21))
        booking.is_fully_paid.return_value = False
        datetime_mock.now.return_value = datetime(year=2020, month=4, day=23)

        res = get_booking_status(booking)

        self.assertEqual(res, 'Waiting taxes')

    def test_get_booking_status_if_it_is_fully_paid_returns_message_paid(self):
        booking = Mock(cancelled=False)
        booking.is_fully_paid.return_value = True

        res = get_booking_status(booking)

        self.assertEqual(res, 'Paid')

    @patch('get_booking_status.datetime')
    def test_get_booking_status_if_it_is_upcoming_returns_message(self, datetime_mock):
        booking = Mock(cancelled=False, start=datetime(year=2020, month=5, day=23))
        booking.is_fully_paid.return_value = False
        datetime_mock.now.return_value = datetime(year=2020, month=4, day=23)

        res = get_booking_status(booking)

        self.assertEqual(res, 'Upcoming')


if __name__ == '__main__':
    unittest.main()
