def small_function():
	print("Hello")
	return 5;
	print("World")

def big_function():
	a = 1
	while(a > 0):
		a+=1
		print(a)
		if (a == 100):
			return 0
		elif (a > 100):
			print("Over 100!")
		else:
			return 5

def wtf_function():
	GamePrices = ("Breath of the Wild":"$60")
	for name in GamePrices:
		print (GamePrices[name])
		if (gamePrices[name] == "Breath of the Wild"):
			print ("costs $60")
	
