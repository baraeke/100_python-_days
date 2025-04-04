# import random

# # number = random.random() * 10000.009
# # new_random_number = round(number)
# # print(new_random_number)

# # number = random.random() * 100
# # random_number = round(number)
# #
# # if random_number % 2 == 0:
# #     print("Heads")
# # else:
# #     print("Tails")

# # friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# # who_will_pay_the_bill =random.randint(0, len(friends) -1)
# # print(f"{friends[who_will_pay_the_bill]} will pay the bill")

# # list_ = ["item1", "item2", "item3"]
# # list__ =["item4", "item5", "item6"]
# #
# # list___ = [list_, list__]
# # print(list___[1][1])

# # rock = "ROCK"
# # paper = "PAPER"
# # scissors = "SCISSORS"
# # computer_choices = [rock, paper, scissors]
# # comp_choice = random.choice(computer_choices)
# # user_choices = [rock, paper, scissors]
# # user_choice = user_choices[int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors "))]
# #
# # print(f"Your choice is {user_choice}")
# # print(f"Computer choice is {comp_choice}")
# #
# # if user_choice == rock:
# #     if comp_choice == rock:
# #         print("It's a DRAW!")
# #     elif comp_choice == paper:
# #         print("You LOSE!")
# #     elif comp_choice == scissors:
# #         print("You WIN!")
# # elif user_choice == paper:
# #     if comp_choice == rock:
# #         print("You WIN!")
# #     elif comp_choice == paper:
# #         print("It's a DRAW!")
# #     elif comp_choice == scissors:
# #         print("You LOSE!")
# # elif user_choice == scissors:
# #     if comp_choice == rock:
# #         print("You LOSE!")
# #     elif comp_choice == paper:
# #         print("You WIN!")
# #     elif comp_choice == scissors:
# #         print("It's a DRAW!")

# # student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
# #
# # max_score = 0
# #
# # for student in student_score:
# #     if student > max_score:
# #         max_score = student
# #     else:
# #         continue
# # print(max_score)

# # sum_ = 0
# #
# # for i in range(101):
# #     sum_ += i
# # print(sum_)

# # for number in range(1, 101):
# #     if (number % 5 == 0) and (number % 3 == 0):
# #         print("FizzBuzz")
# #     elif number % 3 == 0:
# #         print("Fizz")
# #     elif number % 5 == 0:
# #         print("Buzz")
# #     else:
# #         print(number)

# upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols = ["@", "#", "$", "%", "&", "|", "?", "~",]

# print("Welcome to the PyPassword Generator!")

# num_of_upper_case = int(input("How many uppercase letters would you like in your password? "))
# num_of_lower_case = int(input("How many lowercase letters would you like in your password? "))
# num_of_numbers = int(input("How many numbers would you like in your password? "))
# num_of_symbols = int(input("How many symbols would you like in your password? "))

# upper_generated = ""
# for upper_case_ in range(1, num_of_upper_case + 1):
#     upper_generated += random.choice(upper_case)

# lower_generated = ""
# for lower_case_ in range(1, num_of_lower_case + 1):
#     lower_generated += random.choice(lower_case)

# number_generated = ""
# for numbers_ in range(1, num_of_numbers + 1):
#     number_generated += random.choice(numbers)

# symbols_generated = ""
# for symbols_ in range(1, num_of_symbols + 1):
#     symbols_generated += random.choice(symbols)

# password_generated = upper_generated + lower_generated + number_generated + symbols_generated
# print(f"Easy level password generator: {password_generated}")

# upper_generated = [random.choice(upper_case) for char in range(0, num_of_upper_case)]
# lower_generated = [random.choice(lower_case) for char in range(0, num_of_lower_case)]
# number_generated = [random.choice(numbers) for char in range(0, num_of_numbers)]
# symbols_generated = [random.choice(symbols) for char in range(0, num_of_symbols)]

# char_generated = upper_generated + lower_generated + number_generated + symbols_generated
# # random.shuffle(char_generated)
# # password = "".join(char_generated)
# # print(password)

# print(char_generated)
# print(type(char_generated))
