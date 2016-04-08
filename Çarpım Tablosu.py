# Python program to find the multiplacion table (from 1 to 10) of a number

# Take input from user
num = int(input("Display multiplacion table of? "))

# use for loop to iterate 10 times
for i in range(1, 11):
    print(num, "x" , i, "=", num * i)
    
