import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant = Merchant("Lidl")
    
    def test_merchant_has_name(self):
        self.assertEqual("Lidl", self.merchant.name)

    def test_merchant_has_id(self):
        self.assertEqual(None, self.merchant.id)