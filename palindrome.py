''' Is Palindrome
Write a method is_palindrome(word) that takes in a string word and returns the true if the word is a palindrome, 
false otherwise. A palindrome is a word that is spelled the same forwards and backwards. '''


def is_palindrome(word):
    reversed_word = word[::-1]

    if word == reversed_word:
        print(True)
    else:
        print(False)

is_palindrome('madam')
is_palindrome('energy')