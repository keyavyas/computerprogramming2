day1={101,102,103,104}
day2={103,104,105,106}

both_days=day1.intersection(day2)
print("On both days: ", both_days)

only_one_day=day1.symmetric_difference(day2)
print("Only one day:",only_one_day)

total_visitors=day1.union(day2)
print("Total visitors:",total_visitors)
