import random

class Card:
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('C', 'D', 'H', 'S')

    def __init__(self, rank=12, suit='S'):
        if rank in Card.RANKS:
            self.rank = rank
        else:
            self.rank = 12
        
        if suit in Card.SUITS:
            self.suit = suit
        else:
            self.suit = 'S'

    def __str__(self):
        rank_str = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(self.rank, str(self.rank))
        return rank_str + self.suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)

class Poker:
    HAND_RANKS = [
        "High Card",
        "One Pair",
        "Two Pairs",
        "Three of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a Kind",
        "Straight Flush",
    ]

    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [[] for _ in range(num_players)]
        num_cards_in_hand = 5

        for _ in range(num_cards_in_hand):
            for i in range(num_players):
                self.players[i].append(self.deck.deal())

    def play(self):
        player_hands = []

        for i, player_hand in enumerate(self.players):
            sorted_hand = sorted(player_hand, reverse=True)
            self.players[i] = sorted_hand
            hand = " ".join(map(str, sorted_hand))
            player_hands.append((i + 1, sorted_hand, hand))

        for player_num, _, hand in player_hands:
            print(f'Player {player_num}: {hand}')


        best_rank = self.get_hand_rank(player_hands[0][2])
        winners = [player_hands[0]]

        for i in range(1, len(player_hands)):
            hand_rank = self.get_hand_rank(player_hands[i][2])

            if Poker.HAND_RANKS.index(hand_rank) < Poker.HAND_RANKS.index(best_rank):
                best_rank = hand_rank
                winners = [player_hands[i]]
            elif Poker.HAND_RANKS.index(hand_rank) == Poker.HAND_RANKS.index(best_rank):
                winners.append(player_hands[i])

        for winner in winners:
            print(f'Player {winner[0]}: {best_rank}')

    def get_hand_rank(self, hand):
        rank_counts = [0] * 15
        suit_counts = {'C': 0, 'D': 0, 'H': 0, 'S': 0}

        cards = hand.split()
        card_objects = [Card(self.get_rank_value(card[:-1]), card[-1]) for card in cards]

        for card in card_objects:
            rank_counts[card.rank] += 1
            suit_counts[card.suit] += 1

        if 4 in rank_counts:
            return "Four of a Kind"
        if 3 in rank_counts and 2 in rank_counts:
            return "Full House"
        if 3 in rank_counts:
            return "Three of a Kind"

        is_flush = any(count >= 5 for count in suit_counts.values())
        is_straight = self.is_consecutive(rank_counts)

        if is_flush and is_straight:
            return "Straight Flush"
        if is_flush:
            return "Flush"
        if is_straight:
            return "Straight"

        if rank_counts.count(2) == 2:
            return "Two Pairs"
        if 2 in rank_counts:
            return "One Pair"

        return "High Card"

    def get_rank_value(self, rank_str):
        rank_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return rank_dict.get(rank_str, -1)

    def is_consecutive(self, rank_counts):
        consecutive = 0
        for i in range(2, 15):
            if rank_counts[i] >= 1:
                consecutive += 1
                if consecutive == 5:
                    return True
            else:
                consecutive = 0
        return False

def main():
    num_players = int(input('Enter number of players: '))
    while num_players < 2 or num_players > 6:
        num_players = int(input('Enter number of players (2-6): '))


    game = Poker(num_players)
    game.play()

if __name__ == "__main__":
    main()
