#WAP to find total and percentage of marks of 5 subjects of given student

def main():


	print("Enter the marks of subject 1")
	sub1=input()
	#type casting
	sub1=int(sub1)
	print("Enter the marks of subject 2")
	sub2=input()
	sub2=int(sub2)
	print("Enter the marks of subject 3")
	sub3=input()
	sub3=int(sub3)
	print("Enter the marks of subject 4")
	sub4=input()
	sub4=int(sub4)
	print("Enter the marks of subject 5")
	sub5=input()
	sub5=int(sub5)
	total = sub1 + sub2 + sub3 + sub4 + sub5 
	print("Total=",total)
	percentage = (total/500)*100
	print("Percentage= ",percentage)
	
if(__name__=='__main__'):
	main()