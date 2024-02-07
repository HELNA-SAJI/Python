# CONTROL FLOW PYTHON

# 1.Find voting eligibility of a person using if else
# 2.Find a number zero,positive or negative
# 3.check an alphabet is vowel or not
# 4.Display numbers from -10 to -1 using for loop
# 5.Display even numbers in the range of 200-500
# 6.Diplay multiples of given number in the range 1 to 100
# 7.Use a loop to display elements from a given list present at odd index positions
# 8.Print multiplication table of given number
# 9.Using for loop print characters of welcome.If value of i=c stop the program
# 10.Using for loop print characters of hello world and skip the word "w"

# 1.Find voting eligibility of a person using if else

num=int(input("\n  enter the age of the person"))
if num>=18:
    print("Person is eligible for voting")
else:
   print("Person is not eligible for voting") 
   
#  2.Find a number zero,positive or negative
n=int(input("\n enter the number"))
if n==0:
    print("number is zero")
elif n>0:
    print("number is positive")
else:
   print("number is negative") 
   
#3.check an alphabet is vowel or not
vow=['a','e','i','o','u','A','E','I','O','U']
let=input("\n Enter the letter")
if let in vow:
        print("\n Letter is vowel")
else:
     print("\n Letter is not a vowel.It is a consonant")

#  4.Display numbers from -10 to -1 using for loop
print("\n NO'S from 10 to -1")
for i in range(10,-2,-1):
        print(i)
    
#5.Display even numbers in the range of 200-500
print("\n The even numbers between 200 and 500 is ")
for i in range(200,501):
    if(i%2==0):
        print(i)


# 6.Diplay multiples of given number in the range 1 to 100

number=int(input("\n Enter the number"))
for i in range(1,100):
    if i%number==0:
        print(i)
#  7.Use a loop to display elements from a given list present at odd index positions

l1=['red','blue','green','yellow']
print("\n orginal list",l1)
l2=[]
count=0
for i in l1:
    if (count%2)==0:
            l2.append(i) 
    count=count+1
print("\n list of elements present at odd index positions",l2)             
                  

# 8.Print multiplication table of given number
numb=int(input("\n Enter the number"))
print("Multiplication table of ",numb)
for i in range(1,11):
    print(i,"*",numb,"=",i*numb)
# 9.Using for loop print characters of welcome.If value of i=c stop the program
str1="welcome"
print("\n")
for i in str1:
        if i=="c":
            break  
        print(i)   

print("\n")
str1="Hello world"
for i in str1:
        if i=="w":
           continue
        print(i)   