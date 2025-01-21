from enum import Enum
class TransactionType(Enum):
    DEPOSIT = (1, '입금')
    WITHDRAW = (2, '출금')
    INCREASE_DEPOSIT_INTEREST = (3, '이자지급')

    def __init__(self, code, title):
        self.code = code
        self.title = title

    def __str__(self):
        return self.title