# # Vraag 1

def fizzy(n):
    lijst = []

    for i in range(1, n):
        if i % 3 == 0 and (i % 5 == 0 or i % 7 == 0):
            lijst.append(i)

    return lijst


fizzy_list = fizzy(100)
print(fizzy_list)

fizzy_list = fizzy(50)
print(fizzy_list)

# # Conditie: i deelbaar door 3 en 5 of 3 en 7 (of beide).
# # Verwacht: [15, 21, 30, 42, 45, 60, 63, 75, 84, 90]


# Vraag 2

# Conditie: n == 2 * a + b; a en b delers van n
# Alternatief: n - 2 * a = b; a en b delers van n

def print_decomposition(n):
    for a in range(1, n//2):
        if n % a == 0:
            b = n - 2 * a
            if n % b == 0:
                print(f'{n} = 2 * {a} + {b}')


print_decomposition(12)

# # Verwacht:
# # 12 = 2 * 3 + 6
# # 12 = 2 * 4 + 4


# Vraag 3

def filter_words_starting_with(text, letter):
    output_list = []
    word_list = text.split()

    for word in word_list:
        clean_word = word.strip(',.')
        lower_word = word.lower()
        if lower_word[0] == letter:
            output_list.append(clean_word)

    return output_list

example_text = "David Donald Doo dreamed a dozen doughnuts and a duck-dog, too."
print(filter_words_starting_with(example_text, "d"))

example_text = "Blabla hehe"
print(filter_words_starting_with(example_text, "h"))

# Verwacht: ['David', 'Donald', 'Doo', 'dreamed', 'dozen', 'doughnuts', 'duck-dog']


# Vraag 4

def longest_streak(filename):
    file = open(filename)
    winning_streak = 0

    longest_streak = 0

    for line in file:
        splitted = line.split(',')
        result = splitted[2]
        if result == 'won':
            winning_streak += 1
        else:
            winning_streak = 0

        if winning_streak > longest_streak:
            longest_streak = winning_streak

    file.close()

    return longest_streak

streak = longest_streak('barca.txt')
print(streak)

# Verwacht 13