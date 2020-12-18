# WAP to calculate area of circle using symbolic constant

import math
def main():

	print("Enter the radius of circle")
	r=input()
	r=int(r)
	#area of circle
	a=math.pi*r*r
	print("Area of circle is ",a)

if(__name__=="__main__"):
	main()