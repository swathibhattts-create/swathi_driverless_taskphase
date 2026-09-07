n=int(input("enter the no of integers"))
hash_table=[[] for _ in range(10)]
for i in range(n):
    num=int(input("enter the integer"))
    index=num%10
    hash_table[index].append(num)
print("hash table:")
for i in range(10):
    print(i,":",hash_table[i])