from mainquest01.MenuItem import MenuItem


class MenuSupplier:

    def __init__(self, bank_service):
        self.menu_dict = {
            0: MenuItem(bank_service.print_accounts, "0. 전체 계좌 출력"),
            1: MenuItem(bank_service.create_new_account, "1. 계좌 생성"),
            2: MenuItem(bank_service.deposit, "2. 입금"),
            3: MenuItem(bank_service.withdraw, "3. 출금"),
            4: MenuItem(bank_service.print_account_info, "4. 계좌 정보 출력"),
            5: MenuItem(bank_service.print_transaction_history, "5. 거래 내역 출력"),
            6: MenuItem(exit, "6. 종료"),
        }

