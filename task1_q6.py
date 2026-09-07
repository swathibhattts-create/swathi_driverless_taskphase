def find_insertion_index(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
n=int(input("enter the no of integers"))
hash_table=[[] for _ in range(10)]
for i in range(n):
    num=int(input("enter the integer"))
    bucket=num%10
    index=find_insertion_index(hash_table[bucket], num)
    hash_table[bucket].insert(index, num)
for i in range(10):
    print(i,":",hash_table[i])