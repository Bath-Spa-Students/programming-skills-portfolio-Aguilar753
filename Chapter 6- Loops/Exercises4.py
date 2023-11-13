#Exercise 4: Deli

Orders_of_sandwiches = ["Tuna sandwich" , "Hamburger" , "Egg salad sandwich"]

Completed_sandwiches = []

while Orders_of_sandwiches:

    ongoing_sandwich = Orders_of_sandwiches.pop()

    print(f"I am working on your {ongoing_sandwich} sandwich.")

    Completed_sandwiches.append(ongoing_sandwich)

print("Below are the list of sandwiches that are finished")

for sandwiches in Completed_sandwiches:

    print(sandwiches)