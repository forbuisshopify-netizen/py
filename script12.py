# """ათვლა და კვადრატები"""
#
# def countdown(start):
#     for number in range(start, 0, -1):
#         yield number
#     yield "სტარტი! 🚀"
#
#
# def squares_up_to(limit):
#     number = 1
#     while number ** 2 <= limit:
#         yield number ** 2
#         number += 1
#
# launch = countdown(3)
# print(next(launch))
# print(next(launch))
# print(list(launch))
# print(list(launch))  # წინა list()-მა გენერატორი ამოწურა, ამიტომ აქ [] მივიღეთ.
#
# print(list(squares_up_to(50)))
# print(sum(squares_up_to(100)))
# for square in squares_up_to(20):
#     print(square, end=" ")
# print()
