#Check if a number is Armstrong or not
num = int(input("Enter a number : "))

digcount=0
orignum = num
res = 0
digcount = len(str(num))
while orignum !=0:
    dig = orignum % 10
    res = res + dig**digcount
    orignum=orignum//10
if res==num:
    print("Armstrong")
else:
    print("Not Armstrong")

#Extention
print("Toprint the Armstrong numbers betwwen a given range")
print("Enter the range of numbers :")
lim1=int(input("enter the lower limit : "))
lim2=int(input("Enter the upper limit : "))

for i in range(lim1,lim2+1):
    digcount2 = len(str(i))
    number = i
    res1=0
    while number !=0:
        dig1 = number % 10
        res1 = res1 + dig1**digcount2
        number=number//10
    if(res1==i):
        print(i)
    else:
        continue
