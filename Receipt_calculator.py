import math
print("Looking to spilt the cost of a group purchase?\n welcome to receipt calculator !!!")
price_all=eval(input("Step1: Please enter the price of each products : \n (note: eliminate the '$' sign instead separete with'+')"))
tax_p=float(input("Step2: What is the sales tax in your area ?(Note: eliminate the '%'sign)"))
tip_p=float(input("step3 : what percentage would you like to give as a tip / :\n (Note : Eliminate '%' sign)"))
split=float(input("step4: How many peple are spilliting the bill ? :\n (Note : if you are not splitting the bill with anyone with only type '1')"))
total_price=(price_all+(price_all*(tax_p/100.0)) +(price_all*(tip_p/100.0)))/split
final_price=round(total_price,2)
print("The total cost per person is :$",final_price,".")