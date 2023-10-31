import unittest
from card_function import *

class CardNodeTestCase(unittest.TestCase):
    def test_create_card_node(self):
        card_node = create_card_node("my_payload")
        ## Because this is a unit test for "create_card_node()",
        ##  I'm willing to "break the abstraction" to make sure
        ##  it's correct
        self.assertEqual(card_node['payload'], 'my_payload')
        self.assertIsNone(card_node['prev_card'])
        self.assertIsNone(card_node['next_card'])

class HandTestCase(unittest.TestCase):

    def test_create_hand(self):
        hand = create_hand()
        self.assertIsNone(hand['first_card'])
        self.assertEqual(hand['num_cards_in_hand'], 0)

    def add_1card_to_hand_test(self):
        ## Set up
        hand = create_hand()
        card = ("jack", "hearts", 10)

        ## Execute the thing to test
        add_card_to_hand(hand, card)

        ## Evaluate the result for correctness
        self.assertEqual(hand['num_cards_in_hand'], 1)
        self.assertIs(get_card_from_node(hand['first_card']), card)

    def test_add_2cards_to_hand(self):
        ## Set up
        hand = create_hand()
        card = ("Jack", "Hearts", "Red" , 11)       #name, suit, color, value
        card2 = ("Queen", "Hearts", "Red", 12)      #name, suit, color, value

        ## Execute the thing to test
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)

        ## Evaluate the result for correctness
        self.assertEqual(hand['num_cards_in_hand'], 2)
        self.assertTrue(is_card_in_hand(hand, card))
        self.assertTrue(is_card_in_hand(hand, card2))
        self.assertIs(get_card_from_node(hand['first_card']), card2) ## This might depend on your implementation


    def test_remove_first_card_from_hand(self):
        ## Set up
        hand = create_hand()
        card = ("Jack", "Hearts", "Red" , 11)       #name, suit, color, value
        card2 = ("Queen", "Hearts", "Red", 12)      #name, suit, color, value
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)

        ## Execute the thing to test
        removed_card = remove_card_from_hand(hand, card)

        ## Evaluate the result for correctness
        self.assertEqual(hand['num_cards_in_hand'], 1)
        self.assertFalse(is_card_in_hand(hand, card))
        self.assertTrue(is_card_in_hand(hand, card2))
        self.assertEqual(is_suit_in_hand(hand, card2[1]), 1)
        self.assertEqual(is_suit_in_hand(hand, "clubs"), 0)
        self.assertIs(removed_card, card)
        self.assertIs(get_card_from_node(hand['first_card']), card2)


if __name__ == '__main__':
    unittest.main()