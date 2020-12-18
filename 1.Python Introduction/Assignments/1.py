# WAP to find area of triangle

def main():
	print("Enter the base and height of triangle")
	length,breadth=input().split()
	#calculation part
	area=0.5*float(length)*float(breadth)
	print("Area of triangle is ",int(area))
	
if(__name__=='__main__'):
	main()