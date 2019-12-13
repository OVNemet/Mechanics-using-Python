def convertF(TC):
	# Converts from Centigrade to Fahrenheit
	ratio = 9.0 / 5.0
	constant = 32.0
	TF = ratio * TC + constant
	return TF

print(convertF(45.0))
