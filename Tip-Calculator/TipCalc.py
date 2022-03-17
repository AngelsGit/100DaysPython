print("Welcome to the calculator")
billAmount = input("How much was the bill? ")
tipAmount = input("How much % would you want to give? ")
numPeople = input("How many people to split the bill? ")

tipToDecimal = float(tipAmount) / 100

totalBill = ((float(billAmount) * tipToDecimal) + float(billAmount)) / float(numPeople)

print(totalBill)





