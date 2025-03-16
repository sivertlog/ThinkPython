from chapter08 import load_words

#2
def is_anagram(word_1, word_2):
    return sorted(list(word_1.upper())) == sorted(list(word_2.upper()))

wl=[]
al=[]
load_words(wl)
for word in wl:
    if is_anagram('takes', word):
        al.append(word)
#print(al)

#3
def is_palindrome(word:str):
    return word.upper() == ''.join(reversed(word.upper()))
def is_palindrome_2(word:str):
    return word.upper() == word.upper()[::-1]

#for word in wl:
#    if is_palindrome_2(word): print(word)

#4
def reverse_sentence(string:str):
    return ' '.join(reversed(string.split(' '))).capitalize()

a_string = 'Upper case the first letter in this seNtence'
#print(reverse_sentence(a_string))

#5
def total_length(string_list: list):
    count=0
    for word in string_list: count += len(word)
    return count

#print(total_length(wl))
