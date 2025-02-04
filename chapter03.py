def triangle(l, n):
    for i in range(n):
        print(l*(i+1))
letter = "L"
number = 5
triangle(letter, number)

def print_right(word, num):
    a=num-len(word)
    for i in range(a):
        print(" ", end="")
    print(word)

def print_border(char, num):
    for i in range(num):
        print(char, end="")
    print()

ch="*"
le=40
right_word=input("enter a word: ")
print_border(ch, le)
print_right(right_word, le)

print()

def rectangle(l, h, w):
    for i in range(h):
        for j in range(w):
            print(l, end="")
        print()
rectangle("H", 5, 4)

print()

#extra for fun
def coolrectangle(l, la, h, w):
    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                print(l, end="")
            print()
        else:
            print(l, end="")
            for k in range(w-2):
                print(la, end="")
            print(l)
coolrectangle("=", "H", 4, 8)

print()

#############
##beer song##
#############
def plural_check(num): #corrects bottle vs bottles
    if num == 1:
        p=""
    else:
        p="s"
    return p

def bottle_verse(count): #main verse
    s=plural_check(count)
    print(f"{count} bottle{s} of beer on the wall")
    print(f"{count} bottle{s} of beer")
    if count-1 == 0: #checks for end of song
        print("Take it down, pass it around")
        print("No more bottles of beer on the wall")
    else: #business as usual
        print("Take one down, pass it around")
        s=plural_check(count-1)
        print(f"{count-1} bottle{s} of beer on the wall")

bottles=99
bottle_verse(bottles)

print()
print_border(ch, le)

answer=input("Do you want to hear the whole song? (y/n): ").lower()
ch="#"
le=30
if answer == "y":
    print_border(ch, le)
    print_right("The Beer Song", le)
    print_border(ch, le)
    for i in range(99, 0, -1):
        bottle_verse(i)
        print()
else:
    print_border(ch, le)
    print_right("Lol me neither!", le)
    print_border(ch, le)