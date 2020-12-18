#WAP to swap contents of 2 numbers using temporary variable

def main():

	print("Enter 1st number")
	num1=input()
	num1=int(num1)
	print("Enter 2nd number")
	num2=input()
	num2=int(num2)
	print("-------------- Before swapping -----------------")
	print("num1 = ",num1)
	print("num2 = ",num2)
	# logic of swapping
	temp=num1
	num1=num2
	num2=temp
	print("--------------- After swapping -----------------")	
	print("num1 = ",num1)
	print("num2 = ",num2)

if(__name__=="__main__"):
	main()