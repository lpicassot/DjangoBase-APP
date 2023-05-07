import pytest
import requests
from app.handlers.helpers import WordFinder

class TestWordFinder:
    def test_longest_word(self):
        # Create a WordFinder object with a word list
        L = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
        word_finder = WordFinder()

        # Test the longest_word method with a valid set of letters
        letters = 'ajsxuytcnhre'
        expected_word = 'saturn'
        assert word_finder.longest_word(L,letters) == expected_word

        # Test the longest_word method with a set of letters that doesn't include any words in the word list
        letters = 'xyz'
        expected_word = ''
        assert word_finder.longest_word(L,letters) == expected_word

        # Test the longest_word method with a set of letters that only includes one letter from a word in the word list
        letters = 'u'
        expected_word = ''
        assert word_finder.longest_word(L,letters) == expected_word

        # Test the longest_word method with a set of letters that includes two letters from a word in the word list
        letters = 'unrsua'
        expected_word = 'uranus'
        assert word_finder.longest_word(L, letters) == expected_word

        # Test example provided on exercise 2
        letters = 'optonoceari'
        expected_word = 'cooperation'
        url = 'https://goo.gl/aoEr9Q'
        file_list = requests.get(url).text
        L = file_list.split('\n')
        assert word_finder.longest_word(L,letters) == expected_word