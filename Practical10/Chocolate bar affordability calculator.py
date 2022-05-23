# define a function that can calculate the number of chocolate bars and the change
def calculator(total_money, price):  
    number_of_bars = total_money // price
    change = total_money % price
    print('The number of chocolate bar you can buy is', number_of_bars,
      'and the change is', "%.2f" % change) #The result is decimal in case the change is not a integer

# an example function call
print('If the total money is 40 and the chocolate bar price is 3')
result=calculator(40,3)
result

# code for the marker to call the function
print('\n','You call the function usin various total amounts and prices')
total_money = input('Input your total money:') # input the total money
total_money=eval(total_money)
price = input('Input the chocolate bar price:')  # input the price
price=eval(price)
result = calculator(total_money, price)  # call the defined function



