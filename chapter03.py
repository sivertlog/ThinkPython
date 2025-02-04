def triangle(l, n):
    for i in range(n):
        print(l*(i+1))
letter = "L"
number = 5
triangle(letter, number)

def print_right(word):
    a=40-len(word)
    for i in range(a):
        print(" ", end="")
    print(word)

def print_border():
    for i in range(40):
        print("*", end="")
    print()

right_word=input("enter a word: ")
print_border()
print_right(right_word)

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