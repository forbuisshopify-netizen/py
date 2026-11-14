# """asyncio და კორუტინები"""
#
# import asyncio
# import time
#
#
# # სავარჯიშო 1 — კურიერები ზედიზედ და ერთდროულად
# async def deliver(order, seconds):
#     print(f"{order}: გაიგზავნა")
#     await asyncio.sleep(seconds)
#     print(f"{order}: მიტანილია")
#
#
# orders = [
#     ("შეკვეთა #1", 1.0),
#     ("შეკვეთა #2", 1.5),
#     ("შეკვეთა #3", 2.0),
# ]
#
#
# async def compare_deliveries():
#     start = time.perf_counter()
#     for order, seconds in orders:
#         await deliver(order, seconds)
#     sequential_time = time.perf_counter() - start
#     print(f"ზედიზედ: {sequential_time:.1f} წმ")
#
#     start = time.perf_counter()
#     await asyncio.gather(*(deliver(order, seconds) for order, seconds in orders))
#     concurrent_time = time.perf_counter() - start
#     print(f"ერთდროულად: {concurrent_time:.1f} წმ")
#     print(f"დაჩქარება: {sequential_time / concurrent_time:.1f}x")
#
#
# # ერთდროული ვერსია დაახლოებით ყველაზე ხანგრძლივი შეკვეთის დროს გრძელდება,
# # რადგან asyncio.sleep-ის დროს ყველა კორუტინის ლოდინი ერთმანეთს ფარავს.
#
#
# # სავარჯიშო 2 — კვადრატები
# async def square(number):
#     await asyncio.sleep(1)
#     return number * number
#
#
# async def calculate_squares():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
#     start = time.perf_counter()
#     squares = await asyncio.gather(*(square(number) for number in numbers))
#     elapsed = time.perf_counter() - start
#
#     for number, result in zip(numbers, squares):
#         print(f"{number}² = {result}")
#
#     print(f"ჯამი: {sum(squares)}")
#     print(f"დრო: {elapsed:.1f} წმ")
#
#
# # დრო დაახლოებით 1 წამია და არა 8, რადგან რვავე asyncio.sleep(1)
# # ერთდროულად იწყება და კორუტინები ერთმანეთის დასრულებას არ ელოდებიან.
#
#
# # სავარჯიშო 3 — იპოვეთ და გაასწორეთ შეცდომები
# # მოცემულ კოდში პირდაპირ main()-ის გამოძახება არაფერს დაბეჭდავდა
# # და გამოიწვევდა გაფრთხილებას: RuntimeWarning: coroutine 'main' was never awaited.
# # სწორად გაშვებულ main()-შიც await-ის გარეშე მომხმარებლების ნაცვლად
# # კორუტინის ობიექტები მოხვდებოდა სიაში.
#
# async def load_user(user_id):
#     # შეცდომა 1: time.sleep(1) ბლოკავს event loop-ს;
#     # სწორია await asyncio.sleep(1), რომ სხვა კორუტინებმაც იმუშაონ.
#     await asyncio.sleep(1)
#     return {"id": user_id, "name": f"მომხმარებელი {user_id}"}
#
#
# async def load_users():
#     start = time.perf_counter()
#
#     # შეცდომა 2: load_user(user_id) await-ის გარეშე მხოლოდ კორუტინას ქმნიდა;
#     # asyncio.gather ყველა მომხმარებელს ერთდროულად ტვირთავს და შედეგებს აბრუნებს.
#     users = await asyncio.gather(*(load_user(user_id) for user_id in (1, 2, 3)))
#
#     print(users)
#     print(f"დრო: {time.perf_counter() - start:.1f} წმ")
#
#
# async def main():
#     await compare_deliveries()
#     print()
#
#     await calculate_squares()
#     print()
#
#     await load_users()
#
#
# if __name__ == "__main__":
#     # შეცდომა 3: main() მხოლოდ კორუტინის ობიექტს აბრუნებდა;
#     # asyncio.run(main()) კორუტინას რეალურად ასრულებს.
#     asyncio.run(main())
