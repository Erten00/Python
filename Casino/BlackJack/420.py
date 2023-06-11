def hit(self):
        self.drawCard(self.player_cards, self.player_sum)
        self.label_player.setText(f"Player's Hand: {', '.join(self.player_cards)}")

        if self.player_sum[0] > 21:
            self.endGame("Crash")


    def drawCard(self, hand, hand_sum):
    card_index = random.randint(0, len(self.cards) - 1)
    card = self.cards[card_index]
    card_value = self.cards_value[card_index]
    hand.append(card)

    if card_value == 11 and hand_sum + card_value > 21:
        card_value = 1

    hand_sum += card_value

    # Update the dealer_sum attribute when drawing cards for the dealer
    if hand is self.dealer_cards:
        self.dealer_sum = hand_sum

    self.player_sum = hand_sum


    def drawCard(self, hand, hand_sum):
    card_index = random.randint(0, len(self.cards) - 1)
    card = self.cards[card_index]
    card_value = self.cards_value[card_index]
    hand.append(card)

    if card_value == 11 and hand_sum + card_value > 21:
        card_value = 1

    hand_sum += card_value

    # Update the dealer_sum attribute when drawing cards for the dealer
    if hand is self.dealer_cards:
        self.dealer_sum = hand_sum

    self.player_sum = hand_sum


    def drawCard(self, hand, hand_sum):
    card_index = random.randint(0, len(self.cards) - 1)
    card = self.cards[card_index]
    card_value = self.cards_value[card_index]
    hand.append(card)

    if card_value == 11 and hand_sum + card_value > 21:
        card_value = 1

    hand_sum += card_value

    # Update the dealer_sum attribute when drawing cards for the dealer
    if hand is self.dealer_cards:
        self.dealer_sum = hand_sum

    self.player_sum = hand_sum