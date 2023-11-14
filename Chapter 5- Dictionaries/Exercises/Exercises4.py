# Exercise 4: Rivers

Rivers = {
         "The Murray River": "Australia",

         "Volga River": "Russia",

         "Nile River": "Egypt",

         "Loire River": "France",

         "The Yangtze River": "China",
         }

for Famous_Rivers, Country in Rivers.items():

    print(f"\n There is a river called the {Famous_Rivers} that runs through {Country}")

print("\nThese are the most 5 famous rivers around the world!:")

for River in Rivers.keys():

    print(f"\n * {River}")