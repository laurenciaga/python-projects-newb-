print("Welcome to the tip calculator.")

bill = input("What was the total bill? ")
bill_amount = float(bill)
percent = input("What percentage would you like to give? 10, 12, or 15? ")
percent_float = float(percent)
percent_total = (percent_float / 100)
total = (bill_amount) * (percent_total) + (bill_amount)
#total_round = round(total)
people = input("how many people to split the bill? ")
people_int = float(people)
split_total = (total) / (people_int)
print(f"Each person should pay: {split_total:.2f} ")