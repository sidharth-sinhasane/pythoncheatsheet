#____________ basic + list

#variables are dynamically type

#increment 
n=8
n+=1

#ifn
if n>2:
    n*=1

# and == &&
# or == ||

#loop 
n=0
while n<5:
    print(n)
    n+=1


for i in range(5,1,-1):
    print(i)

#5 4 3 2 one nahi aayega

arr=[0,2,4,5,7]
for ele in arr:
    print(ele)

#division 
print(5/2)#2.5
print(5//2)#2l
# ___________________________________________________________
#infinity
a=float("inf")
b=float("-inf")
#numbers do not overflow


#___________________ list

arr=[1,3,5]
arr.append(8)  # o(1)
#1,3,5,8
arr.pop()      # o(1)
#1,3,5
arr.insert(1,4)    # o(n)
#1,4,3,5

print(arr.pop(2))
print(arr)
print(len(arr))     #o(1)


lis=[0]*3    #[0,0,0]

arr[1:3]  #slicing

#unpaking
a,b,c=[7,9,3]

#loop through
# arr 1,3,4,5
for index,value in enumerate(arr):
    print(index,value)
    #output   
    # 0 1
    # 1 3
    # 2 4
    # 3 5
for val in arr:
    print(val)
    #1 3 4 5
#zip
nums1=['sam',"ram","babu"]
nums2=['raju',"alexande","arther"]

for n1,n2 in zip(nums1,nums2):
    print(n1," ",n2)

# output
# sam raju
# ram alexande
# babu arther 

#reverse
nums1.reverse()
# babu ram sam
nums2.sort(reverse= True)
# nums3=sorted(nums2) not nessary to create new arr
# just do nums2.sort()

#list comprehension
arr=[i for i in range(5)]
# arr=[0,1,2,3,4]


