#desrib which year has the greastest number of new COVID-19
a = 19245301
b = 4218520
c = 271
d = b-c
e = a-b
if d>e:
    print("the rate of new case in 2020 is greater than in 2021")
elif d<e:
    print("the rate of new case in 2021 is greater than in 2020")
else:
    print("the rate of new case in 2020 is the same sa in 2021")

#example：W=X+Y
if 3<5: # You can change the numbers
  X = True
else:
  X = False

if 9<15: # You can change the numbers
  Y = True
else:
  Y = False

W = X and Y
print('W is', W)
# W should be true only if both X and Y are True

