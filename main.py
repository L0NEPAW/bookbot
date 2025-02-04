def main():

    word_count = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    count_letters(file_contents)

def count_words(words_to_count):

    count = 0

    words = words_to_count.split()

    for word in words:
        count += 1

    return count

def count_characters(characters_to_count):

    characters_count = {}

    lower_characters = characters_to_count.lower()

    for char in lower_characters:

        if char.isdigit():
            key = int(char)
        else:
            key = char

        if key in characters_count:
            characters_count[key] += 1
        else:
            characters_count[key] = 1

    return characters_count

def count_letters(letters_to_count):
    
    letters_count = {}

    for char in letters_to_count:

        if char.isalpha():
            char = char.lower()
            letters_count[char] = letters_count.get(char, 0) + 1

    sorted_letters = sorted(letters_count.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")

main()