# price =float(input("ყიდვის თანხა (ლარი) :"))
# promo= input("პრომო კოდი (თუ არ გაქვს -Enter):")
#
# if price >= 200:
#     discount=20
# elif price >= 100:
#     discount=10
# elif price >= 50:
#     discount=5
# else:
#     discount=0
#
# final_price=price*(1-discount/100)
#
#
# if promo.lower() == "vip":
#     final_price -= 5
#     print("VIP კოდი: დამატებით -5 ლარი")
#
#
#
# print("ფასდაკლება:", discount, "%")
# print("გადასახდელი:", round(final_price, 2), "ლარი")






#
#
# class InvalidScoreError(Exception):
#     pass
#
#
# try:
#     print("=== სტუდენტის შეფასების სისტემა ===")
#
#     name = input("სტუდენტის სახელი: ").strip()
#     initial = name[0]
#
#     score = int(input("მიღებული ქულა: "))
#     maximum = int(input("მაქსიმალური ქულა: "))
#
#     if maximum == 0:
#         raise ZeroDivisionError
#
#     if score < 0 or maximum < 0 or score > maximum:
#         raise InvalidScoreError
#
#
#     percent = score / maximum * 100
#
#     if percent>=91:
#         grade = "A"
#     elif percent>=81:
#         grade = "B"
#     elif percent>=71:
#         grade = "C"
#     elif percent>=60:
#         grade = "D"
#     elif percent>=50:
#         grade = "E"
#     elif percent>=40:
#         grade = "FX"
#     else:
#         grade = "F"
#
#
# except IndexError:
#     print("❌ სახელი ცარიელი ვერ იქნება")
#
# except ValueError:
#     print("❌ ქულები მთელი რიცხვებით ჩაწერეთ")
#
# except ZeroDivisionError:
#     print("❌ მაქსიმალური ქულა 0 ვერ იქნება")
#
# except InvalidScoreError:
#     print("❌ ქულა არასწორ დიაპაზონშია")
#
# else:
#     print(f"✅ {initial}. {name} — {percent:.1f}% — შეფასება: {grade}")
#
# finally:
#     print("შეფასების სისტემამ მუშაობა დაასრულა")
