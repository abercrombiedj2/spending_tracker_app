class Transaction:

    def __init__(self, amount, merchant, tag, timestamp, id=None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.id = id
        self.timestamp = timestamp