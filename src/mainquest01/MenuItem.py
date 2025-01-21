class MenuItem:
    def __init__(self, action, description):
        self.action = action
        self.description = description

    def execute(self):
        self.action()