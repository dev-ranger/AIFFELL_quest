import re

from mainquest01.InputValidator import InputValidator
from mainquest01.UserInput import UserInput


class InputDict:
    def __init__(self):
        self.input_dict = {
            "owner_name": UserInput(
                "str",
                "이름을 입력하세요",
                InputValidator(lambda txt: len(txt) > 0, "이름은 문자열로 입력하세요"),
            ),
            "balance": UserInput(
                "int",
                "입금액을 입력하세요",
                InputValidator(lambda b: b > 0, "입금액은 숫자로 입력하세요"),
            ),
            "menu": UserInput(
                "int",
                "메뉴를 선택하세요",
                InputValidator(lambda m: -1 < m < 7, "메뉴는 숫자로 입력하세요"),
            ),
            "account_number": UserInput(
                "str",
                "계좌번호를 입력하세요",
                InputValidator(
                    lambda an: re.match(r"\d{3}-\d{2}-\d{7}", an),
                    "계좌번호는 3-2-7 형식으로 입력하세요",
                ),
            ),
            "amount": UserInput(
                "int",
                "금액을 입력하세요",
                InputValidator(lambda a: a >= 0, "금액은 숫자로 입력하세요"),
            ),
        }

    def get_input(self, key):
        return self.input_dict[key]

