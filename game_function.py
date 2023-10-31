from card_function import *
import random
#----------------------------------------
# Game functions
#----------------------------------------

# Shuffle the deck.
# Put them in a random order.
def shuffle(deck):
	random.shuffle(deck)
	return deck

# Given a deck (assume that it is already shuffled),
# take the top card from the deck and alternately give
# it to player 1 and player 2, until they both have
# NUM_DECKS_IN_HAND.
def deal(deck, p1_hand, p2_hand):
	for i in range(NUM_CARDS_IN_HAND):
		add_card_to_hand(p1_hand, pop_card(deck))
		add_card_to_hand(p2_hand, pop_card(deck))
	return

# Given a lead card, a players hand, and the card the player wants
# to play, is it legal?
# If the player has a card of the same suit as the lead_card, they
# must play a card of the same suit.
# If the player does not have a card of the same suit, they can
# play any card.
def is_legal_move(hand, lead_card, played_card):
	if (is_suit_in_hand(hand, get_card_suit(lead_card))) and (get_card_suit(lead_card) != get_card_suit(played_card)):
		#print("lead_card suit", get_card_suit(lead_card))
		#print("followed_card suit", get_card_suit(played_card))
		#print("is_suit_in_hand", is_suit_in_hand(hand, get_card_suit(lead_card)))
		return False  #if suit is in hand & not played card, [1]: suit
	else:
		return True

# Given two cards that are played in a hand, which one wins?
# If the suits are the same, the higher card value wins.
# If the suits are not the same, player 1 wins, unless player 2 played trump.
# Returns True if the person who lead won, False if the person who followed won.
def who_won(lead_card, followed_card, trump):
	if (get_card_suit(lead_card) == get_card_suit(followed_card)):
		if lead_card[3] > followed_card[3]: #same suit & lead wons with larger value
			return True
		else:
			return False   					#same suit & followed wons with larger value
	elif(get_card_suit(followed_card) == trump):
		return False						#different suit, followed play trump
	else:
		return True							#different suit, lead wons

# Take all the cards out of a given hand, and put them
# back into the deck.
def return_hand_to_deck(hand, deck):
	while(is_hand_empty(hand)):  # while(hand)????
		push_card_to_deck(deck, get_card_from_hand(hand, 0))

# Sort the given hand in descending order of power.
# The sort order should be: all cards of the given trump suit should
# be the "highest", and A high down to 9;
# The other suits can be in random order, but the card values must go
# from high to low.
def sort_hand(hand, trump):
	suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
	deck = {}
	deck['Diamonds'] = []
	deck['Hearts'] = []
	deck['Spades'] = []
	deck['Clubs'] = []

######### separate cards with suit and save in dictionary(deck) #############
	index = hand['first_card']
	while (index != None):
		if get_card_suit(index['payload']) == suits[0]:
			deck[suits[0]].append(index['payload'])
		elif get_card_suit(index['payload']) == suits[1]:
			deck[suits[1]].append(index['payload'])
		elif get_card_suit(index['payload']) == suits[2]:
			deck[suits[2]].append(index['payload'])
		elif get_card_suit(index['payload']) == suits[3]:
			deck[suits[3]].append(index['payload'])
		index = index['next_card']
################# sort each suit in each dictionary value #######################
	for suit in suits:
		i = 0
		while (i < len(deck[suit])):
			j = i + 1
			while (j < len(deck[suit])):
				if deck[suit][i][3] > deck[suit][j][3]:
					temp = deck[suit][i]
					deck[suit][i] = deck[suit][j]
					deck[suit][j] = temp
				j += 1
			i += 1
###########add card in descending order to new_hand ########
	new_hand = create_hand()
	for suit in suits: #add each sorted suit in new_hand
		i = 0
		while(i < len(deck[suit]) and suit != trump):
			add_card_to_hand(new_hand, deck[suit][i])
			i += 1
	### add sorted trump in new hand (higher power)
	i = 0
	while (i < len(deck[trump])):
		add_card_to_hand(new_hand, deck[trump][i])
		i += 1
	return new_hand


# Given the player1 hand, play a card.
# Player 1 is always the computer.
# This function should choose a card from the hand,
# remove it from the hand, print out a message
# saying what card was played, and return the played card.
def take_player1_turn(hand, trump):
	played_card = get_card_from_hand(hand, 0)
	print("\n", played_card, ' was played by player 1.')
	return played_card

# Given the player2 hand, play a card.
# Player 2 is always a human.
# This function should prompt the user to choose a card to play.
# It probably should print out the cards that are available to play.
# Once the human player chooses,
# remove it from the hand, print a message
# saying what card was played, and return the played card.
# This function does not have to enforce that a valid card is chosen.
def take_player2_turn(hand, trump):
	i = hand['first_card']
	print("\n", "Cards in hand:")
	for index in range(hand['num_cards_in_hand']):
		print(index, " : ", i['payload'])
		i = i['next_card']
	print("please choose card to play: (type in index)")
	p2_card_index = int(input())
	p2_card = get_card_from_hand(hand, p2_card_index)
	print(p2_card, " was played by player 2.")
	return p2_card

## Helper function to return the Suit of a given card
def get_card_suit(card):
	return card[1]