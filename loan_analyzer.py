#Create a list of banks to be used for loan analyzer application 

loan_costs = [500, 600, 200, 1000, 450]



# Calculate average loan amount in loan_cost list

for loans in loan_costs:
    outstanding_loans = len(loan_costs)
    total_money_lent = sum(loan_costs)
    average_loan = total_money_lent / outstanding_loans



# format and print string statement for the number of loans in the loan_cost list
# format and print string statement for the total money lent in the loan_cost list
# format and print string statement for the average loan amount in the loan_cost list 

print("\nThere are %d loans in the list.\n"%(outstanding_loans))
print("The combined amount of the loans is $%4.2f\n"%(total_money_lent))
print("The average loan amount is $%4.2f\n"%(average_loan))




# Use loan dictionary to pass future_value and remaining_months to variables
# format and print string statement stating the amounts for future value and remainging months

loan = {"loan_price" : 500,
        "remaining_months" : 9,
        "repayment_interval" : "bullet",
        "future_value" : 1000}

future_value = loan.get("future_value",0)
remaining_months = loan.get("remaining_months",0)
print("The future value of the loan is $%4.2f and the months till loan maturity\
 are %d\n"%(future_value, remaining_months))



# Using loan dictionary determine present value, write a conditional statement recommending to buy the loan or not
 
Present_Value = future_value / (1+ .20/12)**remaining_months
print("The current value of the loan is $%6.2f\n"%(Present_Value))

if Present_Value >= future_value:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")



new_loan = {"loan_price": 800,
            "remaining_months": 12,
            "repayment_months": "bullet",
            "future_value": 1000}

# create a function for future value and return output
def current_value(future_value, annual_discount_rate, remaining_months):
   current_price = future_value / (1+ annual_discount_rate/12)**remaining_months
   return current_price


# Using new_loan dictionary assign values for future_value, remaining_months
# Pass future_value , remaining months , and annual discount rate into the the current_value function and print 
future_value = new_loan.get("future_value",0)
remaining_months = new_loan.get("remaining_months",0)
annual_discount_rate = .2
present_money = current_value(future_value,annual_discount_rate ,remaining_months)
print("\nThe current value of the loan is $%6.2f\n"%(present_money))




loans = [ {"loan_price" : 700,
         "remaining_months" : 9,
         "repayment" : "monthly",
         "future_value" : 1000},
         
         {"loan_price" : 500,
         "remaining_months" : 13,
         "repayment" : "bullet",
         "future_value" : 1000},
         
         {"loan_price" : 200,
         "remaining_months" : 16,
         "repayment" : "bullet",
         "future_value" : 1000},
         
         {"loan_price" : 900,
         "remaining_months" : 16,
         "repayment" : "bullet",
         "future_value" : 1000},
         ]


# using a for loop append loans from the loans list to an empty list that meet certain financial criteria
# and print the append list
inexpensive_loans = []
for cost in loans:
    if cost["loan_price"] <= 500:
        inexpensive_loans.append(cost)

print(inexpensive_loans)




#create a header for a csv file
#import csv into into loan_analyzer
#set csv file path to write

header = ["loan_price", "remaining_months","repayment_interval","future_vaule"]

from pathlib import Path
import csv
output_path = Path("inexpensive_loans.csv")
with open(output_path, "w", newline="") as myfile:
    csvwriter = csv.writer(myfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())
      
        
# using csv path write strings for relative and absolute path   
print(f"This is the relative path: {output_path}")
print(f"This is  the absolute path: {output_path.absolute()}")



