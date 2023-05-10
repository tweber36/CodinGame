CARDS = dict(
    [(str(x), x) for x in range(2, 10)] + list(zip(["T", "J", "Q", "K", "A"], [10, 10, 10, 10, 1]))
)

thoughts = input().split(".")
bust_threshold = int(input())


def is_valid_observation(observation: str) -> bool:
    return all(x in CARDS.keys() for x in observation)


class Deck:
    def __init__(self):
        self.cards = dict.fromkeys(CARDS.keys(), 4)

    def update_deck(self, observation: str):
        for card in observation:
            self.cards[card] -= 1

    def get_percentage_chance(self, threshold: int):
        remaining_cards = sum(count for count in self.cards.values())
        cards_under_threshold = sum(count for card, count in self.cards.items() if CARDS[card] < threshold)
        return cards_under_threshold / remaining_cards


deck = Deck()
for obs in thoughts:
    if is_valid_observation(obs):
        deck.update_deck(obs)
print(f"{deck.get_percentage_chance(bust_threshold) * 100:.0f}%")
