# Bill and tips generator program:
# e.g.
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

#Now, in this case, because the bill is likely to have numbers after the decimal place, it's probably better that we turn it into a float so that we get the most accurate result possible.
bill = float(input("What is the amount of total bill? $"))
tip_percentage = int(input("How much would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip_percentage/100 * bill + bill

#Or we ca do the same: bill_with_tip = bill * (1 + tip/100)
#tip = (tip_percentage/100)

bill_per_person = bill_with_tip/people

final_amount_per_person = round(bill_per_person, 2)
#After a comma, we can specify how precise, how many numbers or how many decimal places do we want to round this bill to. 

print(f"Each person should pay ${final_amount_per_person}")
#So instead of using round, we can create this final amount variable by creating a string using that format and then we can use the format function to pass in that bill_per_person. 