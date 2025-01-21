import re

from mainquest01.BankService import BankService
from mainquest01.InputDict import InputDict
from mainquest01.MenuSupplier import MenuSupplier

if __name__ == "__main__":
    input_dict = InputDict()
    bank_service = BankService()
    menu_supplier = MenuSupplier(bank_service)

    while True:
        menu = bank_service.show_choose_menu()
        print(menu)
        if menu == 6:
            break
        menu_supplier.menu_dict[menu].action()

    print("프로그램 종료")

