import random


first_number = 1
random_number = random.randint(1,150)

for num in range(first_number, random_number):
    if num > 1:
        ### this checks if any number is divisible by 2 and any number between whatever the random number is. If it is it means its not a prime number and breaks. if it isnt. it prints the "num"
        for i in range(2, num):
            if  num% i == 0:
                break
        else:
            print(num, end=", ")
