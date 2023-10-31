import unittest

from game_function import *


class DeckTestCase(unittest.TestCase):
    def test_create_deck(self):
        # Set up
        deck = create_deck()
        orig_list = deck[:]

        # Run the thing to test
        shuffle(deck)

        # Observe and check that things are as expected
        self.assertNotEqual(orig_list, deck)

    def test_deal(self):
        deck = create_deck()
        hand1 = create_hand()
        hand2 = create_hand()

        deal(deck, hand1, hand2)

        self.assertEqual(len(deck), NUM_CARDS_IN_DECK - 2 * (NUM_CARDS_IN_HAND))
        self.assertEqual(hand1['num_cards_in_hand'], NUM_CARDS_IN_HAND)
        self.assertEqual(hand2['num_cards_in_hand'], NUM_CARDS_IN_HAND)


class GameTestCase(unittest.TestCase):
    def test_is_legal_move(self):
        hand = create_hand()
        add_card_to_hand(hand, ('Ace', 'Diamonds', 'Red', 14))
        add_card_to_hand(hand, ('Jack', 'Hearts', 'Red' , 11))
        add_card_to_hand(hand, (10, 'Diamonds', 'Red', 10))
        add_card_to_hand(hand, ('Jack', 'Diamonds', 'Red', 11))

        result = is_legal_move(hand, ('Jack', 'Diamonds', 'Red', 11), ('Queen', 'Diamonds', 'Red', 12))

        self.assertTrue(result)

        result = is_legal_move(hand, ('Jack', 'Diamonds', 'Red', 11), ('Jack', 'Hearts', 'Red' , 11))
        self.assertFalse(result)

    def test_who_won(self):
        lead_card = (10, 'Hearts', 'Red', 10)               #name, suit, color, value
        followed_card = ('Jack', 'Clubs', 'Black', 11)    #name, suit, color, value
        trump = 'Clubs'

        result = who_won(lead_card, followed_card, 'Hearts')
        self.assertTrue(result)

        result = who_won(lead_card, followed_card, trump)
        self.assertFalse(result)

        result = who_won(lead_card, followed_card,'Diamonds')
        self.assertTrue(result)

    def test_return_hand_to_deck(self):
        deck = create_deck()
        deck_original_length = len(deck)
        hand1 = create_hand()
        hand2 = create_hand()

        deal(deck, hand1, hand2)
        self.assertTrue(deck_original_length == len(deck) + hand1['num_cards_in_hand'] +  hand2['num_cards_in_hand'])
        return_hand_to_deck(hand1, deck)
        self.assertTrue(deck_original_length == len(deck) + hand2['num_cards_in_hand'])
        return_hand_to_deck(hand2, deck)
        self.assertTrue(deck_original_length == len(deck))

    def test_take_player1_turn(self):
        deck = create_deck()
        hand1 = create_hand()
        hand2 = create_hand()
        deal(deck, hand1, hand2)
        head = hand1['first_card']['payload']
        self.assertTrue(is_card_in_hand(hand1, head))
        take_player1_turn(hand1, 'Clubs')
        self.assertFalse(is_card_in_hand(hand1, head))

    def test_sort_hand(self):
        trump = 'Spades'
        hand_golden = create_hand()     #golden sorted hand
        hand2 = create_hand()           #hand for testing

        add_card_to_hand(hand_golden, (9, 'Diamonds', 'Red', 9))
        add_card_to_hand(hand_golden, ('King', 'Diamonds', 'Red', 13))
        add_card_to_hand(hand_golden, ('Ace', 'Diamonds', 'Red', 14))
        add_card_to_hand(hand_golden, (9, 'Clubs', 'Black', 9))
        add_card_to_hand(hand_golden, (10, 'Clubs', 'Black', 10))
        add_card_to_hand(hand_golden, (9, 'Spades', 'Black', 9))
        add_card_to_hand(hand_golden, (10, 'Spades', 'Black', 10))

        add_card_to_hand(hand2, ('King', 'Diamonds', 'Red', 13))
        add_card_to_hand(hand2, ('Ace', 'Diamonds', 'Red', 14))
        add_card_to_hand(hand2, (9, 'Diamonds', 'Red', 9))
        add_card_to_hand(hand2, (9, 'Spades', 'Black', 9))
        add_card_to_hand(hand2, (10, 'Spades', 'Black', 10))
        add_card_to_hand(hand2, (9, 'Clubs', 'Black', 9))
        add_card_to_hand(hand2, (10, 'Clubs', 'Black', 10))
        hand2 = sort_hand(hand2, trump)

        index = hand_golden['first_card']
        index2 = hand2['first_card']
        while(index != None and index2 != None):
            self.assertEqual(index['payload'], index2['payload'])
            index = index['next_card']
            index2 = index2['next_card']

if __name__ == '__main__':
    unittest.main()
