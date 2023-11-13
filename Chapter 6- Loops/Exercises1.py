#Exercise 1: Pizza Toppings

while True:

    toppings = input("Which toppings would you like to have on your pizza?")

    quit_prompt = input("Enter 'quit' when you are finished: ")

    if quit_prompt == 'quit': 

        break

    print(f"I will add an additional {toppings.title()} to your pizza.")
    