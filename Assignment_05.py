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

print("THANKYOU!!")  
