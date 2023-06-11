def hit(self):
        self.drawCard(self.player_cards, self.player_sum)
        self.label_player.setText(f"Player's Hand: {', '.join(self.player_cards)}")

        if self.player_sum[0] > 21:
            self.endGame("Crash")