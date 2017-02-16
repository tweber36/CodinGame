from collections import Counter, OrderedDict

# Initialize scores for each letter
SCORES = {}
for l, w in {'eaionrtlsu': 1, 'dg': 2, 'bcmp': 3, 'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10}.items():
    SCORES.update(zip(l, [w]*len(l)))

# Inputs
n = int(input())
lexicon = [input() for _ in range(n)]
letters = input()

# Use Counter to count letters and OrderedDict to be able to sort possible words at the end
letters_count = Counter(letters)
possible = OrderedDict()

for word in lexicon:
    word_count = Counter(word)
    word_count.subtract(letters_count)

    if not +word_count:     # Eliminates negative counts
        possible[word] = sum(SCORES[c] for c in word)

print(max(possible.keys(), key=lambda k: possible[k]))
