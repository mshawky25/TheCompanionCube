#imports dependinces
import json

tax = 0.00

with open('taxes.json') as data_file:    
    data = json.load(data_file)


#Future feature, asks the user how many items there was for finding the
#total of multiple items
numberItem = float(input("How many items are there?"))
#Asks the user how much the item was
if numberItem == 1: 
	item = float(input("How much was the item?"))
#Declares the tax variable
tax = 0.00


#Asks the user what state they live in to determine the sales tax
state = input("What is the abbreviation or name of your state?")

def jsoncheck(stateName):
	tax = data["states"][stateName]["tax"]
	pass

jsoncheck(state)
print(tax)

#Asks the user if they want the total or the tax.
totalOrTax = input("Do you want to see the tax or the total?: ")

realTax = tax / 100
totalTax = realTax * item
total = item + totalTax

meal = str(item)
tax = str(tax)

#Prints either the total or the tax of the item which the user asked earlier.
if totalOrTax == "total":
	print("%.2f" % total)

if totalOrTax == "tax":
	print("%.2f" % totalTax)

input("Press any button to close.")


