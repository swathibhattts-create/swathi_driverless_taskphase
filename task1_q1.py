n=int(input("enter the number of strings"))
strings=[]
for i in range(n):
    strings.append(input("enter the strings"))
frequency={}
for string in strings:
    for char in string.lower():
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
print(frequency)    