
#  File: Poker.py

#  Description: This Python program simulates a poker game 
#  for 2 to 6 players. It deals hands, evaluates their ranks, and 
#  determines the winner. Ties are handled, and the winning hand is displayed.

#  Student's Name: Alexander Romero-Barrionuevo

#  Student's UT EID: ANR3784    

#  Partner's Name: Dylan Lam
    
#  Partner's UT EID: DXL85

#  Course Name: CS 313E 

#  Unique Number: 52605

#  Date Created: 9/25/2025

#  Date Last Modified: 9/25/2023

import sys, random

class Card (object):
	RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

	SUITS = ('C', 'D', 'H', 'S')

	# constructor
	def __init__ (self, rank = 12, suit = 'S'):
		if (rank in Card.RANKS):
			self.rank = rank
		else:
			self.rank = 12

		if (suit in Card.SUITS):
			self.suit = suit
		else:
			self.suit = 'S'

	# string representation of a Card object
	def __str__ (self):
		if (self.rank == 14):
			rank = 'A'
		elif (self.rank == 13):
			rank = 'K'
		elif (self.rank == 12):
			rank = 'Q'
		elif (self.rank == 11):
			rank = 'J'
		else:
			rank = str (self.rank)
		return rank + self.suit

	# equality tests
	def __eq__ (self, other):
		return self.rank == other.rank

	def __ne__ (self, other):
		return self.rank != other.rank

	def __lt__ (self, other):
		return self.rank < other.rank

	def __le__ (self, other):
		return self.rank <= other.rank

	def __gt__ (self, other):
		return self.rank > other.rank

	def __ge__ (self, other):
		return self.rank >= other.rank

class Deck (object):
	# constructor
	def __init__ (self, num_decks = 1):
		self.deck = []
		for i in range (num_decks):
			for suit in Card.SUITS:
				for rank in Card.RANKS:
					card = Card (rank, suit)
					self.deck.append (card)

	# shuffle the deck
	def shuffle (self):
		random.shuffle (self.deck)

	# deal a card
	def deal (self):
		if (len(self.deck) == 0):
			return None
		else:
			return self.deck.pop(0)

