"""პერსონალური დავალებების მენეჯერი. გაშვება: python main.py"""
from dataclasses import replace
from functools import wraps
from pathlib import Path

from models import Task, PRIORITIES, STATUSES
from storage import load, save

FILE = Path(__file__).with_name("tasks.json")


def save_changes(action):
    """მენიუს მოქმედების წარმატებით დასრულებისას შეინახე განახლებული სია."""
    @wraps(action)
    def wrapper(tasks):
        updated = action(tasks)
        save(FILE, [task.record() for task in updated])
        print("ცვლილება შენახულია.")
        return updated
    return wrapper


def field(label, old=None):
    hint = f" [{old}]" if old is not None else ""
    answer = input(label + hint + ": ").strip()
    return answer or old or ""


def select(label, options, old=None):
    for number, option in enumerate(options, 1):
        print(f"{number}. {option}")
    value = field(label, old)
    if value in options:
        return value
    if value in [str(i) for i in range(1, len(options) + 1)]:
        return options[int(value) - 1]
    raise ValueError("აირჩიე ერთ-ერთი ჩამოთვლილი ვარიანტი.")


def choose_task(tasks):
    number = input("დავალების ნომერი: ").strip()
    for task in tasks:
        if str(task.id) == number:
            return task
    raise ValueError("ამ ნომრით დავალება ვერ მოიძებნა.")


def enter_task(number, old=None):
    return Task(number, field("სათაური", old.title if old else None),
                field("აღწერა", old.description if old else None),
                field("ვადა (YYYY-MM-DD)", old.deadline if old else None),
                select("პრიორიტეტი", PRIORITIES, old.priority if old else None),
                field("პროექტი", old.project if old else None),
                old.status if old else "pending")


@save_changes
def add(tasks):
    next_id = max((task.id for task in tasks), default=0) + 1
    return tasks + [enter_task(next_id)]


@save_changes
def edit(tasks):
    old = choose_task(tasks)
    print("არსებული მნიშვნელობის დასატოვებლად დააჭირე Enter-ს.")
    new = enter_task(old.id, old)
    return [new if task == old else task for task in tasks]


@save_changes
def change_status(tasks):
    old = choose_task(tasks)
    new = replace(old, status=select("სტატუსი", STATUSES))
    return [new if task == old else task for task in tasks]


@save_changes
def delete(tasks):
    old = choose_task(tasks)
    return [task for task in tasks if task != old]


def show(tasks):
    if not tasks:
        print("დავალებები ვერ მოიძებნა.")
    groups = {}
    for task in tasks:
        groups.setdefault(task.project, []).append(task)
    for project, members in sorted(groups.items()):
        print(f"\nპროექტი: {project}")
        for task in sorted(members, key=lambda item: item.deadline):
            print(task.summary())


def main():
    records = load(FILE, [])
    if not isinstance(records, list):
        raise ValueError("დავალებების ფაილში სია უნდა იყოს.")
    tasks = [Task(**record) for record in records]
    if len({task.id for task in tasks}) != len(tasks):
        raise ValueError("ფაილში დავალებების ნომრები მეორდება.")
    actions = {"1": add, "4": edit, "5": change_status, "6": delete}
    while True:
        print("\n1. დამატება   2. ყველა პროექტი   3. ძებნა")
        print("4. რედაქტირება   5. სტატუსი   6. წაშლა   0. გასვლა")
        choice = input("აირჩიე: ").strip()
        try:
            if choice == "0":
                save(FILE, [task.record() for task in tasks])
                return
            if choice in actions:
                tasks = actions[choice](tasks)
            elif choice == "2":
                show(tasks)
            elif choice == "3":
                query = field("საძიებო სიტყვა").casefold()
                if not query:
                    raise ValueError("ჩაწერე საძიებო სიტყვა.")
                show([task for task in tasks if any(query in value.casefold()
                      for value in (task.title, task.description, task.project))])
            else:
                print("აირჩიე მენიუში მითითებული ნომერი.")
        except (ValueError, OSError) as error:
            print("მოქმედება ვერ შესრულდა:", error)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nნახვამდის!")
    except (TypeError, ValueError, OSError) as error:
        print("დავალებების ფაილი ვერ ჩაიტვირთა:", error)
