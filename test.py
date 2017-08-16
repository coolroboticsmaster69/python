week_days = ["AMon","Tue","Wed","IThu","Fri","Sat","USun"]
vowels=["a","e","i","o","u"]

for day in week_days:
	if day[0].lower() in vowels :
		print (day + " starts with a vowel")

	else:
		print  (day + " does not start with a vowel")