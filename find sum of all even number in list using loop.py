#find sum of all even number in list using loop
lst=[1,2,3,4,5,6,7,8,9,10]
sum=0
for n in lst:
    if n%2==0:
        sum=sum+n

print(sum)

#find diff of all even number in list using loop
lst=[1,2,3,4,5,6,7,8,9,10]
diff=0
for n in lst:
    if n%2==0:
        diff=diff-n

print(diff)

#find product of all even number in list using loop
lst=[1,2,3,4,5,6,7,8,9,10]
pro=1
for n in lst:
    if n%2==0:
        pro=pro*n

print(pro)