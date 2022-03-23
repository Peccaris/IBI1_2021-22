import matplotlib.pyplot as plt  # Import matplotlib.pyplot and numpy for plotting
import numpy as np

marks=[45,36,86,57,53,92,65,45]  # Creat a list called "marks"
print(sorted(marks))

plt.boxplot(marks,labels=["Rob"])  # Set alabel for boxplot
plt.ylabel('marks',fontsize=20) # Set y label
plt.title("IBI marks")  # Set a title for the boxplot
plt.show()

average = sum(marks)/len(marks) # Calculate the average value of the data
print(average)
if average >= 60:   # Test if Rob can pass
    print("Pass")
else:
    print("Rob failed")