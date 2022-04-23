# Taking input from user

number = int(input("Enter any number: "))

# prime number is always greater than 1, so it checked here
# Iterating from 2 to the number entered by the user

if number > 1:
    for i in range(2, number):

         # If number is divisible by any number between 2 and n / 2, it is not prime

        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number.
else:
    print(number, "is not a prime number")