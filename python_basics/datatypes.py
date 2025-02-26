
# various data types in Python
num1=90
float1=11.7
complex1=1+5j
list1 = [17,8,9]
tuple1 = (35,36,37)
dict1= {1: "Nairobi", 2: "Mombasa"}
set1 = {1,2,3,4,5}
bool1 = True

# printing the data types of various variables using f-strings
print(f"num1: \t\t{type(num1)}\nfloat1: \t{type(float1)}\ncomplex1: \t{type(complex1)}\nlist1: \t\t{type(list1)}\ntuple1: \t{type(tuple1)}\ndict1: \t\t{type(dict1)}\nset1: \t\t{type(set1)}\nbool1: \t\t{type(bool1)}\n")

#  Type conversion
result1 = float(num1)
result2 = int(float1)

# Print the results
print("\tResult 1 is: {} \n \tResult 2 is: {}".format(result1, result2))