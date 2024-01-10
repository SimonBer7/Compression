
from comp.compresse import Compressor
from conf.configuration import Configuration

def main():
    """
        Main function for the Compressor program.

        This function serves as the entry point for the Compressor program. It provides a menu-driven interface
        for users to set up the compression, choose actions, and interact with the Compressor class.
    """
    print("Welcome in Compressor, let's do set up\n" + "-" * 70)
    print("1.) Default setup\n2.) Your own set up\n"+"-"*70)
    while(True):
        try:
            settings = int(input("Your choice: "))
            if 1 <= settings <= 2:
                break
            else:
                print("-" * 70)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            print("-" * 70)
    if settings == 1:
        c = Configuration()
        input_file = c.get_input()
        output_file = c.get_output()
    elif settings == 2:
        print("-" * 70)
        i_file = input("Enter name of the file you want compress (without .txt): ")
        input_file = "./src/"+i_file+".txt"
        o_file = input("Enter name of the file on output (without .txt): ")
        output_file = "./src/"+o_file+".txt"
    compressor = Compressor(input_file, output_file)
    running = True
    if compressor.check_files():
        print("-" * 70)
    else:
        running = False
        print("Error with files :(")

    while (running):
        print("Welcome in Compressor, now it's up to you:\n" + "-" * 70)
        print("1.) Compress file\n2.) Decompress file\n3.) Print from log\n4.) Help\n5.) Exit\n" + "-" * 70)
        while (True):
            try:
                choice = int(input("Your choice: "))
                if 1 <= choice <= 5:
                    print("-" * 70)
                    break
                else:
                    print("-" * 70)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                print("-" * 70)
        if choice == 1:
            print(compressor.compression())
            print("-" * 70)
        elif choice == 2:
            print(compressor.decompression())
            print("-" * 70)
        elif choice == 3:
            print(compressor.log_manager.read_from_log())
        elif choice == 4:
            print("Here is manual :D\nThis program has five options to do...\n1 - Compressing file\n2 - Decompressing file\n3 - Printing all logs from file log\n4 - Manual\n5 - EXIT")
            print("-" * 70)
        elif choice == 5:
            print("Goodbye :D")
            running = False


if __name__ == "__main__":
    main()
