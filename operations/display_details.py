class Display:
    def __init__(self,data):
        self.data = data
        self.print_on_terminal()

    def print_on_terminal(self):
        for record in self.data:
            print(record)