# Problem 1 


#this is my input asking for the score
scores=int(input("What was your score:"))


while scores > 0: # while score is greater than 0 run the rest of this code
    if scores > 89: # while score is greater than 89 they are rewarder with Excellent
     print("Excellent")
    if scores > 79 and scores < 90:# while score is between 80 and 90 they are rewarded with Good
            print("Good")
    if scores > 61 and scores < 80:# while score is between 61 and 79 they are rewarded with pass
                print("Pass")
    if scores < 60:   # if score is less than 60 then the user fails
        print("fail")
    scores=int(input("What was your score:"))
else: # if the code is less tan 0 this prints out
     print(" Your score cant be negative")
     
   
#Problem 2

start=int(input("Please enter the starting number:"))#asks the user for the start number
end=int(input("Please enter the ending number:"))# asks the user for the end number
newend=(end + 1)# adds one to the end number because when put in a range the range takes the number before the one you entered

for i in range(start, newend): #print the numbers in between the start and stop 
    print(i)


for i in range(start, newend): # print the numbers in between the start and stop only if the are even and greater than 10
    if (i % 2 == 0) and i > 10:
        print(i)

for i in range(start, newend): #print the numbers in between the start and stop only if the are odd and less than 20
    if (i % 2 ) and i < 20:
        print(i)