def easy():
    print("#Easy")
    word=input("Enter a word: ")
    print("The first char:",word[0])
    print("The last char:",word[-1])

def medium():
    print("Medium")
    word=input("Enter a word: ")
    print("The reversed word is:",word[::-1])

def hard():
    print("#Hard")
    word=input("Enter a word:")
    if word==word[::-1]:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")
