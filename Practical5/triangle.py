# First, I plan to create 3 variables, a, n, i.
# n is the , a is the sum of elements for each triangle, and i is used for adding calculation.
# Then I plan to use "while" to run the process.
# For each loop, i equals i + 1 , a equals a + i, so a is the sum of the number of elements of the nth triangle. 




n = 10
a = 0
i = 0
while i < n:
    i = i + 1 
    a = a + i
    print("The "+str(i)+"th triangle has "+str(a)+" elements.")

