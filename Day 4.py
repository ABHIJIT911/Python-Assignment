#Define a function which will take a number as argument and return its factorial.Call the function to print factorial of any number(integer).
def factorial(n):
  if not ((n >= 0) and (n % 1 == 0)):
    return("Number can't be negative or floating point!")
  return 1 if n == 0 else n * factorial(n - 1)

n=int(input("Input a number to compute the factiorial : "))
print("Factorial of ", (n) ,":" , factorial(n))
