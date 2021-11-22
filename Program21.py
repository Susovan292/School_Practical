# Write a program to display unique vlowels present in the given word using stack.

VOWELS = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the word to search for vowels : ")
stack = []
for letter in word:
    if letter in VOWELS:
        if letter not in stack:
            stack.append(letter)

print(stack)
print("The number of different vowels present in {} is {}".format(word, len(stack)))