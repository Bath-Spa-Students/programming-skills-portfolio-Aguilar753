# Exercise 2: Movie Tickets

while True:

    print("How old are you?")

    Age = int(input())

    if Age < 3:

        print("Under the age of 3: free")

        Price = 0

    elif Age < 12:

        print("3 to 12: $10") 

        Price = 10

    else:
        print("Over 12: $15")

        Price = 15

    print("The cost of your ticket is:", Price)

    break