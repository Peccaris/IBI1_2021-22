# First, I need to create variables,n (times) and p (total number of pieces) for incremental calculations.

n = 0
p = 1
while p <= 64:    # Then I need a "while statement" to creat a loop.
    n = n+1    
    p = int((n*n+n+2)/2)   # Next, I should apply the formula into the loop to count the p for each n
    if n == 1:
        print ("With 1 time of straight cut, the total number of pizza slice is ",p)
    else:
        print("With",n,"times of straight cuts, the total number of pizza slice is ",p)

# Last, to make the output description clear, I should combine strings and number variables to give a complete sentence.

# Additionally, use "if statement " to make the grammar proper.