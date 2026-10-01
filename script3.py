# This is a sample Python script.
age = int(input("შეიყვანე ასაკი: "))

if age >= 18:
    print("შესვლა დაშვებულია")

elif age >= 12 and age <= 17:
    parent = input("მშობელთან ერთად ხარ? (კი/არა): ")

    if parent == "კი":
        print("შესვლა დაშვებულია")
    else:
        print("შესვლა აკრძალულია")

else:
    print("შესვლა აკრძალულია")
