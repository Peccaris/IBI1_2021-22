import pandas as pd
import xlrd  # import 

# open file
xlsx = xlrd.open_workbook('/Users/yiyi/Desktop/IBI1_2021-22/Practical11/BLOSUM.xlsx')
#open sheet1
sheet1 = xlsx.sheets()[0]
name_data=pd.read_excel(r'/Users/yiyi/Desktop/IBI1_2021-22/Practical11/BLOSUM.xlsx',usecols=[0]) #use pandas to read the file as a dataframe 
length_all=len(name_data) # get the length of the colum or row



file_opened_human=open('/Users/yiyi/Desktop/IBI1_2021-22/Practical11/DLX5_human.fa') # open the file
seq_human=file_opened_human.readlines()[1] # chose the second line
file_read_human=list(seq_human) # read the file
file_read_human=file_read_human[0:-1]


file_opened_mouse=open('/Users/yiyi/Desktop/IBI1_2021-22/Practical11/DLX5_mouse.fa') # open the file
seq_mouse=file_opened_mouse.readlines()[1] # chose the second line
file_read_mouse=list(seq_mouse) # read the file
file_read_mouse=file_read_mouse[0:-1]


file_opened_ran=open('/Users/yiyi/Desktop/IBI1_2021-22/Practical11/RandomSeq(1).fa') # open the file
seq_random=file_opened_ran.readlines()[1] # chose the second line
file_read_ran=list(seq_random) # read the file
file_read_ran=file_read_ran[0:-1]



#create empty lists
human_mouse_score=[]
human_random_score=[]
mouse_random_score=[]

total1=0 
for i in range(0,len(file_read_human)): # match the sequence and find the index in the BLOSUM of each single aa
    data1=name_data[name_data['First'].str.contains(file_read_human[i])] # the colum and row are the same in BLOSUM, so we only need to use one
    data2=name_data[name_data['First'].str.contains(file_read_mouse[i])]
    a=eval(str(data1.index[0]))+1
    b=eval(str(data2.index[0]))+1
    score = sheet1.row(a)[b].value  # find the score of each pair of comparasion
    human_mouse_score.append(score)
for ele in range(0, len(human_mouse_score)):  # calculate the total scores
    total1 = total1 + human_mouse_score[ele]   
print("The alignment score of human-mouse is : ", int(total1))

#repeat the same logic to calculate human-random and mouse-random
total2=0
for i in range(0,len(file_read_ran)):
    data1=name_data[name_data['First'].str.contains(file_read_human[i])]
    data2=name_data[name_data['First'].str.contains(file_read_ran[i])]
    a=eval(str(data1.index[0]))+1
    b=eval(str(data2.index[0]))+1
    score = sheet1.row(a)[b].value 
    human_random_score.append(score)
for ele in range(0, len(human_random_score)): 
    total2 = total2 + human_random_score[ele]   
print("The alignment score of human-random is ", int(total2))


total3=0
for i in range(0,len(file_read_ran)):
    data1=name_data[name_data['First'].str.contains(file_read_mouse[i])]
    data2=name_data[name_data['First'].str.contains(file_read_ran[i])]
    a=eval(str(data1.index[0]))+1
    b=eval(str(data2.index[0]))+1
    score = sheet1.row(a)[b].value 
    mouse_random_score.append(score)
for ele in range(0, len(mouse_random_score)): 
    total3 = total3 + mouse_random_score[ele]   
print("The alignment score of mouse-random is: ", int(total3))

#calculate the distance 
edit_distance1=0
for i in range (len(seq_mouse)):
    if seq_human[i]!= seq_mouse[i]:
        edit_distance1 += 1
print('The distance of human-mouse is ',str(edit_distance1))
rate=((len(file_read_human)-edit_distance1)/len(file_read_human))
#calculate the percentage of identical aa
percentage=format(rate,'.2%')
print('The percentage of identical amino acid is ',percentage)

#repeat the same logic
edit_distance2=0
for i in range(len(seq_human)):
    if seq_human[i]!=seq_random[i]:
        edit_distance2 += 1
print('The distance of human-random is ',str(edit_distance2))
edit_distance2 += 0
rate=((len(file_read_human)-edit_distance2)/len(file_read_human))
percentage=format(rate,'.2%')
print('The percentage of identical amino acid is ',percentage)


edit_distance3=0
for i in range(len(seq_mouse)):
    if seq_mouse[i]!= seq_random[i]:
        edit_distance3 += 1
print('The distance of mouse-random is ',str(edit_distance3))
edit_distance3 += 0
rate=((len(file_read_mouse)-edit_distance3)/len(file_read_mouse))
percentage=format(rate,'.2%')
print('The percentage of identical amino acid is ',percentage)



# My interpretation is :
# 1.The high genetic similarity between humans and mice may be due to the fact that these genes perform similar functions, such as respiration, vision, nervous system and so on. 
# 2. Humans and mice may have shared a common ancestor, after which the human ancestor gradually began to separate from the mouse ancestor. Then as the tectonic plate movement caused geographical isolation, the human ancestor and the mouse ancestor became more and more genetically different, until they became separate species.

# By comparing the degree of genetic similarity, we can roughly infer which animals are more likely to share a common ancestor, even though they are now very morphologically different.