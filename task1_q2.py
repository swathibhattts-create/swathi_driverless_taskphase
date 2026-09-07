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
n=int(input("enter the number of strings"))
arr=[]
for i in range(n):
    arr.append(input("enter the string: "))
obj=Sorter()
result=obj.selction_sort(arr)
print(result)