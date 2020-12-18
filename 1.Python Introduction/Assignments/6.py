#WAP to convert temperature from Fahrenheit to Celsius (C=5.0/9.0*F-32)
# WAP to covert F to T
def main():

	print("Enter temperature in Fahrenheit")
	F=input()
	F=float(F)
	#logic
	C=(5.0/9.0)*(F-32)
	print("===================================")
	print("In Fahrenheit=",F," \nIn Celsius=",C)
	
if(__name__=="__main__"):
	main()