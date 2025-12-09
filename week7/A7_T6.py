# main.py

import random
random.seed(1234)

# Get player name
name = input("Enter your name: ").strip()
print(f"\nWelcome, {name}!")
print("Your opponent is: RPS-3PO")
print("The game is starting...")

while True:
    print("\n1. Rock\n2. Paper\n3. Scissors\n4. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        continue
    
    if choice == 4:
        print(f"\nGoodbye, {name}!")
        break
    
    if choice not in [1, 2, 3]:
        continue
    
    # Play round
    print("\nRock! Paper! Scissors! Shoot!\n")
    
    # Player choice
    if choice == 1:
        player = "Rock"
        p_art = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
    elif choice == 2:
        player = "Paper"
        p_art = "     _______\n---'    ____)____\n           ______)\n          _______)\n         _______)\n---.__________)"
    else:
        player = "Scissors"
        p_art = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"
    
    print(f"{name} chose: {player}")
    print(p_art)
    print("\n" + "#" * 25 + "\n")
    
    # Bot choice
    bot = random.randint(1, 3)
    if bot == 1:
        bot_name = "Rock"
        b_art = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
    elif bot == 2:
        bot_name = "Paper"
        b_art = "     _______\n---'    ____)____\n           ______)\n          _______)\n         _______)\n---.__________)"
    else:
        bot_name = "Scissors"
        b_art = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"
    
    print(f"RPS-3PO chose: {bot_name}")
    print(b_art)
    
    # Determine winner
    if choice == bot:
        print(f"\nDraw! Both players chose {player}.")
    elif (choice == 1 and bot == 3) or (choice == 2 and bot == 1) or (choice == 3 and bot == 2):
        # Player wins
        if choice == 1:
            print(f"\n{name} wins! Rock beats Scissors.")
        elif choice == 2:
            print(f"\n{name} wins! Paper beats Rock.")
        else:
            print(f"\n{name} wins! Scissors beats Paper.")
    else:
        # Bot wins
        if bot == 1:
            print("\nRPS-3PO wins! Rock beats Scissors.")
        elif bot == 2:
            print("\nRPS-3PO wins! Paper beats Rock.")
        else:
            print("\nRPS-3PO wins! Scissors beats Paper.")