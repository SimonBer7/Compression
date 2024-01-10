import string
from datetime import datetime
from comp.logmanager import LogManager

class Compressor:
    """
        Compressor class for text compression and decompression.

        This class provides methods for compressing and decompressing text files using a simple camel case encoding scheme.
        It also includes error handling and logging functionalities.

        Attributes:
            input_file (str): Path to the input text file.
            output_file (str): Path to the output compressed/decompressed text file.
            log_manager (LogManager): An instance of LogManager for logging errors and compression/decompression events.

        Methods:
            check_files() -> bool:
                Checks if input and output files exist.

            compression() -> str:
                Compresses the text from the input file and writes the result to the output file.

            decompression() -> str:
                Decompresses the text from the output file and writes the result to the same file.
        """

    def __init__(self, input_file, output_file):
        """
            Initializes the Compressor instance with input and output file paths.

            Parameters:
                input_file (str): Path to the input text file.
                output_file (str): Path to the output compressed/decompressed text file.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.log_manager = LogManager()
    def check_files(self):
        """
            Checks if input and output files exist.
        """
        files = [self.input_file, self.output_file]
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as tmp:
                    return True
            except Exception as e:
                return False

    def compression(self):
        """
            Compresses the text from the input file and writes the result to the output file.

            Returns:
                str: Status message indicating success or failure of compression.
        """
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                original_text = file.read()
                translator = str.maketrans("", "", string.punctuation)
                clean_text = original_text.translate(translator)
                words = clean_text.split()
                camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
                result = ''.join(camel_case_words)
                actual_time = datetime.now()
                format = "%Y-%m-%d %H:%M:%S"
                time = actual_time.strftime(format)
        except Exception as e:
            self.log_manager.add_log(time+" - Error with reading or compressing file :(")
            return "Error with reading or compressing file :( {e}"
        try:
            with open(self.output_file, 'w', encoding='utf-8') as file:
                file.write(result)
        except Exception as e:
            self.log_manager.add_log(f"{time} - Error with writting to output file :( {e}")
            return "Error with reading or compressing file :( {e}"
        self.log_manager.add_log(f"{time} - Compression complete :)")
        return "Compression complete :)"

    def decompression(self):
        """
            Decompresses the text from the output file and writes the result to the same file.

            Returns:
                str: Status message indicating success or failure of decompression.
        """
        try:
            letter = None
            with open(self.output_file, 'r', encoding='utf-8') as file:
                compressed_text = file.read()
                original_text = [compressed_text[0].upper()]
                for char in compressed_text[1:]:
                    if char.isdigit() and letter.isdigit():
                        original_text.append('')
                    else:
                        if char.isupper() or char.isdigit():
                            original_text.append(' ')
                    original_text.append(char.lower())
                    letter = char
                original_text.append('.')
                original_text = ''.join(original_text).split()
                original_text = ' '.join(original_text)
                actual_time = datetime.now()
                format = "%Y-%m-%d %H:%M:%S"
                time = actual_time.strftime(format)
        except Exception as e:
            self.log_manager.add_log(time + " - Error with decompressing :(")
            return f"Error with decompressing :( {e}"
        try:
            with open(self.output_file, 'w', encoding='utf-8') as file:
                file.write(original_text)
        except Exception as e:
            self.log_manager.add_log(time + " - Error with writting decompressed text to output file :(")
            return f"Error with writting decompressed text to output file :("
        self.log_manager.add_log(time + " - Decompression complete :)")
        return "Decompression complete :)"
