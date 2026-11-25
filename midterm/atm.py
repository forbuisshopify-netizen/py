"""სასწავლო ბანკომატი. გაშვება: python atm.py"""
import json
import re
from abc import ABC, abstractmethod
from pathlib import Path
from tempfile import NamedTemporaryFile


def read_amount(text):
    text = text.strip().replace(",", ".")
    if not re.fullmatch(r"[0-9]+(\.[0-9]{1,2})?", text):
        raise ValueError("თანხა ჩაწერე ლარებში, მაგალითად 12.50.")
    whole, _, fraction = text.partition(".")
    tetri = int(whole) * 100 + int(fraction.ljust(2, "0"))
    if tetri <= 0:
        raise ValueError("თანხა ნულზე მეტი უნდა იყოს.")
    return tetri


def money(tetri):
    return f"{tetri // 100}.{tetri % 100:02d} ₾"


class Operation(ABC):
    @abstractmethod
    def change(self, amount):
        """აბრუნებს ბალანსის ცვლილებას თეთრებში."""


class Deposit(Operation):
    def change(self, amount):
        return amount


class Withdrawal(Operation):
    def change(self, amount):
        return -amount


class Account:
    def __init__(self, balance=0):
        if type(balance) is not int or balance < 0:
            raise ValueError("ანგარიშის ფაილში ბალანსი დაზიანებულია.")
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def apply(self, operation, amount):
        if type(amount) is not int or amount <= 0:
            raise ValueError("თანხა უნდა იყოს დადებითი.")
        new_balance = self.balance + operation.change(amount)
        if new_balance < 0:
            raise ValueError("ანგარიშზე საკმარისი თანხა არ არის.")
        self._balance = new_balance


def load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def save(path, data):
    # ძველი ფაილი მხოლოდ ახალი ასლის სრულად ჩაწერის შემდეგ იცვლება.
    with NamedTemporaryFile(dir=path.parent, delete=False, mode="w",
                            encoding="utf-8") as stream:
        temporary = Path(stream.name)
        try:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.flush()
        except BaseException:
            stream.close()
            temporary.unlink(missing_ok=True)
            raise
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


FILE = Path(__file__).with_name("account.json")
RECEIPT = FILE.with_name("balance_receipt.txt")
MENU = ["1. ბალანსი", "2. თანხის შეტანა", "3. თანხის გატანა",
        "4. ბალანსის ქვითრის შენახვა", "5. ქვითრის წაშლა", "0. გასვლა"]
OPERATIONS = {"2": Deposit(), "3": Withdrawal()}


def main():
    print("ბანკომატი · სასწავლო ანგარიში")
    while True:
        print("\n" + "\n".join(MENU))
        choice = input("აირჩიე: ").strip()
        if choice == "0":
            return
        try:
            data = load(FILE, {"balance_tetri": 0})
            if not isinstance(data, dict) or "balance_tetri" not in data:
                raise ValueError("ანგარიშის ფაილის ფორმატი არასწორია.")
            account = Account(data["balance_tetri"])
            if choice in OPERATIONS:
                amount = read_amount(input("თანხა ლარებში: "))
                account.apply(OPERATIONS[choice], amount)
                save(FILE, {"balance_tetri": account.balance})
                print("ოპერაცია შესრულდა.")
            elif choice == "4":
                RECEIPT.write_text(f"ანგარიშის ბალანსი: {money(account.balance)}\n",
                                   encoding="utf-8")
                print("ქვითარი შენახულია:", RECEIPT.name)
            elif choice == "5":
                try:
                    RECEIPT.unlink()
                    print("ქვითარი წაიშალა.")
                except FileNotFoundError:
                    print("შენახული ქვითარი არ არის.")
            elif choice != "1":
                print("აირჩიე მენიუში მითითებული ნომერი.")
                continue
            print("ბალანსი:", money(account.balance))
        except (ValueError, OSError) as error:
            print("ოპერაცია ვერ შესრულდა:", error)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nნახვამდის!")
