import random

from mainquest01.Transaction import Transaction
from mainquest01.TransactionType import TransactionType


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = self.create_account_number()
        self.bank_name = 'SC은행'
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction_history(TransactionType.DEPOSIT, amount, self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        self.add_transaction_history(TransactionType.WITHDRAW, amount, self.balance)

    def get_transaction_history(self):
        return self.transaction_history

    def get_withdraw_history(self):
        return filter(lambda t : t.type == TransactionType.WITHDRAW, self.transaction_history)

    def get_deposit_history(self):
        return filter(lambda t : t.type == TransactionType.DEPOSIT, self.transaction_history)

    def add_transaction_history(self, tr_type, amount, balance):
        self.transaction_history.append(Transaction(tr_type,amount, balance))

    def create_account_number(self):
        return (f'{random.randint(100, 999)}'
                f'-{random.randint(10, 99)}'
                f'-{random.randint(1000000, 9999999)}')

    def display_info(self):
        return(f'은행명: {self.bank_name}, 이름: {self.name}, 계좌번호: {self.account_number}, 잔액: {self.balance}')

    def __str__(self):
        return f'은행명: {self.bank_name}, 이름: {self.name}, 계좌번호: {self.account_number}, 잔액: {self.balance}'


