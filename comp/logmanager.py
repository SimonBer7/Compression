from datetime import datetime

class LogManager:
    """
        LogManager class for managing log files.

        This class provides functionalities for adding logs, reading logs, and counting the number of logs.
        Log messages are written to a specified log file, and the class includes error handling.

        Attributes:
            count_of_logs (int): Number of logs in the log file.
            log_file (str): Path to the log file.

        Methods:
            get_line_count() -> int:
                Helper method to count lines in the log file.

            add_log(text: str) -> str:
                Adds a log message to the log file.

            read_from_log() -> str:
                Reads the content of the log file and returns it.

    """
    def __init__(self):
        """
            Initializes the LogManager instance with the log count and file path.
        """
        self.count_of_logs = 0
        self.log_file = "./logs/log.txt"

    def get_line_count(self):
        """
            Helper method to count lines in the log file.

            Returns:
                int: Number of lines in the log file.
        """
        with open(self.log_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return len(lines)

    def add_log(self, text):
        """
            Adds a log message to the log file.

            Parameters:
                text (str): The log message to be added.

            Returns:
                str: Status message indicating success or failure of log addition.
        """
        try:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                file.write(text+"\n")
        except Exception as e:
            return f"Error with writting to log file :( {e}"

    def read_from_log(self):
        """
            Reads the content of the log file and returns it.

            Returns:
                str: Content of the log file, or an error message if reading fails.
        """
        try:
            with open(self.log_file, 'r', encoding='utf-8') as file:
                content = file.read()
                actual_time = datetime.now()
                format = "%Y-%m-%d %H:%M:%S"
                time = actual_time.strftime(format)
        except Exception as e:
            self.add_log(time+"Error with reading from log file :(")
            return f"Error with reading from log file :( {e}"
        self.add_log(time+" - Successful reading from log :)")
        return content+"-"*70
