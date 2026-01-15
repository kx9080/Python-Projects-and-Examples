print("Hello World")

myname = input("What is your name")

print("Greetings, " + myname + " this works :)")
path = input("type forest if your brave or search to find another path")
if path.lower() == "forest":
    print("You enter the forest")
elif path.lower() == "search":
    print("you find a path to the dragon lair")

print("Quick lesson on variables")

hero_level = 1 #int
hero_name = myname #str
dragon_health = 150.0 #float
dragon_alive = True;

print("your level ", type(hero_level))

print("as you travel you find a potion that increases your level")
hero_level += 1
print("your new level", hero_level)

print("You encounter a merchant that will sell you magic arrows")
arrows = int(input("How many arrows do you want to buy? Earh arrow cost two GP."))
gold_spent = arrows * 2
print(f"you spend {gold_spent} GP on arrows")

print("You fight the dragon with your " + str(arrows) + " arrows wisely")

print("you defeat the dragon")

print(f"good job {hero_name}, ")