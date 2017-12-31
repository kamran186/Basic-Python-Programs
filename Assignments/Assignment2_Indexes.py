#Indexes are also known as Arrays in many Languages

test1=["Kamran",'K','a','m','r','a','n',186];
print(test1)

#If we want to add something in array
test1.append('gjhj')
print(test1)

#If we want to remove element from array
test1.pop(); #This will remove the last element from array
print(test1)


#If we want to remove the element by its index and see the removed element
print(test1.pop(3))
#After Effects
print(test1)

#If we want to see the sorted list
test2=[1,2,6,0,-1]
print(sorted(test2))

#We can also save it in some variable
SortedTest2=sorted(test2)
print(SortedTest2)



#If you vant to add all the squares of the given range in index
square0=[];
for value in range(1,11):
    square0.append(value**2);
print(square0)

#A very simple way of this work is given in Python
square=[value**2 for value in range(1,11)]
print(square)


