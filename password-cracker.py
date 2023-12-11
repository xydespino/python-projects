import random
from datetime import datetime
# Guessing a number
# number = int(input("Input a number that is a password: "))
# guess = 0
# while (guess != number):
#     # Randomly
#     # guess = random.randint(0,9999)

#     guess += 1
#     print(guess)
# print("Your password is " + str(number))

# Guessing a password
character = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
character_list = list(character)
password = input("Enter your password: ")
guess = ""
startTime = datetime.now()
while (guess != password):
    guess = random.choices((character_list),k=len(password))
    # print(guess)
    guess = "".join(guess)
    # print(guess)


finishTime = datetime.now()
change = datetime.strftime(startTime-finishTime,'%H:%M:%S')
formatted_date = change.strftime(change,'%H:%M:%S')
print(formatted_date)
# print("Your password is " + guess + " and it took " +  formatted_date)