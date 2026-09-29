import random

########################################################
# Program Name: Whats In A Name?                       #
# Author: Skye Gattegno                                #
# Description: this code is made up of various         #
# functions that users can chose to use by selecting   #
# the function's corresponding number                  #
# and the functions are made to play around            #
# with words, or your name, which you                  #
# enter at the start of this program                   #
# Bugs: N/A                                            #
########################################################


def get_first_name(data):
     output = data[0]
     return output

def get_last_name(name):
    names = name.split(" ")
    name_length = len(names)
    last = name_length -1
    return names[last]

def count_vowels(word):
    '''
    Take user's input and find the number of vowels in it

    Parameters: word

    Returns: return the number of vowels in the user's word in integer form
    '''
    vowels = 'aeiouAEIOU'
    count = 0

    for char in word:
        if char in vowels:
            count += 1
    return count

def count_consonants(word):
    '''
    Take user's input and find the number of consonants in it

    Parameters: word (user's input)

    Returns: return the number of consonants in the user's word in integer form
    '''
    consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    count = 0

    for char in word:
        if char in consonants:
            count += 1
    return count

def get_initials(fullname):
    '''
    Take user's inputed name and find initials by taking character 0 of each word

    Parameters: fullname(Users answer to "Enter your full name:")

    Returns: return character 0 of each word and print initials
    '''
    names = fullname.split()
    initials = ""
    for name in names:
        initials += name[0]
    print(f'You intials are {initials}')

def reverse(word):
    '''
    Reverse user's input

    Parameters: word (user's input)

    Returns: return word reversed in order
    '''
    pos = len(word)-1
    while (pos >= 0):
        print (word[pos])
        pos = pos-1

def make_uppercase(word):
     letter = ""
     for char in word:
        if 'a' <= char <= 'z':
            upper_letter = chr(ord(char) - 32)
            letter += upper_letter
        else:
            letter += char
    return letter

def scramble(name):
    '''
    Scramble the letters of the user's inputted name

    Parameters
    '''
    name_list = list(name)
    new_list = []

    while len(name_list) > 0:
        r = random.randrange(0,len(name_list))
        new_list.append(name_list[r])
        del name_list[r]
       



def has_hyphen(word):
    for letter in word:
        if letter == "-":
            return True
    return False

def main():
    name = input ('Enter your full name: ')
    print (f'Hi {name}')
    words = name.split()
    options = '''
    1. Get full name 
    2. Get first name
    3. Get middle name 
    4. Get last name
    5. Find vowel count of entered word
    5a. Find vowel count of name
    6. Find consonant count of entered word
    6a. Find consonant count of name
    7. Get initials
    8. Reverse word
    8a. Reverse name
    9. Make all caps
    10. Make name all caps
    11. Scramble a word
    11a. Scramble your name 
    12. Check for hyphen'''
    print(options)
    while True:
        choice = input ("Select what you would like to do: Enter one of the options listed above, enter 'quit' to leave, or enter 'options' to see all the options again: ")
        if choice == "quit":
            break
        elif choice == "options":
            print(options)
        elif choice == "1":
            print(name)
        elif choice == "2":
            print(words[0])
        elif choice == "3":
            print(words[1])
        elif choice == "4":
            #print(get_last_name(name))
            last = get_last_name(name)
            print("the last name is: " + last)
        elif choice == "5":
            word = input('Enter a word to discover its number of vowels: ')
            print(count_vowels(word))
        elif choice == "5a":
            print(count_vowels(name))
        elif choice == "6":
            word = input('Enter a word to discover how many consonants it has: ')
            print(count_consonants(word))
        elif choice == "6a":
            print(count_consonants(name))
        elif choice == "7":
            get_initials(name)
        elif choice == "8":
            word = input("Enter the word you would like to reverse: ")
            output = reverse(word)
        elif choice == "8a":
            output = reverse(name)
        elif choice == "9":
            word = input("Enter a word to make it all caps: ")
            print(make_uppercase(word))
        elif choice == "10":
            print(make_uppercase(name))
        elif choice == "11":
            word = input("Enter the word you would like to scramble: ")
            print(scramble(word))
        elif choice == "11a":
            print(scramble(name))
        elif choice == "12":
            word = input("Enter a word to check for hyphen: ")
            print(has_hyphen(word))
        else:
            print('Invalid response')
main()
