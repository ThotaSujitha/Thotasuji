def findResistance(a, b, c, d, e):
	color_digit = {'black': '0','brown': '1','red': '2','orange': '3','yellow': '4','green' : '5','blue' : '6','violet' : '7','grey' : '8','white': '9'}
	multiplier = {'black': '1','brown': '10','red': '100','orange': '1k','yellow': '10k','green' : '100k','blue' : '1M','violet' : '1','grey' : '100M','white': '1G'}
	tolerance = {'brown': '+/- 1 %','red' : '+/- 2 %','green': "+/- 0.5 %",'blue': '+/- 0.25 %','violet' : '+/- 0.1 %','gold': '+/- 5 %','silver' : '+/- 10 %','none': '+/-20 %'}
	if (a in color_digit)and (b in color_digit)and (c in color_digit)and (d in multiplier)and (e in tolerance):
		xx = color_digit.get(a)
		yy = color_digit.get(b)
		zz = color_digit.get(c)
		aa = multiplier.get(d)
		bb = tolerance.get(e)
		print("Resistance = "+xx + yy\
			+ zz+" x "+aa+" ohms "+bb)
	else:
  		print("Invalid Colors")

a=str(input("Enter color a : "))
b=str(input("Enter color b : "))
c=str(input("Enter color c : "))
d=str(input("Enter color d : "))
e=str(input("Enter color e : "))
findResistance(a,b,c,d,e)
