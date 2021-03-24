a = [1,  4.9,"dhruv", 1+5j, 2, 54.88, "patel", 9+6j, 2, 8.44]


#ans2
lst = [1, 2.5, "Consultadd", 1+2j, 2]
print(lst[::-1])
print(lst[::2])
print(lst[2:])
print(lst[:3])


#ans3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = 0
lst2 = 1
for i in lst:
    lst1 += i
for i in lst:
    lst2 *= i
print("Sum of all numbers in the list:", lst1)
print("Multiplication of all numbers in the list:", lst2)

#ans4
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Largest element:", max(lst))
print("Smallest element:", min(lst))

#ans5
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1 = [i for i in lst if i % 2 != 0]
print("New list which contains the specified numbers after removing the even numbers:", lst1)

#ans6
lst = [i*i for i in range(1, 31)]
print("First 5 elements of the list:", lst[:4])
print("Last 5 elements of the list:", lst[-1:-5])

#ans7

lst1 = [1, 3, 5, 7, 9, 10]
lst2 =  [2, 4, 6, 8]

print(lst1[:-2].extend(lst2))


#ans8
a={1:10,2:20}
b={3:30,4:40}
c={}
for k, v in [a, b]:
    c[k] = v
print(c)

#ans9
n = 8
dictionary = {}
for i in range(1, n+1):
    dictionary[i] = i**2
print(dictionary)

#ams10
values =input("enter numbers")
l = values.split(",")
t = tuple(l)
print (l)
print (t)
