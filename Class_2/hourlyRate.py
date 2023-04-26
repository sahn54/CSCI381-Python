hours = int(input("Please enter the number of hours that you worked: "))
hourlyRate = float(input("Please enter your hourly rate: "))


#

# Straight Pay = amount owed to worker for worker less than equal to 40 hours
# Overtime pay = amount owed to worker for worker for work done after 40 hours
# Total Pay = straight Pay + Overtime Pay

overTimeHours = max(0, hours - 40)
straightHours = hours - overTimeHours

overTimePay = overTimeHours * 1.5 * hourlyRate
straightPay = hours * hourlyRate
totalamount = overTimePay + straightPay

print("$" + str(totalamount))
