class UserInput:
    def __init__(self, input_type, msg, validator):
        self.input_type = input_type
        self.msg = msg
        self.validator = validator

    def get_input(self):
        while True:
            try:
                user_input = input(f"{self.msg}: ")
                if self.input_type == 'int':
                    user_input = int(user_input)
                self.validator.validate(user_input)
                return user_input
            except ValueError as e:
                print(e)