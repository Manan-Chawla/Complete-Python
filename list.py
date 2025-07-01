''' 
list is more like a collection of items which can be different from each
more like we can store string, int ,float etc in a same list

syntax : 
list_name=[elements here]

list is mutable
list maintain order
list allow duplicate value within

1.list also contains index value for each element store within
2.index value always start from one
3.if we use index value in negative then it will point element from 
last position from list
4. slicing within the list or using ':' within two specific index value
   will extract element apart from index vale we used
5. we can even change value of element using index values
'''

names=['Manan','Asha','Tanu','Yash']
names.append('Dheeraj')
names[0]="Suhani"
print(names)

my_list = [1, "apple", 3.14, True]
print(my_list)

# we can even print a word or string as list using 
# list method
string_list=list("hello")
print(string_list)


# this will remove element having 1 and 3 as index value
newnames=names[1:3] 
print(newnames)