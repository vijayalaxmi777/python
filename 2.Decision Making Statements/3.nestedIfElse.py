# WAP for nested if-else statement: 
#check number is divisible by 5 & 7
def main():
 #if else
 print("Please enter number")
 number = input()
 number = int(number)
 if (number %5 == 0):
  if(number % 7 == 0):
   print("Number ",number," is divisible by both.")
  else:
   print("Number ",number," is divisible by 5 only.")
 else:
  if(number % 7 == 0):
   print("Number ",number," is divisible by 7 only.")
  else:
   print("Number ",number," is neither divisible by 5 nor by 7.")
   
if (__name__ == "__main__"):
 main()