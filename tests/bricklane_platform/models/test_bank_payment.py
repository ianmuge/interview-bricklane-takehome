import unittest
from datetime import datetime

from bricklane_platform.models.payment import Payment
from bricklane_platform.models.bank import Bank


class TestBankPayment(unittest.TestCase):
    def test_bank_init(self):
        payment = Payment()
        self.assertIsNone(payment.customer_id)
        self.assertIsNone(payment.date)
        self.assertIsNone(payment.amount)
        self.assertIsNone(payment.fee)
        self.assertIsNone(payment.bank_account_id)

    def test_bank_init_with_data(self):

        data = {
            "amount": "2000",
            "bank_account_id": "45",
            "bank_status": "processed",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        payment = Payment(data)

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)

        bank = payment.bank

        self.assertIsInstance(bank, Bank)
        self.assertEqual(bank.bank_account_id, 45)
        self.assertEqual(bank.status, "processed")

    def test_bank_is_successful(self):
        bank = Bank()
        bank.status = "processed"
        payment = Payment()
        payment.bank = bank
        self.assertTrue(payment.is_successful())