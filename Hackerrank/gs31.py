def stringFormattedWeeklyPrices(dailyPrice):
	num_of_days = len(dailyPrice)
	lower_limit = 0
	# upper_limit = 6
	sum = 0
	average_price = []
	for i in range(0,6):
		sum = sum + dailyPrice[i]
	average_price.append(str("%.2f" % round(sum/7, 2)))
	for i in range(7, num_of_days):
		sum = sum - dailyPrice[lower_limit] + dailyPrice[i]
		average_price.append(str("%.2f" % round(sum/7, 2)))
		lower_limit += 1
	return average_price
dailyPrice=[7,1,2,3,4,5,6,7]
print(stringFormattedWeeklyPrices(dailyPrice))