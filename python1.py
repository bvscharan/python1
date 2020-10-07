example list for first two tasks

data=[10,20,-109,82,198,-278,0,239]
data.sort()
print(data)
#output
[-38, -19, 0, 1, 10, 20, 122, 198, 892]

<-----------------#finding largest number in a list-------------------->
print(max(data))
#output
892

<-----------------#finding second largest number in a list------------->
print(data[-2])
#output
198


<------------------#Sorting of two lists after merging------------------>
list1 = [-38, -19, 0, 1, 10, 20, 122, 198, 892]
list2 = [0, -59, 20, 11, 761, 209, 1122, 98, -892]
list3 = list1+list2
list3.sort()                     
print(list3)
#output
[-892, -59, -38, -19, 0, 0, 1, 10, 11, 20, 20, 98, 122, 198, 209, 761, 892, 1122]


<------------------#swapping of first and last elements--------------------->
data=[10,20,-109,82,198,-278,0,239]
data[0],data[-1] = data[-1],data[0]
print(data) 
#output
[239, 20, -109, 82, 198, -278, 0, 10]
