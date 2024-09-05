# Assignment-05
print("\nLet's start the Assignment!!!")


#Even or Odd
print("\n->Check for Even or Odd\n")

try:
    number_input=int(input("Enter the value: "))
    if number_input %2==0 :
        print(f"Number entered '{number_input}' is even!")
    else:
        print(f"Number entered '{number_input}'is odd!")
except ValueError:
    print("Please enter a valid response!")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

#Positive, Negative, or Zero.
print("\n->Check for Positive, Negative, or Zero.\n")

try:
    number_input=int(input("Enter the value: "))
    if number_input<0 :
        print(f"'{number_input}'is negative!")
    elif(number_input>0):
        print(f"'{number_input}' is positive!")
    else:
        print(f"'{number_input}' is zero!")
except ValueError:
    print("Please enter a valid response!")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


#Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.
print("\n->Checking for conditions regarding '2' and'3'")

try:
    number_input=int(input("\nEnter the value: "))
    if number_input%3==0 :
        print(f"'{number_input}'is divisible by 3!")
    elif(number_input%2==0):
        print(f"'{number_input}' is divisible by 2!")
    elif((number_input%2==0)and(number_input%3==0)):
        print(f"'{number_input}' is divisible by both '2' and '3'!")
    else:
        print(f"'{number_input}' is not divisible by both '2' and '3'!")
except ValueError:
    print("Please enter a valid response!")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

# age, vote eligibility
print("\n->Checking voting eligiblity!")
try:
    age_entered=int(input("\nEnter your age to check:"))
    if age_entered>=18:
        nationality=str(input("\nDo you have 'Pakistani' nationality?:"))
        if nationality in ['yes','y','Yes','YES']:
            print("You are eligible to vote!")
        else:
            print("Please obtain a valid ID to vote!")
    else:
        print("Your'e not eligible!")
except ValueError:
        print("Please enter a valid response!")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


# Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)
print("\n->Checking age scales!")
try:
    age=int(input("\nEnter your age:"))
    if age!=0:
        if age<=12 and age>=0:
            print(f"Your'e entered age'{age}'lies between'child' age scale!")
        elif age>=13 and age<=19:
            print(f"Your'e entered age'{age}'lies between'Teenagar' age scale!")
        elif age>=20 and age<=59:
            print(f"Your'e entered age'{age}'lies between'Adult' age scale!")
    else:
        print(f"Your'e entered age'{age}'lies between'Senior Citizen' age scale!")
except ValueError:
    print("Enter a valid response!")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")  

print("\n->Checking for number of days in months except leap year!")
try:
    month= int(input("\nEnter the month as number between '1' to '12':"))
    if month== (1 and 3 and 5 and 7 and 8 and 10 and 12):
        print(f"The days of the month '{month}'is '31' days!")
    elif month== (4 and 6 and 9 and 11 ):
        print(f"The days of the month '{month}'is '30' days!") 
    else:
        print(f"The days of the month '{month}'is '28' days!") 
except ValueError:
    print("Enter a valid response!")     
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_") 

print("\n->Checking for 'leap year'!\n")
try:
    year=int(input("\nEnter the year: "))
    if( year%4==0 ):
        if (year%100==0):
            if (year%400==0 ):
                print("Entered year is a leap year!")
            else:
                print("Entered year is not a leap year!")
        else:
            print("Entered year is  a leap year!")
    else:
        print("Entered year is not a leap year!")    
except ValueError:
    print(" Enter a valid response!")    
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")     

print("THANKYOU!!")  
