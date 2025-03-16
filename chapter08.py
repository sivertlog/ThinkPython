import re

'''
#1
From Gemini:

10 digit phone number
r"^\d{3}-\d{3}-\d{4}$"

street address with number and street name with st. or ave:
r"\d+\s+[\w\s]+\s+(ST|AVE)"

names
r"(Mr|Ms|Mrs|Miss|Dr)\.?\s+[A-Z][a-z]+(?:[\s-][A-Z][a-z]+)*"

'''

#2
def head(filename, n, newfile=None):
    with open(filename, 'r') as book:
        for _ in range(n):
            if newfile:
                with open(newfile, 'a') as head_file:
                    head_file.write(book.readline())
            else:
                print(book.readline())


#head('thinkpy.txt', 7, 'headfile.txt')

def head_hartman(in_file, num_lines, out_file=None):
    lines = []
    with open(in_file, 'r') as file:
        for _ in range(num_lines):
            lines.append(file.readline())
    if out_file:
        with open(out_file, 'w') as file:
            file.writelines(''.join(lines))
    else:
        print(''.join(lines))

#3
#wordle

def load_words(word_list: list, n=0):
    with open('words.txt', 'r') as words:
        for word in words:
            if n == 0:
                word_list.append(word.strip().upper())
            elif len(word.strip()) == n: word_list.append(word.strip().upper())

def valid_word(guess, word_list):
    if any(word == guess for word in word_list): return True
    return False

def check_word(guess, word):
    c_letter = '█'
    c_spot = '↑'
    inc = '░'
    result = ''
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result = result + c_spot
        elif guess[i] in word:
            result = result + c_letter
        else:
            result = result + inc
    return result

def wordle():
    word_list = []
    guess_list = []
    load_words(word_list, 5)
    word = 'HELLO'
    while True:
        guess = input("Please enter a 5 letter word: ").upper()

        if valid_word(guess, word_list):
            if not guess in guess_list: guess_list.append(guess)
            print(f"""Result Key:
                  ↑ - correct letter in correct spot
                  █ - correct letter in wrong spot
                  ░ - letter not in word""")
            print("Your guess:")
            print("    ", guess)
            print("    ", check_word(guess, word))
            if guess == word:
                print("You Win!!")
                print(guess_list)
                break
        else:
            print(guess, "is not a valid try")

def main():
    wordle()

if __name__ == '__main__':
    main()

#5
def find_pale():
    #pale pales paled paleness pallor 256
    pattern = r'.*(pale\w*|pallor).*'
    count = 0
    line=''
    with open('TheCountofMnteCristo.txt', 'r', encoding='utf-8') as book:
        for line in book:
            result = re.match(pattern, line.strip().lower())
            if result != None: count += 1

    return count

print(find_pale())


def check_pale(sentence):
   pattern = r'.*(pale\w*|pallor).*'
   return True if re.match(pattern, sentence) else False

def main_2():
    with open('TheCountofMnteCristo.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if check_pale(line.strip()):
                #print(line)
                count += 1

    print(f"Lines with some form of pale: {count}")
main_2()