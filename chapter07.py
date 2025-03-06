#1
#Examples from book:

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def uses_any_incorrect(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT!
'''The program is incorrect because it returns after checking only the first letter.'''

#2
def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('building', 'score')
    True
    >>> uses_none('sivert', 'five')
    False
    """
    return not any(letter in word for letter in forbidden)

#3
def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('canada', 'cand')
    True
    >>> uses_only('can', 'usa')
    False
    """
    return all(letter in available for letter in word)

#4
def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('thequickbrownfoxjumpsoverthelazydog', 'abcdefghijklmnopqrstuvwxyz')
    True
    >>> uses_all('bucket', 'buckets')
    False
    >>> uses_all('bucket', 'buck')
    True
    """
    return all(letter in word for letter in required)

#05
def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    word = word.lower()
    available = available.lower()
    required = required.lower()
    return uses_only(word, available) and not uses_none(word, required) and len(word) >= 4


def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    score = 0
    if len(word) == 4: return 1
    if len(word) > 4: score = len(word)
    if uses_all(word.lower(), available.lower()): score += 7
    return score

#6
def uses_all_2(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all_2('banana', 'ban')
    True
    >>> uses_all_2('apple', 'api')
    False
    >>> uses_all('thequickbrownfoxjumpsoverthelazydog', 'abcdefghijklmnopqrstuvwxyz')
    True
    >>> uses_all('bucket', 'buckets')
    False
    >>> uses_all('bucket', 'buck')
    True
    """
    return uses_only(required, word)

#7
'''lol no ai required'''

#8
# I asked gemini the question word for word as described in the book.
# Gemini failed to call uses_any() in uses_all().
# I repeated the question word for word and it gave me the last function
# on this page, defined as uses_all_gemini_v2()

def uses_any_gemini(word, available):
    """Checks if any letters in available are in word."""
    for letter in available:
        if letter in word:
            return True
    return False

def uses_all_gemini(word, required):
    """Checks if all letters in required are in word, allowing repeats."""
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all_gemini_v2(word, required):
    """Checks if all letters in required are in word, allowing repeats, using uses_any."""
    for letter in required:
        if not uses_any(word, letter):
            return False
    return True

# Example Usage
'''
print(uses_any_gemini("hello", "aeiou"))  # Output: True
print(uses_any_gemini("world", "xyz"))    # Output: False

print(uses_all_gemini("hello", "he"))     # Output: True
print(uses_all_gemini("balloon", "lol")) # Output: True
print(uses_all_gemini("hello", "hexyz"))  # Output: False
print(uses_all_gemini("aabbcc", "abc")) #Output: True
print(uses_all_gemini("aabbcc", "abcd")) #Output: False
'''