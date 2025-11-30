from itertools import permutations

def word_to_number(word, mapping):
    number = 0
    factor = 1
    for letter in reversed(word):
        number += mapping[letter]*factor
        factor *= 10
    return number

def crypt(equation):
    equation = equation.replace(' ', '').upper()
    left_side, righ_side = equation.split('=')
    left_words = left_side.split('+')

    uniqueletters = set(righ_side)
    for word in left_words:
        for letter in word:
            uniqueletters.add(letter)
    uniqueletters = list(uniqueletters)

    digits = range(10)
    for perm in permutations(digits, len(uniqueletters)):
        mapping = dict(zip(uniqueletters, perm))

        if any(mapping[word[0]]==0 for word in left_words + [righ_side]):
            continue

        left_sum = sum(word_to_number(word, mapping) for word in left_words)
        right_value = word_to_number(righ_side, mapping)

        if left_sum == right_value:
            left_nums = [word_to_number(word, mapping) for word in left_words]
            print(f"{left_nums[0]} + {left_nums[1]} = {right_value}; Mapping: {mapping}")
            return True

if __name__ == "__main__":
    crypt(input("Enter the expression: "))