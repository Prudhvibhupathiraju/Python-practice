bill_amount=float(input("What is the total bill amount\n"))
tip_percentage = int(input("how much percentage of tip you would like to give ie.. 10 12 20\n"))
num_of_mem=int(input("total persons whom the bill is shared\n"))
share = round((bill_amount + (tip_percentage/100)*bill_amount)/num_of_mem, 2)
print(f"share of each person is {share}")

