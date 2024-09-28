import random

currentPlayer = ""
answer = ""

while answer != 'Y' and answer != 'N':
    answer = input("Do you want to start the game? (Y/N)").upper()
    if answer == 'Y':
        currentPlayer = "user"
    elif answer == 'N':
        currentPlayer = "computer"
    else:
        print("Invalid option!")

number = 0
arrOfNumbers = []

while number != 21:
    arrOfNumbersPlayer1 = []
    arrOfNumbersPlayer2 = []

    if currentPlayer == "computer":
        # computer move
        qtdOfMoves = random.randint(1, 3)
        for i in range(qtdOfMoves):
            number += 1
            numberConverted = [number]
            arrOfNumbersPlayer1.extend(numberConverted)
            if number == 21:
                break
        arrOfNumbers.extend(arrOfNumbersPlayer1)
        print(arrOfNumbers)
        if arrOfNumbers[-1] == 21:
            print("Computer lose. You win!")
            break
        currentPlayer = "user"
    else:
        # user move
        while True:
            while True:
                userInput = input("Enter a sequence up to 3 numbers separated by comma or just enter a single number: ")
                if userInput != "":
                    break
            userInputToList = userInput.split(",")
            arrOfNumbersPlayer2 = [int(num) for num in userInputToList] # userInputToIntList = list(map(int, userInputToList))
            is_consecutive = all(
                arrOfNumbersPlayer2[i] == arrOfNumbersPlayer2[i - 1] + 1 for i in range(1, len(arrOfNumbersPlayer2)))
            if arrOfNumbersPlayer2[0] == number + 1 and is_consecutive and len(arrOfNumbersPlayer2) <= 3:
                break

        arrOfNumbers.extend(arrOfNumbersPlayer2)
        if arrOfNumbers[-1] == 21:
            print("Computer wins! You lose!")
            break
        number += len(arrOfNumbersPlayer2)
        currentPlayer = "computer"




