from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

merchant_1 = Merchant("Lidl")
merchant_repository.save(merchant_1)

tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

transaction_1 = Transaction(50, merchant_1, tag_1)
transaction_repository.save(transaction_1)
transaction_repository.select_all()