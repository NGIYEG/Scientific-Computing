# This function checks if a number is even. It returns True if the number is even, and False otherwise
def checkEven(number):
    if number % 2==0:
        return True
    else:
        return False
    
    # prompts the user to enter an integer, checks if it is even or odd using the checkEven function, and prints the result.
num1=int(input('Enter an intetger '))
if checkEven(num1):
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")
    
# even_numbers=[i for i in range(1,51) if checkEven(i)]

# for loop that generate a list of even numbers from 1 to 50
even_numbers=[]
for i in range(1,51):
    if checkEven(i):
        even_numbers.append(i)
        
# printing the list
print(even_numbers)

#  a while loop that print numbers from 10 down to 1 .


number1=10
while number1>0:
    print(number1)
    number1-=1