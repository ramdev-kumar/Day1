#PROJECT1 : Band Name Generator
"""
print("Welcome to the Band Name Generator")
city = input("What is the name of the city you grew up in? ")
pet = input("What is your pet's name?: ")
print("Your band name could be : " + city + " " + pet)
"""


#PROJECT2 : BMI
"""
print("Calculate your Body Mass Index\n")
weight = int(input("Enter your body weight in kgs: "))
height = int(input("Enter your height in cms: "))
bmi = weight/height
print(round(bmi, 2))
"""


#Projet3 : Tip calculator
"""
print("Calculate your bill\n")
total_bill = float(input("Enter the total amount of bill: "))
num_of_people = int(input("Enter how many of you are sharing: "))
tip_percentage = float(input("Enter how much percent you want to tip: "))
amount_with_tip = (tip_percentage/total_bill) * 100 + total_bill
each_pay = amount_with_tip/num_of_people
print(f"Each of you are paying {round(each_pay, 2)}")
"""

#Project4: Who will pay the Bill
"""
import random
friends = ['ram', 'liza', 'prayush', 'pranab']
#option1
print("\n",random.choice(friends))

#option2
random_index1 = (random.randint(0, len(friends) -1))
print(f"\n, {friends[random_index1]} will pay the bill.")

#option3
random_index2 = random.randint(0, 4)
print(f"\n{friends[random_index2]} will pay the bill")
"""

#Project5: FizzBuzz game
"""
'''
FizzBuzz
You are going to write a program that automatically prints the solution to the FizzBuzz game.
 These are the rules of the FizzBuzz game:
Your program should print each number from 1 to 100 in turn and include number 100.
But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FIzzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
"""

#Project6: Random Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8,', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+']

print("Welcome to random password generator.")
num_letters = int(input("How many letter would you like in your password.: "))
num_symbols = int(input("How many symbols would you like in your password. "))
num_numbers = int(input("How many number would you like in your password.: "))

 #EASY LEVEL
password = ""
for char in range(1, num_letters + 1): #for char in range(0, num_letters):
    password += random.choice(letters)

for char in range(1, num_numbers + 1):
    password += random.choice(numbers)

for char in range(1, num_symbols + 1):
    password += random.choice(symbols)
random.shuffle(password)
print(password)

#HARD LEVEL
password_list = []
for char in range(0, num_letters):
    password_list += random.choice(letters)
for char in range(0, num_numbers):
    password_list += random.choice(numbers)
for char in range(0, num_symbols):
    password_list += random.choice(symbols)
#print(password_list) = gives us the password in same pattern
random_order_of_password = random.shuffle(password_list)
#print(random_order_of_list) = gives us the password in list
only_string = ""
for char in password_list:
    only_string += char
print(only_string) #gives us in random pattern and in string








