import re  #import regulation expression

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC' #creat a string variable
y = len(re.findall("GAATTC",seq))+1 # find EcoRI cutting sequence and count the number of fragments into which the sequence would be but  
print(' The	 total	number of fragments cut by EcoRI enzyme is: ',y) # print the result
