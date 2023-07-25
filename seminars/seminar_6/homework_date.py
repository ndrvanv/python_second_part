import sys
from datetime import datetime
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку
def check_date(str_data):
    try:
        date = datetime.strptime(str_data, "%Y-%m-%d")
        current_data = datetime.now().date()

        if date.date() == current_data:
            print("Введенные значения совпадают с текущей датой")
        elif date.date() > current_data:
            print("Введенные значения в будущем от текущей даты")
        else:
            print("Введенная дата в прошлом")

    except ValueError:
        print("Введено некоректное значение даты. Введите дату в формате YYYY-MM-DD")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        date_to_check = sys.argv[1]
        check_date(date_to_check)
    else:
        print("Введите дату в формате YYYY-MM-DD")