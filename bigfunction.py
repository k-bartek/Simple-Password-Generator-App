
#Password Checker and Generator - Katarina Bartekova
#Checks the strength of user-given password/s, and then suggests random, very strong password
#FUNCTION DOCUMENTATION 

import csv
import random


def add_chars():
    #function used in both checking and generating password - optional - offers user to add more chracters to the list of given characters, useful for letters from different languages
    filechars = open("chars.txt", "r")
    reader = csv.reader(filechars)
    mylist = []
    for row in reader:
        mylist.append(row)
    filechars.close()
    #special = mylist[0] #letters = mylist[1] #numbers = mylist[2] #capitals = mylist[3]
    see = str(input("\nDo you want to see characters used in checking your password? \nWe encourage this option if your password includes non-standard-English letters such as ä,ľ,ž,Ø,ö,ü. Otherwise, the program will not be able to check the strength of your password correctly. \nType in 'yes' otherwise, push Enter or push any key on your keyboard to skip this step."))
    if see == "yes":
        print("\nThese are the letters used in checking your password: " , mylist[1],"\nThese are the special characters: ", mylist[0], "\nThese are the numbers: ", mylist[2], "\nThese are the capital letters: ", mylist[3])
        appendchoice = str(input("Do you want to append characters used in checking your password? Type in 'yes' \nOtherwise, if your password contains only characters in the lists given above, push Enter or push any key on your keyboard"))
        if appendchoice == "yes":
            listchoice = str(input("Which list do you want them to be appended to? Write letters, numbers, capital letters, or special characters"))
            newchars = str(input("\nWhat are the new characters you wish to append? Type them in without a spacebar or a comma. "))
            def charappend(a,b): #function for appending any chosen list
                listchoice = a
                newchars = b
                if listchoice == "letters": listchoice1 = mylist[1]
                elif listchoice == "numbers": listchoice1 = mylist[2]
                elif listchoice == "capital" or listchoice == "capital letters": listchoice1 = mylist[3]
                else: listchoice1 = mylist[0]
                for i in newchars:
                    listchoice1.append(i)
                print("\nThis is the new list ", listchoice, " used for checking your password: ", listchoice1)
                return listchoice1
                return mylist
            charappend(listchoice, newchars)
    return mylist


def strength(a):
        word = a
        mylist = add_chars() #option to add characters to their list for password check of non english letters

        print("\nWe evaluated the given password ", word)
        #checking strength
        def digit_check(a):
            word = a
            count_digit = 0
            for i in word: #check each character if it is a digit or a char -def for nested function
                if i.isdigit() == True:
                    count_digit += 1
            if count_digit == 0: print("There are no digits.")
            elif count_digit == 1: print("There is 1 digit.")
            else: print("There are ", count_digit, "digits.")
            return count_digit
        def check_special_char(a):
            word = a
            special_char_list = mylist[0]
            count_special = 0
            for i in word:
                if (i in special_char_list):
                    count_special += 1
                #nice grammar
            if count_special == 0: print("There are no special characters")
            elif count_special == 1: print("There is 1 special character")
            else: print("There are ", count_special, "special characters.")
            return count_special
        def check_letter(a):
            count_letter = 0
            for i in word:
                if (i in mylist[1]):
                    count_letter += 1
            if count_letter == 0: print("There are no lowercase letters.")
            elif count_letter == 1: print("There is 1 lowercase letter.")
            else: print("There are ", count_letter, "lowercase letters.")
            return count_letter
        def check_capital(a):
            count_capital = 0
            for i in word:
                if (i in mylist[3]):
                    count_capital += 1
            if count_capital == 0: print("There are no capital letters.")
            elif count_capital == 1: print("There is 1 capital letter.")
            else: print("There are ", count_capital, "capital letters.")
            return count_capital
        def alternation(a): #alternation is important to avoid fully written words (such as apple) or  things such as 1234
            word = a
            alternationcount = 0
            for i in range(len(word)-1):
                for j in range(len(mylist)-1):
                    if ((word[i] in mylist[j]) and ((word[i+1] not in mylist[j]))): #checking if the next character is a different element type
                        alternationcount += 1
            print("There are ", alternationcount, "alternations between different character types in your password.")
            return alternationcount


        #getting counts of each important characteristic for evaluation
        count_digit = digit_check(a)
        count_special = check_special_char(a)
        count_letter = check_letter(a)
        count_alternation = alternation(a)
        count_capital = check_capital(a)

        def evaluation(a,b,c,d,e,f):
            word = a
            numdigits = b
            numspecial = c
            numletters = d
            numalternation = e
            numcapital = f
            #length and numalternation are the most important aspects. Sufficient amount of different element types can compensate for missing numalternation,but not length
            #scale: very weak, weak, moderate, moderately strong, strong, very strong
            print("\n")
            if len(a) < 5:
                print("Your password is very weak, it is too short.")
            elif 5<len(a)<10: # this password can be max strong
                if numalternation > 4:
                    print("Your password is strong.")
                elif numalternation > 3:
                    print("Your password is moderately strong.")
                elif (numdigits > 2) and (numspecial > 1) and (numletters > 2) and (numcapital>1):
                    print("Your password is strong.")
                elif (numdigits > 1) and (numspecial > 1) and (numletters > 2) and (numcapital>1):
                    print("Your password is moderately strong.")
                elif ((numdigits > 1) or (numspecial > 1)) and ((numletters > 2) or (numcapital>1)):
                    print("Your password is moderate.")
                else:
                    print("Your password is weak.")
            elif len(a)>= 10: #long passwords can be very strong
                if numalternation > 5:
                    print("Your password is very strong.")
                elif numalternation > 4:
                    print("Your password is strong.")
                elif numalternation > 3:
                    print("Your password is moderately strong.")
                elif (numdigits > 2) and (numspecial > 2) and (numletters > 2) and (numcapital>2):
                    print("Your password is very strong.")
                elif (numdigits > 2) and (numspecial > 1) and (numletters > 2) and (numcapital>1):
                    print("Your password is strong.")
                elif (numdigits > 1) and (numspecial > 1) and (numletters > 2) and (numcapital>1):
                    print("Your password is moderately strong.")
                elif ((numdigits > 1) or (numspecial > 1)) and ((numletters > 2) or (numcapital>1)):
                    print("Your password is moderate.")
                else:
                    print("Your password is weak.")


        return evaluation(a, count_digit, count_special, count_letter, count_alternation,count_capital)
        print("Remember, the more different character types you have, the better")




def password_generation(a):
    mylist = add_chars() #reads the txt doc, creates list in the function 1 allows user to append chars
    desired_length = a

    def generate_random(b):
        chosen_list = b
        rand = random.randint(0,(len(chosen_list))-1)
        ch1 = (chosen_list[rand])
        return ch1

    newpassword = ""
    for i in range(desired_length):
        randchars =[]
        for i in mylist:
            randchars.append(generate_random(i)) #generates a random element for numbers, special chars, letters,capital letters /one each
        ch = generate_random(randchars) #randomly chooses an element from the list of random elements for each iteration (for each character in length of the desired password) = double randomness
        newpassword += str(ch)
    print("\nThis is your new password: ", newpassword)
