import sys
from random import randint

from game_function import *

PRINT_OUT_DECK = True
PRINT_P1_HAND = False


def print_trump(suit):
    print("\n\n*************************\n")
    print("**** Trump is %s *****\n" % suit)
    print("*************************\n\n")


def print_score(score1, score2):
    print("Player 1: %d\t\tPlayer 2: %d"  %(score1, score2))


# Returns 1 or 2, based on who won.
def play_round(game_deck):
    shuffle(game_deck)
    if PRINT_OUT_DECK:
        print_deck(game_deck)
    # Deal the hand
    p1hand = create_hand()
    p2hand = create_hand()

    deal(game_deck, p1hand, p2hand)

    if PRINT_P1_HAND:
        print("Player 1: \n")
        print_hand(p1hand)

    # For each round:

    # Determine trump Suit
    trump = get_card_suit(peek_card(game_deck))
    print_trump(trump)

    # Start playing.
    num_tricks = 0
    p1score = 0
    p2score = 0

    print("\n\n")
    print("Starting the round...")

    while num_tricks < NUM_CARDS_IN_HAND:
        print("\n---------------------\n")

        led_card = take_player1_turn(p1hand, trump)
        followed_card = take_player2_turn(p2hand, trump)
        #print("followed card:", followed_card)
        if is_legal_move(p2hand, led_card, followed_card):
            # figure out who won
            if who_won(led_card, followed_card, trump):
                print("Player 1 took the trick. \n")
                # P1 won
                p1score += 1

            else:
                print("Player 2 took the trick. \n")
                # P2 won
                p2score += 1

            print("\n")
            print_score(p1score, p2score)
            print("\n")

        else:
            # It was not a legal move; player 2 loses!
            print("\n\nPlayer 2 did not make a legal move!! \n")
            print("The round is over. \n")
            print("Player 1 wins by default. \n")
            p1score += 1

        # Put the cards back in the deck
        # so we don't "lose" them
        push_card_to_deck(game_deck, led_card)
        push_card_to_deck(game_deck, followed_card)

        num_tricks += 1

    print('\n\nPlayer %d won this round with %d tricks!\n'
          %(1 if (p1score > p2score) else 2,
          p1score if (p1score > p2score) else p2score))

    ## There probably shouldn't be any cards left in the hands at this point,
    ## but let's make sure they get returned anyway.
    return_hand_to_deck(p1hand, game_deck)
    return_hand_to_deck(p2hand, game_deck)

    return 1 if (p1score > p2score) else 2


def play_game(deck):
    num_rounds = 5
    player1score, player2score = 0, 0

    for i in range(0, num_rounds):
        print("\n\n===========================\n")
        print("Round # %d\n" %(i + 1))
        print("===========================\n\n")

        which_player_won = play_round(deck)

        if which_player_won == 1:
            player1score += 1
        else:
            player2score += 1

        print("\n\n\n")
        print("Game Score so far: \n")
        print_score(player1score, player2score)
        print("\n===========================\n\n")

        print("When you're ready, press <enter> to go to the next round. \n")
        which_one = input()

    print("\n\n")
    print("Player %d won the game!\n"
          % (1 if (player1score > player2score) else 2))

    print_score(player1score, player2score)

    print("\n\n")
    return 1 if (player1score > player2score) else 2


def main():
    print("Welcome to UW-Euchre!\n")
    print("When you're ready to play, press <enter>\n")
    user_input = input()

    print("Okay. ")
    game_deck = create_deck()

    if PRINT_OUT_DECK:
        print_deck(game_deck)

    print("Would you like to play a [R]ound or a [G]ame?\n")
    user_input = input()

    if user_input == 'R':
        play_round(game_deck)
    elif user_input == 'G':
        play_game(game_deck)
    else:
        print("Quitting the game. ")

    return 0


if __name__ == '__main__':
    sys.exit(main())