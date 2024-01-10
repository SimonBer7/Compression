
import unittest
from comp.compresse import Compressor
from conf.configuration import Configuration

class TestCompressor(unittest.TestCase):
    """
        TestCompressor class for unit testing the Compressor class.

        This class contains methods to test the compression, decompression, and logging functionalities
        of the Compressor class using a predefined set of test input and output files.

        Methods:
            test_compression() -> None:
                Tests the compression method of the Compressor class.

            test_decompression() -> None:
                Tests the decompression method of the Compressor class.

            test_add_log() -> None:
                Tests the log addition functionality of the LogManager class.
    """
    def test_compression(self):
        """
            Tests the compression method of the Compressor class.
        """
        try:
            c = Compressor(Configuration.get_test_input, Configuration.get_test_output)
            c.compression()
            with open(c.output_file, 'r', encoding='utf-8') as file:
                result = file.read()
        except Exception as e:
            return f"Error with reading from test file :( {e}"
        self.assertEquals(result, "helloWorldThisIsSimpleFileForTestingThisProject")


    def test_decompression(self):
        """
            Tests the decompression method of the Compressor class.
        """
        try:
            c = Compressor(Configuration.get_test_input, Configuration.get_test_output)
            c.decompression()
            with open(c.output_file, 'r', encoding='utf-8') as file:
                result = file.read()
        except Exception as e:
            return f"Error with reading from test file :( {e}"
        self.assertEquals(result, "Hello world this is simple file for testing this project.")

    def test_add_log(self):
        """
            Tests the log addition functionality of the LogManager class.
        """
        try:
            c = Compressor(Configuration.get_test_input, Configuration.get_test_output)
            count = c.log_manager.get_line_count()
            c.log_manager.add_log("Test add text to log.txt")
            count_after = c.log_manager.get_line_count()
            self.assertEquals(count_after, count+1)
        except Exception as e:
            return f"Error with test of adding to log.txt"
