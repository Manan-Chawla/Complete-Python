<<<<<<< HEAD
# array
# array is collection of homogenous data strucutre or element

from array import * # type: ignore

# syntax : arr_name=array(typecode,[initalizer])
my_arr = array('i',[1,2,3,4])

# adding element in last
my_arr.append(5)


# adding element using index
my_arr.insert(0,0)

# extending a array using another array
my_extnd_array = array('i', [7,8,9,10])
my_arr.extend(my_extnd_array)


# remove
my_arr.remove(0)



for ele in my_arr:
 print(ele)

=======
# array
# array is collection of homogenous data strucutre or element

from array import * # type: ignore

# syntax : arr_name=array(typecode,[initalizer])
my_arr = array('i',[1,2,3,4])

# adding element in last
my_arr.append(5)


# adding element using index
my_arr.insert(0,0)

# extending a array using another array
my_extnd_array = array('i', [7,8,9,10])
my_arr.extend(my_extnd_array)


# remove
my_arr.remove(0)



for ele in my_arr:
 print(ele)

>>>>>>> f124a1fcc03fb8662e4e7786201ec0d2cecb7478
