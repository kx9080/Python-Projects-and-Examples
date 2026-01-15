import random

print("Welcome to the Mad Libs Game!")

if input("Do you want to use random choices? (yes/no): ").lower() == "yes":
    adjectives = ["brave", "curious", "mysterious", "cheerful"]
    nouns = ["dragon", "castle", "forest", "wizard"]
    verbs = ["fly", "explore", "cast spells", "dance"]
    adverbs = ["quickly", "silently", "happily", "bravely"]
    villagers = ["Alice", "Bob", "Charlie", "Diana"]

    adjective1 = random.choice(adjectives)
    noun1 = random.choice(nouns)
    verb1 = random.choice(verbs)
    adverb1 = random.choice(adverbs)
else:
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a action verb: ")
    adverb1 = input("Enter an adverb: ")

print("\nHere's your Mad Libs story:\n")
print(f"In a land far away was a very {adjective1} {noun1}. This {noun1} was very sought after because it could {verb1} very well. \nOne day, the {noun1} was taken, and everyone in the land was shocked. They all wanted their {noun1} back.")

if input("Do you want to use random choices for the next part? (yes/no): ").lower() == "yes":
    noun2 = random.choice(nouns)
    verb2 = random.choice(verbs)
    adverb2 = random.choice(adverbs)
    villager1 = random.choice(villagers)
    xVillagers = random.randint(5, 20)
    howLongIsTheLand = random.choice(["across three mountains", "through a dark forest", "over a wide river", "beyond the desert"])
else:
    noun2 = input("Enter another noun: ")
    verb2 = input("And another action verb: ")
    adverb2 = input("One more adverb: ")
    villager1 = input("Finally, name a brave villager: ")
    xVillagers = input("How many villagers are there: ")
    howLongIsTheLand = input("Describe how long the land is (e.g., 'across three mountains'): ")

print(f"\nThe people decided to {verb2} {adverb2} to find the missing {noun1}, they even had the brave villager {villager1}. After a long journey through the lands, across {howLongIsTheLand}, and the sacrifice of {xVillagers}, they finally found it in a cave guarded by a giant {noun2}.")

if input(f"Do they get the {noun1} back? Type yes if they do, and no if they don't: ") == "yes":
    print(f"They had to be very {adjective1} to get past the giant and retrieve their beloved {noun1}. In the end, they succeeded and returned home {adverb1} victorious!")
    print("\nThe End, feel free to play again!")
else:
    print(f"Unfortunately, the giant {noun2} was way too powerful for them. The people, including {villager1}, had to get out of there and leave their {noun1} behind. They returned home taking the loss, but they had vowed to one day return and take it back.")
    print("\nThe End, feel free to play again!")
