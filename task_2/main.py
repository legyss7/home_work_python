# Добавьте логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной
# строки с передачей параметров.
import argparse
import argparse
from pathlib import Path
from archive import Archive
from archive_exception import InvalidTextError, InvalidNumberError
from logger_setup import setup_logging


def main():
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(description="Process some text and number.")
    parser.add_argument('text', type=str, help='Text to be archived')
    parser.add_argument('number', type=float, help='Number to be archived')
    parser.add_argument('-p', '--path', type=str, default=str(script_dir),
                        help='Path to save the archives (default: script directory)')

    try:
        args = parser.parse_args()
    except SystemExit as e:
        logger_info, logger_error = setup_logging(script_dir)
        logger_error.error(f"Argument parsing failed: {e}")
        print("Error: Argument parsing failed. Check the logs for more details.")
        return

    logger_info, logger_error = setup_logging(Path(args.path))

    if not args.text.strip():
        logger_error.error("Text argument is missing or empty.")
        print("Error: Text is required and cannot be empty.")
        return

    if args.number is None:
        logger_error.error("Number argument is missing.")
        print("Error: Number is required.")
        return

    archive_path = Path(args.path)
    if not archive_path.exists():
        archive_path.mkdir(parents=True)

    try:
        archive_instance = Archive(args.text, args.number)
        logger_info.info(f"Created archive instance: {archive_instance}")
        print(archive_instance)
    except (InvalidTextError, InvalidNumberError) as e:
        logger_error.error(f"Error occurred: {e}")
        print(f"Error: {e}")


#  test OK
# Для запуска задаем длинный путь или переходим в папку task_2
#  python C:\projects\Python_projects\gb_second_year\1_Python\home_work\task_2\main.py
#  "Hello" 123 -p C:\projects\Python_projects\gb_second_year\1_Python\home_work\task_2

#  python main.py "Hello" 123 -p C:\projects\Python_projects\gb_second_year\1_Python\home_work\task_2
#  python main.py "Hello" 123

#  test ERROR
#  python main.py "Hello" -123 -p C:\projects\Python_projects\gb_second_year\1_Python\home_work\task_2
#  python main.py "Hello" -123
#  python main.py " " 1233 -p C:\projects\Python_projects\gb_second_year\1_Python\home_work\task_2
#  python main.py "Hello" -p C:\projects\Python_projects\gb_second_year\1_Python\home_work\task_2
#  python main.py  -p C:\projects\Python_projects\gb_second_year\1_Python\home_work\task_2
#  python main.py
if __name__ == '__main__':
    main()
