## Original code https://github.com/GustavSkou/Blackjack

import random
import Cards

Cards.cards
Cards.cards_value

money = 100
money_won = 0
money_lost = 0

playing = input("Is it Blackjack time? (yes/no) ")

while playing == "yes" or playing == "y":
    # Creating empty lists for the hands to be generated into
    dealer_cards = []
    dealer_cards_value = []
    player_cards = []
    player_cards_value = []

    player_crash = False
    dealer_crash = False
    player_sum = 0
    dealer_sum = 0
    allow_bet = 0

    print("You have", money)
    bet = input("Bet: ")
    Bet = int(bet)
    while allow_bet == 0:
        if Bet <= money:
            money = money - Bet
            allow_bet = 1
        else:
            bet = input("Try again. Bet: ")
            Bet = int(bet)

    def gen_dealer_card():
        ran = random.randint(0, 12)
        dealer_cards.append(Cards.cards[ran])
        dealer_cards_value.append(Cards.cards_value[ran])

    def gen_player_card():
        ran = random.randint(0, 12)
        player_cards.append(Cards.cards[ran])
        player_cards_value.append(Cards.cards_value[ran])

    while len(dealer_cards) != 2:
        gen_dealer_card()
        dealer_new_card = dealer_cards_value[-1]

        if dealer_new_card != 11:
            dealer_sum += dealer_new_card
        elif dealer_sum + 11 <= 21:
            dealer_sum += 11
        else:
            dealer_sum += 1

    while len(player_cards) != 2:
        gen_player_card()
        player_new_card = player_cards_value[-1]

        if player_new_card != 11:
            player_sum += player_new_card
        elif player_sum + 11 <= 21:
            player_sum += 11
        else:
            player_sum += 1

    print("Player:", player_cards[0], ",", player_cards[1], ":", player_sum)
    print("Dealer:", dealer_cards[0], ":", dealer_cards_value[0])

    while player_sum < 21:
        choice = input("Stand or Hit: ")
        if choice == "stand":
            print("Player:", player_cards, ":", player_sum)
            print("Dealer:", dealer_cards, ":", dealer_sum)
            break
        elif choice == "hit":
            gen_player_card()
            player_new_card = player_cards_value[-1]

            if player_new_card != 11:
                player_sum += player_new_card
            elif player_sum + 11 <= 21:
                player_sum += 11
            else:
                player_sum += 1

            print("Player:", player_cards, player_sum)
            print("Dealer:", dealer_cards, dealer_sum)

    while dealer_sum < 16:
        gen_dealer_card()
        dealer_new_card = dealer_cards_value[-1]

        if dealer_new_card != 11:
            dealer_sum += dealer_new_card
        elif dealer_sum + 11 <= 21:
            dealer_sum += 11
        else:
            dealer_sum += 1

        print("Dealer:", dealer_cards, dealer_sum)

    if player_sum > 21:
        player_crash = True
    if dealer_sum > 21:
        dealer_crash = True

    if player_sum == 21:
        money += Bet * 3 + Bet
        print("Blackjack +", Bet * 3)
    elif player_sum == dealer_sum or (dealer_crash and player_crash):
        money += Bet
        print("Tie")
    elif player_sum > 21:
        print("Crash -", Bet)
    elif dealer_sum > 21 or player_sum > dealer_sum:
        money += Bet * 2 + Bet
        print("Win +", Bet * 2)
    elif player_sum < dealer_sum:
        print("Lost -", Bet)

    answer = 0
    while answer == 0:
        playing = input("Play again? (yes/no) ")
        if playing == "yes" or playing == "no":
            answer = 1
        else:
            answer = 0