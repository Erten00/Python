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