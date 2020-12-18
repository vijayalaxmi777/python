#WAP to find simple interest : I = PNR/100

def main():

	print("Enter Principal amount")
	P=input()	
	#print(type(P))
	print("Enter Number of months")
	N=input()
	print("Enter rate of interest")
	R=input()	
	#calculations
	I = (int(P)*int(N)*int(R))/100
	print("Simple Interest I ", I)

if(__name__=='__main__'):
	main()