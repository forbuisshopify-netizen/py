# """წყარო — დავალება (2).docx"""
#
#
# # სავარჯიშო 1 — წიგნის კლასი
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def info(self):
#         print(f"{self.title} — {self.author}, {self.pages} გვ.")
#
# books = [
#     Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 250),
#     Book("იგი", "ჯემალ ქარჩხაძე", 64),
#     Book("ბახტრიონი", "ვაჟა-ფშაველა", 48),
# ]
# for book in books:
#     book.info()
#
#
# # სავარჯიშო 2 — მანქანები და ბორბლები
# class Car:
#     wheels = 4
#
#     def __init__(self, brand, color, year):
#         self.brand = brand
#         self.color = color
#         self.year = year
#
# first = Car("BMW", "შავი", 2020)
# second = Car("Toyota", "თეთრი", 2022)
# print(first.brand, first.wheels)
# print(second.brand, second.wheels)
# second.wheels = 3
# # მეორე მანქანას საკუთარი wheels აქვს. პირველი ისევ კლასის მნიშვნელობას კითხულობს.
# print(first.wheels)
# print(second.wheels)
# print(Car.wheels)
#
#
# # სავარჯიშო 3 — მოთამაშეების მთვლელი
# class Player:
#     players_count = 0
#
#     def __init__(self, name, level=1):
#         self.name = name
#         self.level = level
#         Player.players_count += 1
#
# print(Player.players_count)
# players = [Player("ანა"), Player("დავითი", 5), Player(name="მარიამი", level=3)]
# print("სულ მოთამაშე:", Player.players_count)
# for player in players:
#     print(player.name, player.level)
