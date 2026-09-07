def sorted_list(list,ref):
    for i in range(len(list)):
        min_index=i
        for j in range(i+1,len(list)):
            d1=((list[i][0]-ref[0])**2+(list[i][1]-ref[1])**2)**0.5
            d2=((list[min_index][0]-ref[0])**2+(list[min_index][1]-ref[1])**2)**0.5
            if d2>d1:
                min_index=j
            list[i],list[min_index]=list[min_index],list[i]
        print(list)
n=int(input("enter the number of points"))
list=[]
for i in range(n):
    x=int(input("enter the x coordinate"))
    y=int(input("enter the y coordinate"))
    list.append((x,y))
rx=int(input("enter the x coordinate of reference point"))
ry=int(input("enter the y coordinate of reference point"))
ref=(rx,ry)
sorted_list(list,ref)