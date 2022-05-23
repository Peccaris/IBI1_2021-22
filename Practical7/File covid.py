# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

covid_data = pd.read_csv("/Users/yiyi/Desktop/IBI1_2021-22/Practical7/full_data.csv")  # Read the dataframe


# A list of Booleans that is the same length as the number of columns in the dataframe can choose to show the first and third columns
my_columns_1 = [True, False, True, False, False, False]
t1 = covid_data.iloc[10:21, my_columns_1]  # Columns from rows 10-20
print(' The first and third columns from rows 10-20 (inclusive):','\n', t1)

# The 'total_cases' for all rows corresponding to Afghanistan
df = pd.DataFrame()
for i in range(len(covid_data)):
    if covid_data.loc[i, "location"] == "Afghanistan":
        df_i=covid_data.iloc[i:i+1]
        df=pd.concat([df,df_i])
my_columns_2 = [False, False, False, False, True, False] # use Boolean to select colums
total_cases=df.iloc[:, my_columns_2]
print('\n',"The 'total_cases' for all rows corresponding to Afghanistan:")
print(total_cases)

# compute the mean number of new cases and new deaths in China
china_new_data  = covid_data[covid_data.location == 'China'][[
    'date', 'new_cases', "new_deaths"]] # make an object called china_new_data to store only the data on new cases and deaths for China
t4 = china_new_data['new_cases']
t5 = china_new_data['new_deaths']
M1 = round(np.mean(t4), 2)
M2 = round(np.mean(t5), 2)
print('\n','The mean number of new cases in China is', M1,'\n','The mean number of new cases in China is', M2)

 # create a boxplot of new cases in China worldwide
plt.figure(figsize=(3, 6))
plt.boxplot(t4,labels='A')
plt.yticks(np.arange(0, 16000, 1000))
plt.title('New_cases')
plt.xlabel('China')
plt.ylabel('number of daily new cases')
plt.show()

 #created a boxplot of new deaths in China worldwide
plt.figure(figsize=(4, 4))
plt.boxplot(t5,labels='B')
plt.yticks(np.arange(0, 300, 100))
plt.title('Death_cases')
plt.xlabel('China')
plt.ylabel('number of daily death_cases')
plt.show()

# plot both new cases in China over time.
t6 = china_new_data['date']
china_dates = t6
plt.plot(china_dates, t4, 'r+')
plt.title('New_cases')
plt.xlabel('Date')
plt.ylabel('Daily new_cases')
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.show()

# plot both new deaths in China over time.
plt.plot(t6, t4, label='New_cases')
plt.plot(t6, t5, label='Death_cases')
plt.legend()
plt.xlabel('Date')
plt.title('Daily New_cases and Death_cases in China')
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.show()


# The code to answer the chosen question
SK = covid_data[covid_data.location == 'South Korea']['total_cases']
SK_date = covid_data[covid_data.location == 'South Korea']['date']
plt.plot(SK_date, SK, label='South Korea')

K = covid_data[covid_data.location == 'Kenya']['total_cases']
K_date = covid_data[covid_data.location == 'Kenya']['date']
plt.plot(K_date, K, label='Kenya')

C = covid_data[covid_data.location == 'Colombia']['total_cases']
C_date = covid_data[covid_data.location == 'Colombia']['date']
plt.plot(C_date, C, label='Colombia')
# label the plots
plt.legend()
plt.xlabel('Date')
plt.ylabel('Number')
plt.title('Total cases')
plt.xticks(SK_date.iloc[0:len(SK_date):4], rotation=-90)
plt.show()
