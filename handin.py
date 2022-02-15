
#Password Checker and Generator ACTUAL PROGRAM
#Checks the strength of user-given password/s, and then suggests random, very strong password


import csv
from bigfunction import strength, password_generation, add_chars 


#Password Checker and Generator
print("Welcome to the Password Program. \nI can help you check the strength of your passwords and help you generate better, stronger passwords. ")

userpassword = str(input("\nLets start with checking your old password. \nLonger passwords that use more different character types are stronger. \nFor example '7i-Uo3' is stronger than 'apple12'. \nEnter your old password: "))
strength(userpassword)
newcheck = str(input("\nDo you want to check another password? Type in 'yes' or just push any key or Enter if you do not want to check another password: "))
while newcheck == "yes": #runs until the user has no more passwords to check
    strength(userpassword)
    newcheck = str(input("\nDo you want to check another password? Type in 'yes' or just push any key or Enter if you do not want to check another password: "))


#New password generator
newquestion = str(input("\nDo you want a new, stonger password? Type in 'yes' or just push any key or Enter if you do not want a new password: "))
while newquestion == "yes": #runs until the user is happy with the new password
    userlength = int(input("\nHow long should your new password be? Enter number of characters for your new, stronger password: "))
    password_generation(userlength)
    newquestion = str(input("\nIf you are not happy with your new password, generate a new one. Do you want a new password? Type in 'yes' for a new password, otherwise just push any key or Enter: "))
else:
    print("\nThanks for using this program.")
