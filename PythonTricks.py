#List "in" list:
setA, setB = [1,2,3,4,5], [2,4]
print(setB in setA) #False
print(set(setB).issubset(set(setA))) #True

#Str in str:
a, b = "abcdef", "bc"
print(b in a) #True
