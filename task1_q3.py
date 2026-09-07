class Sorter:
    def selction_sort(self,arr):
        n=len(arr)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if arr[j].lower()<arr[min_index].lower():
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
class Searcher:
    def binary_search(self,arr,target):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid].lower()==target.lower():
                return mid
            elif arr[mid].lower()<target.lower():
                low=mid+1
            else:
                high=mid-1
        return -1
n=int(input("enter the number of strings"))
arr=[]
for i in range(n):
    arr.append(input("enter the string: "))
sorter=Sorter()
searcher=Searcher()
sorter.selction_sort(arr)
target=input("enter the string to search: ")
index=searcher.binary_search(arr,target)
if index!=-1:
    print("found at index ",index)
else:
    print("stringnot found")
