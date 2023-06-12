import random

# Create a deck of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank) for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Deal the cards to the players
player1_hand = deck[:4]
player2_hand = deck[4:8]

# Play the game
player1_score = 0
player2_score = 0
trick = 0
board = []

while True:
    trick += 1
    print(f"Trick {trick}")

    # Player 1's turn
    print("Player 1's turn:")
    print("Your hand:", player1_hand)
    card_index = int(input("Choose a card to play (enter the index): "))
    card = player1_hand.pop(card_index)
    board.append(card)

    # Player 2's turn
    print("Player 2's turn:")
    print("Your hand:", player2_hand)
    card_index = int(input("Choose a card to play (enter the index): "))
    card = player2_hand.pop(card_index)
    board.append(card)

    print("\nBoard:", board)

    # Check if any player has no cards left
    if not player1_hand:
        player1_score += len(board)
        print("Player 1 wins the trick!")
        board = []
        if len(deck) >= 4:
            player1_hand = deck[:4]
            deck = deck[4:]
        else:
            player1_hand = deck[:]
            deck = []
    elif not player2_hand:
        player2_score += len(board)
        print("Player 2 wins the trick!")
        board = []
        if len(deck) >= 4:
            player2_hand = deck[:4]
            deck = deck[4:]
        else:
            player2_hand = deck[:]
            deck = []

    print()
    print("Scores:")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)
    print()

    # Check if any player has played their last card and the deck is empty
    if not player1_hand and not player2_hand and not deck:
        break

# Determine the winner of the game
if player1_score > player2_score:
    print("Player 1 wins the game!")
elif player2_score > player1_score:
    print("Player 2 wins the game!")
else:
    print("It's a tie!")