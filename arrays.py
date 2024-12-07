import array as arr


# ------ Creating an array with integer datatype -------

a = arr.array('i',[1,2,3])

# ------- Print original array -----

print("The array created is: ",end = " ")
for i in range(0,3):
    print(a[i],end = " ")
print()


# ----- Create the floating type ------

b = arr.array('d',[2.3,4.5,5.5])

# ------printing the array -------

print("The array is : ",end = " ")
for i in range(0,3):
    print(b[i],end = " ")
