
#Question 1
#created a variable to determine the age of the user
age= int(input("How old are you? "))
#created a variable to determine whether or no the user is a member
member= input("Are you a member?Y/N?: ")
#if statement to see if you are younger than 18 then your ticket is $10
if age <18:
    print("Youth ticket price is $10")
#if you are over 18 and less than 65 and you have a membership you pay $12
if age >=18 and age <65 and member=="Y":
    print("Discounted adult ticket price is $12")
#if you are over 18 and less than 65 and you dont have a membership you pay $15

if age >=18 and age <65 and member=="N":
    print("Regular adult ticket price is $15")
#if you are over 65 you pay 8 dollars regardless
if age >=65:
    print("Senior discount price is $8")




#Question 18
length= int(input("What is the length of your password?: "))
special=(input("Does your password have any special charcters? Yes or No?: "))

#made a variable for the computer to determine if the user said yes or no 
if special == "Yes" or "yes":
    special=1
else:
 special=0

#if statement to determine if the users password is over the length of 12 characters and has a special character
if length > 12 and special:
    print("Very nice long and strong password")
elif length >= 12: #if it doesnt have a special character then this will print out
    print("Consider adding special characters")


if (8<=length<=12) and special :    # asking if the password is between 8 to 12 characters and if it has a special characters
    print("Moderate password strength")
elif 8<=length<=12 : #if it doesnt have a special character then this will print out
    print("Weak password. Consider adding special characters")

if length < 8: # if the password is less than 8 characters the password is too short
    print("Password is too short.")