print("Welcome to the tip calculator!")

bill=float(input("What was the total bill? $"))

num_percent=int(input("What percentage tip would tou like to give? 10, 12, or 15? "))

no_people=int(input("How many people to split the bill? "))

#calculation of total tip
tip_percent=num_percent/100
tip_amount=tip_percent*bill
total_bill=bill+tip_amount

#splliting in each people
final_amt=total_bill/no_people
#rounding to 2 places of decimal
bill_per_person=round(final_amt,2)
bill_per_person="{:.2f}".format(bill_per_person)


#output
print(f"Each person should pay: $ {bill_per_person}")


#ouput screen
'''Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would tou like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $ 33.60'''
