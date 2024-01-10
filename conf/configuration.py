class Configuration:
    """
    Configuration class for managing file paths.

    This class provides default file paths for input, output, test input, and test output files.
    The file paths can be accessed using the corresponding getter methods.

    Attributes:
        input_file (str): Default path for input file.
        output_file (str): Default path for output file.
        test_input (str): Default path for test input file.
        test_output (str): Default path for test output file.

    Methods:
        get_input() -> str:
            Returns the default path for the input file.

        get_output() -> str:
            Returns the default path for the output file.

        get_test_input() -> str:
            Returns the default path for the test input file.

        get_test_output() -> str:
            Returns the default path for the test output file.
    """

    def __init__(self):
        """
        Initializes default file paths.
        """
        self.input_file = "./src/input.txt"
        self.output_file = "./src/output.txt"
        self.test_input = "./test_data/test_input.txt"
        self.test_output = "./test_data/test_output.txt"

    def get_input(self) -> str:
        """
        Returns the default path for the input file.
        """
        return self.input_file

    def get_output(self) -> str:
        """
        Returns the default path for the output file.
        """
        return self.output_file

    def get_test_input(self) -> str:
        """
        Returns the default path for the test input file.
        """
        return self.test_input

    def get_test_output(self) -> str:
        """
        Returns the default path for the test output file.
        """
        return self.test_output
