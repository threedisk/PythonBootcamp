# Don't change the code below 
from numpy import diff


age = input("What is your current age?")
# Don't change the code above

# Write your code below this line 

yourAge = int(age)
#diffAge = 90 - yourAge
diffAge = 63 - yourAge
#print (diffAge)

ageToMonth = diffAge * 12
ageToWeek = diffAge * 52
ageToDay = diffAge * 365
# Dibawah cuma tambahan saja
ageToHour = ageToDay * 24
ageToMinute = ageToHour * 60
ageToSecond= ageToMinute * 60

# print(ageToDay)
# print(ageToWeek)
# print(ageToMonth)

print (f"You have {ageToDay} days, {ageToWeek} weeks, and {ageToMonth} months left.")
print (f"Hidup kamu tinggal {ageToSecond} detik atau {ageToMinute} menit atau {ageToHour} jam ")