import random
import time;

roundScore = 0
computerRoundScore = 0

def rollDice():
    return random.randint(1, 6)
    # Roll a dice in its own function for some reason I guess

def playerTurn():
    roundScore = 0
    print(f"\nStarting a new turn. Current round score: {roundScore}")
    while True:
        # Prompt player for action
        choice = input("Roll or Hold? (r/h): ").lower().strip()
        if choice == 'r' or choice == 'roll':
            roll = rollDice()
            print(f"You rolled a {roll}.")
            if roll == 1:
                print("Rolled a 1! No points this round.")
                roundScore = 0
                break
            else:
                roundScore += roll
                print(f"Current round score: {roundScore}")
        elif choice == 'h' or choice == 'hold':
            print(f"You hold with a round score of {roundScore}.")
            break
        else:
            # Have a fallback for invalid input
            print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")
    return roundScore

def computerTurn():
    # Set starting score to 0
    computerRoundScore = 0
    print(f"\nComputer's turn. Current round score: {computerRoundScore}")
    
    # Computer will roll until it reaches a random number between 5 and 25
    while computerRoundScore < random.randint(5, 25):
        roll = rollDice()
        print(f"Computer rolled a {roll}.")
        if roll == 1:
            print("Computer rolled a 1! No points this round.")
            computerRoundScore = 0
            break
        else:
            computerRoundScore += roll
            print(f"Computer's current round score: {computerRoundScore}")
        time.sleep(1)  # Pause for dramatic effect
    print(f"Computer holds with a round score of {computerRoundScore}.")
    return computerRoundScore

def playGame():
    playerScores = 0
    computerScores = 0
    currentRound = 0
    winningScore = 100

    # Game loop

    while playerScores < winningScore or computerScores < winningScore:
        currentRound += 1
        print(f"\n Turn {currentRound}. Current score (Player): {playerScores}, (Computer): {computerScores}")
        roundScore = playerTurn()

        playerScores += roundScore
        
        # Doublely handle wins
        if playerScores >= winningScore:
            print(f"\n Player wins with a score of {playerScores}! And only after {currentRound} turns!")
            break
        elif computerScores >= winningScore:
            print(f"\n Computer wins with a score of {computerScores}! And only after {currentRound} turns!")
            break
        
        print(f"Total score: {playerScores}")

        print("-------------------------------")
        print(f"Now it is the computer's turn.")
        computerRoundScore = computerTurn()
        computerScores += computerRoundScore
        
        # Handle wins
        if playerScores >= winningScore:
            print(f"\n Player wins with a score of {playerScores}! And only after {currentRound} turns!")
            break
        elif computerScores >= winningScore:
            print(f"\n Computer wins with a score of {computerScores}! And only after {currentRound} turns!")
            break


print("")
playGame()