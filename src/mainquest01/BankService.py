from mainquest01.Account import Account
from mainquest01.InputDict import InputDict
from mainquest01.MenuSupplier import MenuSupplier


class BankService:
    def __init__(self):
        self.account_list = []
        self.inputDict = InputDict()
        self.menu_dict = MenuSupplier(self)

    def input_from_user(self, option):
        return option.get_input()

    def show_choose_menu(self):
        for key, value in self.menu_dict.menu_dict.items():
            print(value.description)
        return self.input_from_user(self.inputDict.get_input("menu"))

    def input_account_number(self):
        return self.input_from_user(self.inputDict.get_input("account_number"))

    def create_new_account(self):
        name = self.input_from_user(self.inputDict.get_input("owner_name"))
        balance = self.input_from_user(self.inputDict.get_input("balance"))
        account = Account(name, balance)
        self.account_list.append(account)
        print(f"계좌가 생성되었습니다. {account.display_info()}")
        return account

    def find_account_by_account_num(self, account_number):
        for account in self.account_list:
            if account.account_number == account_number:
                print(f"계좌를 찾았습니다. {account.display_info()}")
                return account
        return None

    # def get_valid_account(self, find_account_func):
    #     def decorator(func):
    #         def wrapper(input_dict):
    #             account_number = self.input_from_user(input_dict['account_number'])
    #             account = find_account_func(account_number)
    #             if account is None:
    #                 print('계좌가 올바르지 않습니다.')
    #                 return False
    #             return func(input_dict, account)
    #         return wrapper
    #     return decorator

    def deposit(self):
        input_dict = InputDict().input_dict
        account_number = self.input_from_user(input_dict["account_number"])
        account = self.find_account_by_account_num(account_number)
        if account is None:
            print("계좌가 올바르지 않습니다.")
            return False
        amount = self.input_from_user(input_dict["amount"])
        account.deposit(amount)
        print(f"{amount}원이 입금 되었습니다. 잔액: {account.balance}")
        return True

    def withdraw(self):
        input_dict = InputDict().input_dict
        account_number = self.input_from_user(input_dict["account_number"])
        account = self.find_account_by_account_num(account_number)
        if account is None:
            print("계좌가 올바르지 않습니다.")
            return False
        amount = self.input_from_user(input_dict["amount"])
        account.withdraw(amount)
        print(f"{amount}원이 출금 되었습니다. 잔액: {account.balance}")
        return True

    # deposit = get_valid_account(find_account_by_account_num)(deposit)
    # withdraw = get_valid_account(find_account_by_account_num)(withdraw)

    def print_transaction_history(self):
        account_number = self.input_account_number()
        account = self.find_account_by_account_num(account_number)
        if account is None:
            print("계좌가 올바르지 않습니다.")
        else:
            index = 0
            for transaction in account.get_transaction_history():
                index += 1
                print(
                    f"{index}회: {transaction.type}, 금액: {transaction.amount}, 잔액: {transaction.balance}"
                )

    def print_account_info(self):
        account_number = self.input_account_number()
        account = self.find_account_by_account_num(account_number)
        if account is None:
            print("계좌가 올바르지 않습니다.")
        else:
            print(account)

    def print_accounts(self):
        for account in self.account_list:
            print(account)

