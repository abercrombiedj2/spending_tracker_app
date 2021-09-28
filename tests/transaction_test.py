import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction(100, "Lidl", "Groceries")
    
    def test_transaction_has_amount(self):
        self.assertEqual(100, self.transaction.amount)
    
    def test_transaction_has_id(self):
        self.assertEqual(None, self.transaction.id)
    
    def test_transaction_has_merchant(self):
        self.assertEqual("Lidl", self.transaction.merchant)
    
    def test_transaction_has_tag(self):
        self.assertEqual("Groceries", self.transaction.tag)
