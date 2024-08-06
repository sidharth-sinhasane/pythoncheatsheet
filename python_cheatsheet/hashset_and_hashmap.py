hash_set=set()


hash_set.add(1)
hash_set.add(4)
print(len(hash_set))
print(hash_set)
#search O(1) imp
print(4 in hash_set)

#remove 
hash_set.remove(1)
arr=[1,2,4,6,8,2]
print(set(arr))

#hash tuple
print("__________________________")
tp=(2,5,7)
hashtup=set()
hashtup.add(tp)
for ele in hashtup:
    print(ele)


#________________hashmap
mymap={}
# {}
mymap["sid"]=58
#     key    =val
# {"sid":58}
mymap["pranya"]=62
mymap["shreya"]=54
print(mymap)

print(len(mymap))

# change
mymap["sid"]=59

#search
print("pranya" in mymap)
#  only keys can be sourch!!!!!!!!!!!!!
#  keys are uniqe    not the values

#remove
mymap.pop("pranya")
#  key and value both pop


#shortcut to count accorances of elements in list
l=[1,3,5,6,3]
# count=Counter(l)
#initialise
mymap={7:0,34:3}

#initialize
for key in mymap:
    print(key,mymap[key])

for key,val in mymap.items():
    print(key,val)
