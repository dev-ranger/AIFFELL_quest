import datetime as dt
class Transaction:
    def __init__(self, type, amount, balance):
        self.type = type
        self.amount = amount
        self.balance = balance
        self.date = dt.datetime.now()

    def __str__(self):
        return f'날짜: {self.date}, 내용: {self.type}, 금액: {self.amount}, 잔액: {self.balance}'
