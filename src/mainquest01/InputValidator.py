class InputValidator:
    def __init__(self, restriction, error_msg):
        self.restriction = restriction
        self.error_msg = error_msg

    def validate(self, user_input):
        if not self.restriction(user_input):
            raise ValueError(self.error_msg)