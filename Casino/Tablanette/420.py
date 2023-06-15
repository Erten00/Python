import random
    # Check if both players have empty hands
    if not player1_hand and len(deck1) >= 4:
        player1_hand = deck1[:4]
        deck1 = deck1[4:]
    elif not player1_hand and len(deck1) > 0:
        player1_hand = deck1[:]
        deck1 = []
    if not player2_hand and len(deck2) >= 4:
        player2_hand = deck2[:4]
        deck2 = deck2[4:]
    elif not player2_hand and len(deck2) > 0:
        player2_hand = deck2[:]
        deck2 = []

# Create two decks of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck1 = [(rank) for rank in ranks]
deck2 = [(rank) for rank in ranks]

# Shuffle the decks
random.shuffle(deck1)
random.shuffle(deck2)

# Deal the cards to the players
player1_hand = deck1[:4]
player2_hand = deck2[:4]

# Check if player 1 played the last card on the board
    if card == board[-1] and card_opponent != board[-1]:
        player1_inventory.extend(board)
        board = []

    # Check if player 2 played the last card on the board
    if card_opponent == board[-1] and card != board[-1]:
        player2_score += len(board)
        board = []



import random


# Play the game
tricks = 6  # Number of tricks to play

player1_score = 0
player2_score = 0

for trick in range(tricks):
    table = []
    
    # Player 1's turn
    print("Player 1's turn:")
    print("Your hand:", player1_hand)
    card_index = int(input("Choose a card to play (enter the index): "))
    card = player1_hand.pop(card_index)
    table.append(card)
    
    # Player 2's turn
    print("Player 2's turn:")
    print("Your hand:", player2_hand)
    card_index = int(input("Choose a card to play (enter the index): "))
    card = player2_hand.pop(card_index)
    table.append(card)
    
    # Determine the winner of the trick
    winner = table.index(max(table, key=lambda x: (ranks.index(x[0]), suits.index(x[1]))))
    if winner == 0:
        player1_score += 1
        print("Player 1 wins the trick!")
    else:
        player2_score += 1
        print("Player 2 wins the trick!")
    
    print()
    print("Scores:")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)
    print()

# Determine the winner of the game
if player1_score > player2_score:
    print("Player 1 wins the game!")
elif player2_score > player1_score:
    print("Player 2 wins the game!")
else:
    print("It's a tie!")