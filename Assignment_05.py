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


print("THANKYOU!!")  
