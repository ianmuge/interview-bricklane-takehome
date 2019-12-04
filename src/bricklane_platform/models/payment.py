from decimal import Decimal
from dateutil.parser import parse


from bricklane_platform.models.card import Card
from bricklane_platform.models.bank import Bank
from bricklane_platform.config import PAYMENT_FEE_RATE



class Payment(object):

    customer_id = None
    date = None
    amount = None
    fee = None
    card_id = None
    bank_account_id=None
    payment_method=None

    def __init__(self, data=None):

        if not data:
            return

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

        if "card_id" in data:
            card = Card()
            card.card_id = int(data["card_id"])
            card.status = data["card_status"]
            self.card = card
            self.payment_method="card"
        elif "bank_account_id" in data:
            bank = Bank()
            bank.bank_account_id = int(data["bank_account_id"])
            bank.status = "processed"
            self.bank = bank
            self.payment_method = "bank"
        else:
            raise Exception("Data Structure not valid")

    # def is_successful(self):
    #     if self.payment_method=="card":
    #         return self.card.status == "processed"
    #     elif self.payment_method=="bank":
    #         return True
    #     else:
    #         raise Exception("Payment method not valid")
    def is_successful(self):
        if hasattr(self, 'card'):
            return self.card.status == "processed"
        elif hasattr(self, 'bank'):
            return self.bank.status == "processed"
        else:
            raise Exception("Payment method not valid")
