
class Configuration:
    def __init__(self):
        self.input_file = "input.txt"
        self.output_file = "output.txt"

    def get_input(self):
        return self.input_file

    def get_output(self):
        return self.output_file