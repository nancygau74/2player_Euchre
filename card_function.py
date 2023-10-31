NUM_CARDS_IN_HAND = 5
NUM_CARDS_IN_DECK = 24

SUITS = ["Clubs", "Spades", "Hearts", "Diamonds"]
FACES = ["Jack", "Queen", "King", "Ace"]
NUMBERED = [9, 10]
VALUES = [9, 10, 11, 12 ,13, 14]  # Jack = 11; Queen = 12; King = 13; Ace = 14
COLOR_BLACK = "Black"
COLOR_RED = "Red"

## card is a tuple of (name, suit, color, value)

## deck is a list structured as a stack

## card_node is a dict of {next_card, prev_card, payload}

## hand is a linked list, represented by a dict of {first_card, num_cards_in_hand}

# ----------------------------------------
#  Deck functions
# ---------------------------------------

# Creates the deck, initializing any fields necessary.
# Returns a deck.
def create_deck():
	deck = []
	for s in SUITS:
		for i in range(len(VALUES)):
			if s =="Clubs" or s == "Spades":  # Cards in Black
				deck.append(((NUMBERED + FACES)[i],s,COLOR_BLACK,VALUES[i])) 				#name, suit, color, value
			elif s =="Hearts" or s == "Diamonds": #Cards in Red
				deck.append(((NUMBERED + FACES)[i],s,COLOR_RED,VALUES[i]))  					#name, suit, color, value
	return deck

# Adds a card to the top of the deck.
# Returns a pointer to the deck.
def push_card_to_deck(deck, card):
	deck.append(card)
	return deck

# Shows the top card, but does not remove it from the stack.
# Returns a pointer to the top card.
def peek_card(deck):
	print(deck[len(deck)-1])
	return deck[len(deck)-1]

# Removes the top card from the deck and returns it.
# Returns a pointer to the top card in the deck.
def pop_card(deck):
	return deck.pop()

# Determines if the deck is empty.
# Returns 0 if the Deck has any cards; 1 otherwise.
def is_deck_empty(deck):
	return int(len(deck) == 0)

## Prints the provided deck
def print_deck(deck):
	print(deck)

#----------------------------------------
# Hand functions
#----------------------------------------

## A Hand is a linked list, so we define Card_Nodes before
## defining the Hand

## card_node is a dict of {next_card, prev_card, payload}

def create_card_node(card):
	return {'next_card': None , 'prev_card': None, 'payload': card}

def get_next_card_node(card_node):
	next_node = card_node['next_card']
	return next_node
def get_prev_card_node(card_node):
	prev_node = card_node['prev_card']
	return prev_node

def get_card_from_node(card_node):
	return card_node['payload']

# Creates a Hand and initializes any necessary fields.
# Returns a new empty hand

## hand is a linked list, represented by a dict of {first_card, num_cards_in_hand}
def create_hand():
	hand = {'first_card': None, 'num_cards_in_hand': 0}
	return hand

# Adds a card to the hand.
def add_card_to_hand(hand, card):
	new_card = create_card_node(card)
	if hand['num_cards_in_hand'] == 0:
		#print('num_cards_in_hand is 0')
		hand['first_card'] = new_card
	else:  								#add card to head in hand
		temp = hand['first_card']		#temp: record original head
		hand['first_card'] = new_card 	#make new card the head
		new_card['next_card'] = temp
		temp['prev_card'] = new_card
	hand['num_cards_in_hand'] += 1
	return hand

# Removes a card from the hand via card value
# Returns the card (not a card_node) that was removed from the hand
# Returns None if the specified card is not in the hand
def remove_card_from_hand(hand, card):
	index = hand['first_card']			#index: parse through hand
	while(index != None):
		#print('in loop')
		if (index['payload'] == card): #found & delete card node
			if (index == hand['first_card']) :	#if card is found as "head"
				#print('card to delete is found at head')
				hand['first_card'] = index['next_card']
				if(index['next_card'] != None): #if only 1 node left
					index['next_card']['prev_card'] = None
			elif (index['next_card'] != None):  	#card is found in the middle
				#print('card to delete is found and in the middle')
				index['prev_card']['next_card'] = index['next_card']
				index['next_card']['prev_card'] = index['prev_card']
			else:								#card is found as "tail"
				#print('card to delete is found at end ')
				index['prev_card']['next_card'] = None
			hand['num_cards_in_hand'] -= 1
			#print('return delete card', index['payload'])
			return index['payload']
		else:      						#if card not found, parse to next node
			index = index['next_card']
	return None							#card not in hand

# Removes a card from the hand via index
# Returns the card, not a card_node
# Returns None if index is < 0 or greater than the length of the hand/list.
def get_card_from_hand(hand, index):
	i = hand['first_card'] 		#i: parse through hand
	if (index < 0) or (index > hand['num_cards_in_hand']):
		return None
	round = 0
	while ( round <= index ):
		if round == index:		#round: parse through index
			remove_card_from_hand(hand, i['payload'])
			return i['payload']
		else:
			i = i['next_card']
		round += 1

#return True if card is found in hand
def is_card_in_hand(hand, card):
	index = hand['first_card']			#index: parse through hand
	while(index != None):
		if (index['payload'] == card): #found & delete card node
			return True
		else:      						#if card not found, parse to next node
			index = index['next_card']
	return False

#Find if the specific suit is in hand
#If found return 1, else 0.
def is_suit_in_hand(hand, suit):
	index = hand['first_card']			#index: parse through hand
	while(index != None):
		if (index['payload'][1] == suit): #found suit
			return 1
		else:      						#if card not found, parse to next node
			index = index['next_card']
	return 0

# Determines if there are any cards in the hand.
# Return 0 if the hand is empty; 1 otherwise.
def is_hand_empty(hand):
	return int(hand['num_cards_in_hand'] != 0)

# Prints a single card
def print_card(card):
	print(card)

# Prints an entire hand
def print_hand(hand):
	print(hand)