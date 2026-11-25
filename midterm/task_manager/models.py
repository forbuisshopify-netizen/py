"""დავალების მონაცემები და მათი შემოწმების წესები."""
from dataclasses import dataclass, asdict
from datetime import date

PRIORITIES = ("დაბალი", "საშუალო", "მაღალი")
STATUSES = ("pending", "in-progress", "completed")


@dataclass(frozen=True)
class Entry:
    id: int
    title: str

    def summary(self):
        return f"#{self.id} {self.title}"


@dataclass(frozen=True)
class Task(Entry):
    description: str
    deadline: str
    priority: str
    project: str
    status: str = "pending"

    def __post_init__(self):
        if type(self.id) is not int or self.id < 1:
            raise ValueError("დავალების ნომერი არასწორია.")
        for field in (self.title, self.project, self.deadline, self.description):
            if not isinstance(field, str) or not field.strip():
                raise ValueError("ყველა ველი უნდა შეავსო.")
        try:
            parsed = date.fromisoformat(self.deadline)
            if parsed.isoformat() != self.deadline:
                raise ValueError
        except ValueError:
            raise ValueError("თარიღი ჩაწერე ფორმატით YYYY-MM-DD.") from None
        if self.priority not in PRIORITIES or self.status not in STATUSES:
            raise ValueError("პრიორიტეტი ან სტატუსი არასწორია.")

    def summary(self):
        return (f"{super().summary()} | {self.deadline} | {self.priority} | "
                f"{self.status}\n   {self.description}")

    def record(self):
        return asdict(self)
