#largest and smallest element from a list without using min max function

a=[100,-6,589,10,2,3,-999,18,23,9]
max=a[0]
min=a[0]
for i in range(len(a)):
    #to find the largest
    if(a[i]>max):
        max=a[i]
    #to find the smallest
    if(a[i]<min):
        min=a[i]
print("Max value ",max)
print("Min value ",min)