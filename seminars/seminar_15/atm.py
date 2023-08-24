import logging
import sys

# Реализация банкомата использованием логгирования и также реализуйте возможность запуска из
# командной строки с передачей параметров.

# Насторойка логгирования
logging.basicConfig(filename="atm.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        logging.info("Проверка баланса")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            logging.error("На счету недостаточно средств")
            return "Ошибка: На счету недостаточно средств"
        else:
            self.balance -= amount
            logging.info(f'Снятие средств на {amount} рублей')
            return f'Успешно снято на {amount} рублей'

    def deposit(self, amount):
        self.balance += amount
        logging.info(f"Пополнение на {amount} рублей")
        return f'Успешно пополнено на {amount} рублей'

if __name__ == "__main__":
    # Получение параметоров из командной строки
    args = sys.argv[1:]
    balance = int(args[0])

    # Создание экземпляра банкомата
    atm = ATM(balance)

    print(f'Баланс: {atm.check_balance()}')
    print(atm.withdraw(500))
    print(atm.deposit(1000))
    print(f'Баланс: {atm.check_balance()}')

    # Для запуска кода в терминале выбираем путь файла где она нахоидтся открываем этот файл терминале запускаем командой python atm.py 1000 (и вводим любую сумму)