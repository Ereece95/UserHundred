# This is a sample Python script.
# Eric Reece
# 1/2/2021
# Date calculator - program to calculate user's current age, the current year, and when
#   user will turn 100 years old.
import datetime

if __name__ == '__main__':
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    num_copies = int(input("Enter a number of copies to be printed: "))
    print('Hello, ' + user_name + '.\nYou are: ' + str(user_age) + ' years old.')
    user_hundred = (datetime.datetime.now().year - user_age) + 99
    print(num_copies * ("\nYou will be 100 years old in: " + str(user_hundred)))
