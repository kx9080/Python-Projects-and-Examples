import random

def rollDice():
    return random.randint(1, 6)

def playerTurn():
    roundScore = 0
    print(f"\nStarting a new turn. Current round score: {roundScore}")
    while True:
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
            print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")
    return roundScore

def computerTurn():
    computerRoundScore = 0
    print(f"\nComputer's turn. Current round score: {computerRoundScore}")
    while computerRoundScore < 20:
        roll = rollDice()
        print(f"Computer rolled a {roll}.")
        if roll == 1:
            print("Computer rolled a 1! No points this round.")
            computerRoundScore = 0
            break
        else:
            computerRoundScore += roll
            print(f"Computer's current round score: {computerRoundScore}")
    print(f"Computer holds with a round score of {computerRoundScore}.")
    return computerRoundScore

def playGame():
    playerScores = 0
    currentRound = 0
    winningScore = 100

    while playerScores < winningScore:
        currentRound += 1
        print(f"\n Turn {currentRound}. Current score: {playerScores}")
        roundScore = playerTurn()
        playerScores += roundScore
        print(f"Total score: {playerScores}")

        print("-------------------------------")
        print(f"Now it is the computer's turn.")
        computerRoundScore = computerTurn()

        if playerScores >= winningScore:
            print(f"\n Player wins with a score of {playerScores}! And only after {currentRound} turns!")
            break

print("")
playGame()