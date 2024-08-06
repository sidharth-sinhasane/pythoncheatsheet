s="abcsd"

print(s[0:3])
# abc

#immutable
# s[1]='k' not possible 

s+= "aha"  #new string is created o(n) time operation with o(n) space

s=list(s)#list of string
#conversion
print("986" )
u=int("986")
print(u)
# 986
m=str(u)
# "986"



#get ascii
print(ord("u"))

strings=["ab","cd","mn"]
print("________________________")
print(strings)
print("".join(strings))   #ad cd mn

# itorate 

name="shreya ji"
for ele in name :
    print(ele)

for i in range(len(name)):
    print(name[i])

for ind,val in enumerate(name):
    print(ind ," ->", val)

some=0
while some<len(name):
    print(name[some])
    some+=1