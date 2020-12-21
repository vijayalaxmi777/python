# WAP to print day according to the number entered by the user: elif 
def main():
 print("Enter the day in number:")
 day=input()
 day=int(day) # type casting
 if(day==1):
  print("Sunday")
 elif (day==2):
  print("Monday")
 elif (day==3):
  print("Tuesday")
 elif (day==4):
  print("Wednesday")
 elif (day==5):
  print("Thursday")
 elif (day==6):
  print("Friday") 
 elif (day==7):
  print("Saturday") 
 else:
  print("You have entered wrong number.Please enter number between 1-7.") 
if (__name__ == "__main__"):
 main()