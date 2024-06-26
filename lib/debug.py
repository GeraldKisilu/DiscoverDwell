from lib.cli import main_menu
from lib.helpers import create_tables, populate_sample_data

def main():
    create_tables()
    populate_sample_data()
    main_menu()

if __name__ == '__main__':
    main()
