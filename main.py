
from console_interface import ConsoleInterface


def main():
    filename = "note.json"
    console_interface = ConsoleInterface(filename)
    console_interface.run()


if __name__ == "__main__":
    main()