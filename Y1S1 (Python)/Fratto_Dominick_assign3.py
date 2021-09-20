# variables
payrate = input("Please input your hourly pay: ")
hours = input("Please input your hours worked: ")
overtime = input("Please input how many hours you worked overtime: ")

# tells python these are floats
payrate = float(payrate)
hours = float(hours)
overtime = float(overtime)

# wage calculation, used in lines 25 and 29
wage = payrate * hours

# error handler for hours being under 40, and having anything above 0 in the overtime input
if (hours < 40) and (overtime >= 1):
    print("error. you put in", int(hours), "for hours, and", int(overtime), "for overtime, that's impossible")

# error handler for the hours input being over 40
elif hours > 40:
    print("you cant work more then 40 hours without overtime")

# output for overtime pay, plus formatting
elif overtime >= 1:
    overpay = payrate * 1.5 * overtime
    print("Your pay for the week is, plus overtime: ${0:.2f}".format(overpay + wage))

# output for basic wages, and formatting
elif overtime >= 0:
    print("Your pay for the week is: ${0:.2f}".format(wage))
