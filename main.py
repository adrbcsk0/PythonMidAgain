days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()

workdays.pop(5)
workdays.pop(5)

print(days)
print(workdays)


days2 = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays2 = days2.copy()

workdays2.remove('sat')
workdays2.remove('sun')

print(days2)
print(workdays2)