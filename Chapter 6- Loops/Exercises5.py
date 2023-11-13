#Exercise 5: No Pastrami

Orders_of_sandwiches = ["Tuna sandwich" , "Hamburger" , "Egg salad sandwich" , "Pastrami" , "Panini" , "Ham sandwich"]

Completed_sandwiches = []

print("Unfortunately, there is no more pastrami availabe today.")

while "Pastrami" in Orders_of_sandwiches:

    Orders_of_sandwiches.remove("Pastrami")

print("\n")

while Orders_of_sandwiches:

    ongoing_sandwich = Orders_of_sandwiches.pop()

    print(f"I am working on your {ongoing_sandwich} sandwich.")

    Completed_sandwiches.append(ongoing_sandwich)

print("Below are the list of sandwiches that are finished")

for sandwiches in Completed_sandwiches:
    
    print(sandwiches)