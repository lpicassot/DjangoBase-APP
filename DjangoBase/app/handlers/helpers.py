import string

class WordFinder:
    def __init__(self):
        self.word_list = list(string.ascii_lowercase)


    def longest_word(self, L, letters):
        is_string_included = lambda letters, word_list: all(letter in word_list for letter in letters)
        if len(letters) > 12 or not is_string_included(letters, self.word_list):
            return "Error: word is longer than 12 characters or contains non ascii lowercase values"

        max_word = ''
        letters_set = set(letters)
        for word in L:
            if all(word.count(c) <= letters.count(c) for c in set(word)) and set(word).issubset(letters_set) and len(word) > len(max_word):
                max_word = word
        return max_word
