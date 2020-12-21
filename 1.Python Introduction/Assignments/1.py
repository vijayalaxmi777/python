# WAP to find area of triangle

def main():
 #print("Enter the base and height of triangle")
 #length,breadth=input().split()
 print("Enter the base of triangle")
 base=input()
 print(base)
 print(type(base))
 base=int(base)
 print(type(base))
 print("Enter the height of triangle")
 height=input()
 print(height)
 print(type(height))
 height=int(height)
 print(type(height))
 #calculation part
 #area=0.5*float(length)*float(breadth)
 area = 0.5 * base * height
 print("Area of triangle is ",int(area))
	
if(__name__=='__main__'):
	main()