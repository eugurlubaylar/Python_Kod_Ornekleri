# Python program to display the Fibonacci sequence ut to n-th term using
# recursive functions

def recur_fibo(n):
    """Recursive function to print Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

# take input from the user
nterms = int(input("How many terms? "))

# check if the number of terms i valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
