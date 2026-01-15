import random;

has_magic_scroll = False
has_ankh_pendant = random.choice([True, False])

def solve_riddle(has_magic_scroll):
    attempts = 3
    for attempt in range(attempts):
        print(f"Attempt {attempt + 1} of {attempts} to solve the riddle.")
        if has_magic_scroll:
            print("Using the magic scroll, you easily solve the riddle!")
            return True
        wisdom_check = random.randint(1, 10)
        if wisdom_check > 7:
            print("You have solved the riddle with luck!")
            return True
        else:
            print("You could not solve the riddle.")
            attempt += 1
            if attempt == attempts:
                return False



def pass_mummy_tomb(had_ankh_pendant):
        if has_ankh_pendant:
            print("Using the Ankh pendant, you safely navigate the mummy's tomb.")
            return True
        disturb_mummies = random.choice([True, False])
        if disturb_mummies:
            print("You disturbed the mummies! You must try again.")
            return False
        else :
            print("You carefully navigate the tomb without disturbing the mummies.")
            return True

def survive_scorpions_den(has_ankh_pendant, has_magic_scroll):
    challenges = 2
    for i in range(challenges):
        print(f"Facing challenge {i + 1} in the scorpion's den.")
        if has_ankh_pendant and has_magic_scroll:
            print("With both the Ankh pendant and magic scroll, you easily survive the scorpion's den.")
            return True
        survival_check = random.random();
        if survival_check > 0.5 or has_ankh_pendant or has_magic_scroll:
            print("You successfully navigate this challenge.")
        else:
            print("You failed to navigate this challenge.")
            return False
    return True

if solve_riddle(has_magic_scroll):
    if pass_mummy_tomb(has_ankh_pendant):
        if survive_scorpions_den(has_ankh_pendant, has_magic_scroll):
            print("Congratulations! You have successfully completed your adventure!")
        else:
            print("You were unable to survive the scorpion's den. Game over.")
    else:
        print("You could not pass through the mummy's tomb. Game over.")