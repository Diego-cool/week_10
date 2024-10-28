
#Question 1
age= int(input("How old are you? "))
member= input("Are you a member?Y/N?: ")

if age <18:
    print("Youth ticket price is $10")
 
if age >=18 and age <65 and member=="Y":
    print("Discounted adult ticket price is $12")
if age >=18 and age <65 and member=="N":
    print("Regular adult ticket price is $15")
if age >=65:
    print("Senior discount price is $8")




#Question 18
Length= int(input("What is the length of your password?: "))
Special=(input("Does your password have any special charcters? Yes or No?: "))

if Special == "Yes" or "yes":
    Special=1
else:
 Special=0

if Length > 12 and Special:
    print("Very nice long and strong password")
elif Length >= 12:
    print("Consider adding special characters")


if (8<=Length<=12) and Special :
    print("Moderate password strength")
elif 8<=Length<=12 :
    print("Weak password. Consider adding special characters")
if Length < 8:
    print("Password is too short.")