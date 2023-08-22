# # #Q 1:-  STONE , PAPER SCISSOR GAME 

# # # John = input("John's Turn :")
# # # Bob = input("Bob's Turn :")

# # # if (John == 'paper' and Bob== 'stone'):
# # #     print("John Win's")
# # # elif (John == 'scissor' and Bob== 'paper'):
# # #     print("John Win's")
# # # elif (John == 'stone' and Bob== 'scissor'):
# # #     print("John Win's")
# # # elif (John == 'stone' and Bob== 'paper'):
# # #     print("Bob Win's")
# # # elif (John == 'scissor' and Bob== 'stone'):
# # #     print("Bob Win's")
# # # else:
# # #     print("Bob Win's")


# # #Q 2:- check Whether a number is Even or odd without using if-else.
# # # a = int(input("Enter Number"))
# # # print(a%2)


# # #Q 3:- LOTTERY TICKET GAME
# # # num = int(input("Enter Your Lottery No :"))
# # # if num>=1 and num<=20:
# # #     print("You win a refrigerator")
# # # elif num>=21 and num<=40:
# # #     print("You win a Televison")
# # # elif num>=41 and num<=60:
# # #     print("You win a Andoroid Phone")
# # # elif num>=61 and num<=100:
# # #     print("You won a car")
# # # else:
# # #     print("Uppppssss ! You didn't win Anything ")
# # #     print("Better Luck Next time")

    
# # # Q 4:-Make a program for salary distribution to employees with increment or hike.

# # # salary = int(input("Enter Your Salary Here : "))
# # # days = int(input("Enter Your Days of Working :"))

# # # if days>=25 and salary >=10000 and salary <=15000:
# # #     increment = (salary*10)//100
# # #     print("Your Total salary is :" ,salary+increment)

# # # elif days>=20 and days<=25 and salary >=10000 and salary <=15000:
# # #     increment = (salary*5)//100
# # #     print("Your Total salary is :" ,salary+increment)
 
# # # elif days<20 and salary >=10000 and salary <=15000:
# # #     increment = (salary*5)//100
# # #     print("Your Total Salary is :" ,salary-increment)
    
# # # elif days>=25 and salary >=15000:
# # #     increment = (salary*5)//100
# # #     print("Your Total salary is :" ,salary+increment)

# # # elif days<=25 and salary >=15000:
# # #     increment = (salary*5)//100
# # #     print("Your Total salary is :" ,salary-increment)
# # # else:
# # #     print("You Didn't Recieve Salary")

 
# # # i = 1
# # # string =""
# # # n= int(input("Enter Your Word Length :"))

# # # while i<=n:
# # #     a = input("Enter Your Word :-")
# # #     string +=a 
# # #     i+=1
    
# # # print(string)
     
# # # factorial

# # # n = int(input("Enter Number :"))
# # # fact = 1
# # # i=1
# # # while i<=n:
# # #     fact = fact*i
# # #     i+=1
# # # print(fact)

# # # fact = 1
# # # while n>=1:
# # #     fact= fact*n
# # #     n-=1
# # # print(fact)

# # # Find Next date..

# # date = int(input("Enter Date :"))  #31
# # month = int(input("Enter Month :")) #4
# # year = int(input("Enter Year :"))  #2001

# # if date < 29 and month ==2 and  year>0:  # 31<29 and 4==2 
# #   print(date+1,"-", month ,"-",year)
# #   if date==29 and month ==2:
# #     print(1,"-",month+1,"-",year)


# # if date <30 and (month==4 or month ==6 or month== 9 or month==11) and year>0:  # 31 < 30 and   4==4  or 4==6 or 4==9 or 4==11 and 2001>0
# #   print(date+1,"/", month ,"/",year)

# # elif date >=30 and (month==4 or month ==6 or month== 9 or month==11) and year>0:
# #     print(1,"-",month+1,"-",year)


# # elif date <31 and (month==1 or month ==3 or month== 5 or month==7 or month==8 or month==10) and year>0 :
# #   print(date+1,"=", month ,"=",year)
  
# # elif date ==31 and (month==1 or month ==3 or month== 5 or month==7 or month==8 or month==10) and year>0:
# #     print(1,"+",month+1,"+",year)   


# # Find the number is Prime or Not Using If else.......
# # n= int(input())
# # p= ((2**n)-1)% n
# # if p==1:
# #   print('Prime no')
# # else:
# #   print('Not Prime')

# # i = 1
# # while i<=10:  forloop 
# #   print(i) 1,2,3,4,5,6,7,8,9,10
# #   i+=1

# # for i in range(1,i<=10):
# #   print(i)

# 132 digits sum ;12345689
# n = int(input())
# sum=0
# while n>0:   #n=123 true 12true 1 true
#   rem = n%10  # 1
#   n//=10  # 0
#   sum+=rem   # 0+3 = 3+2=5 5+1= 6

# n= 1234576892456 sum of those digits which are divisble by 2
# n= 1234576892456
# sum = 0
# while n>0:
#   rem = n%10  #6
#   if rem%2==0:
#     sum+=rem
#   n//=10
  
  
# prime No 3 = 1,3

# find the prime number between 1 to 10;  expected Output:-2,3,5,7
# n = int(input("Enter Your Number"))
# count = 0     
# i= 1        
# while i<=n:    
#   if n%i==0:  
#     count+=1    
#   i+=1    

# if count==2:  
#   print("Prime No")
# else:
#   print("Not Prime ")

n = int(input("Enter Value: "))
target_value  = 5
count = 0

while True:
  



  
  
