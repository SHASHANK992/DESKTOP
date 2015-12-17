def hcf(x, y):
   """This function implements the Euclidian algorithm
   to find H.C.F. of two numbers"""
   while(y):
       x, y = y, x % y

   return x

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))
