Year = int(input("Enter a year: "))

if (Year < 1582):
	print("Not within the Gregorian calendar period")
elif (Year % 4 != 0 and Year % 400 !=0 ):
		print("Common year")
elif (Year % 100 != 0):
		print("Leap year")
else:
		print("Leap year")