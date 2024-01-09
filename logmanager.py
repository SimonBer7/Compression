from datetime import datetime

class LogManager:
    def __init__(self):
        self.count_of_logs = 0
        self.log_file = "./logs/log.txt"

    def add_log(self, text):
        try:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                file.write(text+"\n")
        except Exception as e:
            return f"Error with writting to log file :( {e}"

    def read_from_log(self):
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




