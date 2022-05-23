import matplotlib.pyplot as plt #import matplotlib.pyplot for plotting
import numpy as np

parernal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

# Create a dictionary using the given numbers
dict={30:1.03, 35:1.07, 40:1.11, 45:1.17, 50:1.23, 55:1.32, 60:1.42, 65:1.55, 70:1.72, 75:1.94}
print(dict)


# A variable of requested paretal age that can be modified
x=30    # This can be modified
print("The risk of chd in the offspring of a father aged",x,"is",chd[parernal_age.index(x)]) 


#plt.scatter(paternal_age,chd) This can be used to change the style of the plot
plt.plot(parernal_age , chd, 'rx') 
plt.title('Parental age vs offspring health')
plt.xlabel('Parernal age') #Edit the xlabel
plt.ylabel('Congenital heart disease in the offspring') # Edit the ylabel
plt.show() # To show the plot
