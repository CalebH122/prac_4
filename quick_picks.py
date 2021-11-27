import random

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    random_list = []
    for x in range(6):
        number = random.randint(1, 45)
        random_list.append(number)
        random_list.sort()
    number = random_list[0:]
    print(f"{number[0]} {number[1]} {number[2]} {number[3]} {number[4]} {number[5]}")
    random_list.clear()