class Poker (object):
	# constructor
	def __init__ (self, num_players = 2, num_cards = 5):
		self.deck = Deck()
		self.deck.shuffle()
		self.players_hands = []
		self.numCards_in_Hand = num_cards

		# Print the number of players
		print("\nNumber of players:", num_players, "\n")

		# deal the cards to the players
		for i in range (num_players):
			# Print the number of players
			hand = []
			for j in range (self.numCards_in_Hand):
				hand.append (self.deck.deal())
			self.players_hands.append (hand)

	# simulate the play of poker
	def play (self):
		# sort the hands of each player and print
		for i in range (len(self.players_hands)):
			sorted_hand = sorted (self.players_hands[i], reverse = True)
			self.players_hands[i] = sorted_hand
			hand_str = ''
			for card in sorted_hand:
				hand_str = hand_str + str (card) + ' '
			print ('Player ' + str(i + 1) + ' : ' + hand_str)
		print('')

		# determine the type of each hand and print
		hand_type = []	# create a list to store type of hand
		hand_points = []	# create a list to store points for hand


		for i in range(len(self.players_hands)):
			hand = self.players_hands[i]

			# Run each player hand through the hand types
			hand_checkers = [
				self.is_royal,
				self.is_straight_flush,
				self.is_four_kind,
				self.is_full_house,
				self.is_flush,
				self.is_straight,
				self.is_three_kind,
				self.is_two_pair,
				self.is_one_pair,
				self.is_high_card
			]

			# Check each hand type and store the points and type
			for checker in hand_checkers:
				points, hand_type_str = checker(hand)
				if points > 0:
					hand_type.append(hand_type_str)
					hand_points.append(points)
					break  # Stop checking when the first valid hand type is found

		# Create a dictionary to count occurrences of each hand type
		hand_type_count = {}

		# Count the occurrences of each hand type
		for ht in hand_type:
			if ht in hand_type_count:
				hand_type_count[ht] += 1
			else:
				hand_type_count[ht] = 1

		# Find the highest hand type
		highest_hand_type = max(hand_type_count, key=lambda x: hand_points[hand_type.index(x)])

		# Find the players with the highest hand type
		tied_winners = [i for i, ht in enumerate(hand_type) if ht == highest_hand_type]

		for i in range(len(self.players_hands)):
			print(f"Player {i + 1}: {hand_type[i]}")

		# Output the winners or tied players in descending values
		print('')
		if hand_type_count[highest_hand_type] == 1:
			print(f"Player {tied_winners[0] + 1} wins.")
		else:
		    # Sort tied players by point values in descending order
			tied_winners = sorted(tied_winners, key=lambda x: hand_points[x], reverse=True)
			for winner in tied_winners:
				print(f"Player {winner + 1} ties.")



	def is_royal(self, hand):
		# Check if all cards in the hand have the same suit
		same_suit = all(card.suit == hand[0].suit for card in hand)
		
		# Check if the ranks of cards form a descending order starting from 14 (Ace)
		rank_order = all(card.rank == 14 - i for i, card in enumerate(hand))

		if same_suit and rank_order:
			# Calculate and return a unique score for a Royal Flush, and its name
			return 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 \
				+ (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Royal Flush'
		else:
			# Return a score of 0 if not a Royal Flush
			return 0, ''


	def is_straight_flush(self, hand):
		# Check if all cards in the hand have the same suit
		same_suit = all(card.suit == hand[0].suit for card in hand)
		
		# Check if the ranks of cards form a consecutive sequence
		rank_order = all(card.rank == hand[0].rank - i for i, card in enumerate(hand))

		if same_suit and rank_order:
			# Calculate and return a unique score for a Straight Flush, and its name
			return 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 \
				+ (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Straight Flush'
		else:
			# Return a score of 0 if not a Straight Flush
			return 0, ''


	def is_four_kind(self, hand):
		# Count the occurrences of each rank in the hand
		rank_count = {}
		for card in hand:
			if card.rank not in rank_count:
				rank_count[card.rank] = 1
			else:
				rank_count[card.rank] += 1

		for rank, count in rank_count.items():
			if count == 4:
				# Calculate and return a unique score for Four of a Kind, and its name
				return 8 * 15 ** 5 + (rank) * 15 ** 4 + (rank) * 15 ** 3 \
					+ (rank) * 15 ** 2 + (rank) * 15 ** 1 + (hand[4].rank), 'Four of a Kind'

		# Return a score of 0 if not Four of a Kind
		return 0, ''


	def is_full_house(self, hand):
		# Count the occurrences of each rank in the hand
		rank_count = {}
		for card in hand:
			if card.rank not in rank_count:
				rank_count[card.rank] = 1
			else:
				rank_count[card.rank] += 1

		three_kind_rank = None
		two_pair_rank = None

		for rank, count in rank_count.items():
			if count == 3:
				three_kind_rank = rank
			elif count == 2:
				two_pair_rank = rank

		if three_kind_rank is not None and two_pair_rank is not None:
			# Calculate and return a unique score for a Full House, and its name
			return 7 * 15 ** 5 + (three_kind_rank) * 15 ** 4 + (three_kind_rank) * 15 ** 3 \
				+ (three_kind_rank) * 15 ** 2 + (two_pair_rank) * 15 ** 1 + (two_pair_rank), 'Full House'

		# Return a score of 0 if not a Full House
		return 0, ''


	def is_flush(self, hand):
		# Check if all cards in the hand have the same suit
		same_suit = all(card.suit == hand[0].suit for card in hand)

		if same_suit:
			# Calculate and return a unique score for a Flush, and its name
			return 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 \
				+ (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Flush'
		else:
			# Return a score of 0 if not a Flush
			return 0, ''


	def is_straight(self, hand):
		# Check if the ranks of cards form a consecutive sequence
		rank_order = all(card.rank == hand[0].rank - i for i, card in enumerate(hand))

		if rank_order:
			# Calculate and return a unique score for a Straight, and its name
			return 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 \
				+ (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Straight'
		else:
			# Return a score of 0 if not a Straight
			return 0, ''


	def is_three_kind(self, hand):
		# Count the occurrences of each rank in the hand
		rank_count = {}
		for card in hand:
			if card.rank not in rank_count:
				rank_count[card.rank] = 1
			else:
				rank_count[card.rank] += 1

		three_kind_rank = None
		side_card_ranks = []

		for rank, count in rank_count.items():
			if count == 3:
				three_kind_rank = rank
			else:
				side_card_ranks.append(rank)

		if three_kind_rank is not None:
			# Sort the side card ranks in descending order and calculate a unique score for Three of a Kind
			side_card_ranks.sort(reverse=True)
			return 4 * 15 ** 5 + (three_kind_rank) * 15 ** 4 + (three_kind_rank) * 15 ** 3 \
				+ (three_kind_rank) * 15 ** 2 + (side_card_ranks[0]) * 15 ** 1 + (side_card_ranks[1]), 'Three of a Kind'

		# Return a score of 0 if not Three of a Kind
		return 0, ''


	def is_two_pair(self, hand):
		# Count the occurrences of each rank in the hand
		rank_count = {}
		for card in hand:
			if card.rank not in rank_count:
				rank_count[card.rank] = 1
			else:
				rank_count[card.rank] += 1

		pairs = []
		side_card_rank = None

		for rank, count in rank_count.items():
			if count == 2:
				pairs.append(rank)
			else:
				side_card_rank = rank

		if len(pairs) == 2:
			# Sort the pairs in descending order and calculate a unique score for Two Pair
			pairs.sort(reverse=True)
			return 3 * 15 ** 5 + (pairs[0]) * 15 ** 4 + (pairs[0]) * 15 ** 3 \
				+ (pairs[1]) * 15 ** 2 + (pairs[1]) * 15 ** 1 + (side_card_rank), 'Two Pair'

		# Return a score of 0 if not Two Pair
		return 0, ''


	def is_one_pair(self, hand):
		# Count the occurrences of each rank in the hand
		rank_count = {}
		for card in hand:
			if card.rank not in rank_count:
				rank_count[card.rank] = 1
			else:
				rank_count[card.rank] += 1

		pair_rank = None
		side_card_ranks = []

		for rank, count in rank_count.items():
			if count == 2:
				pair_rank = rank
			else:
				side_card_ranks.append(rank)

		if pair_rank is not None:
			# Sort the side card ranks in descending order and calculate a unique score for One Pair
			side_card_ranks.sort(reverse=True)
			return 2 * 15 ** 5 + (pair_rank) * 15 ** 4 + (pair_rank) * 15 ** 3 \
				+ (side_card_ranks[0]) * 15 ** 2 + (side_card_ranks[1]) * 15 ** 1 + (side_card_ranks[2]), 'One Pair'

		# Return a score of 0 if not One Pair
		return 0, ''


	def is_high_card(self, hand):
		# Calculate and return a unique score for High Card, and its name
		return 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 \
			+ (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'High Card'




def main():
	# read number of players from stdin
	line = sys.stdin.readline()
	line = line.strip()
	num_players = int (line)
	if (num_players < 2) or (num_players > 6):
		return

	# create the Poker object
	game = Poker (num_players)

	# play the game
	game.play()

if __name__ == "__main__":
	main()