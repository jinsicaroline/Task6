#Program 1

import numpy as np

list1 = np.array([10,501,22,37,100,999,87,351])

only_odd = list1[list1 % 2 == 1]

print(only_odd)

only_even = list1[list1 % 2 == 0]

print(only_even)

#output : 
[501  37 999  87 351]
[ 10  22 100]

#............................................................................................................#

#Program 2

mylist =[10,501,22,37,100,999,87,351]
prime =[]
for i in mylist :
    c=0
    for j in range(1,i):
        if i%j == 0:
            c+=1
    if c==1:
        prime.append(i)
print(prime)

#output : [37]

#...........................................................................................................#

#Program 3


a = [10,501,22,37,100,999,87,351]
b = []
def happy(a):
    for i in range (len(a)):
         sum = a[i]
    while sum!=1 and sum !=4:
       tempsum=0
       for digit in str(sum):
        tempsum += int(digit) ** 2
         sum = tempsum
         if sum == 1:
          b.append(a[i])
         return sum
         print(happy(a))

#output : [10,100]

#............................................................................................................#

#Program 4

number = 3456

number = str(number)

first_digit = int(number[0])

last_digit = int(number[-1])

addition = first_digit + last_digit

print("Addition of first and last digit of the number is", addition)

# output : Addition of first and last digit of the number is 9

​

#...........................................................................................................#

#Program 5

def man(n, m):
res = 1

if m > n — m:
m = n — m

for i in range(0, m):
res *= (n — i)
res /= (i + 1)

return res
# helper function for generating no of ways
# to distribute n mangoes amongst m student
def calculate(n, m):

# not enough mangoes to be distributed
if n<m:
return 0

# ways -> (m + n-1)C(m-1)
ways = man(m + n-1, m-1)
return int(ways)

# Driver function
if __name__ == ‘__main__’:

# n represents number of mangoes
# m represents number of people
n = 7 ;m = 5

result = calculate(n, m)
print(result)

#output : 330

#.........................................................................................................#

#Program 6

def Intersets(arr1, arr2, arr3):
common = list(filter(lambda x: x in arr2 and x in arr3, arr1))


arr1 = [1, 5, 10, 20, 80, 50]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 50, 70, 80]

Intersets(arr1, arr2, arr3)
print(common)

#output : [20, 80]

#...........................................................................................................#

#Program 7

def count(arr, n):

visited = [False for i in range(n)]

for i in range(n):

if (visited[i] == True):
continue

count = 1
for j in range(i + 1, n, 1):
if (arr[i] == arr[j]):
visited[j] = True
count += 1
if count == 1 :
print(arr[i]);

arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)

#output : 
30
40
50

#..............................................................................................................#

#program 8

list1 = [21, 67, 3, 98]

list1.sort()

print(“Smallest element is:”, list1[0])

#output : Smallest element is: 3

#.................................................................................................................#

#Program 9

from itertools import combinations

def findTriplets(lst, key):

def valid(val):
return sum(val) == key

return list(filter(valid, list(combinations(lst, 3))))

lst = [10,20,30,9]
print(findTriplets(lst, 59))

#output : [(20, 30, 9)]

#...............................................................................................................3

#Program 10

def subArray(arr, l):
for i in range(l — 1):
s = arr[i]
for j in range(i + 1, l):
s += arr[j]
if s == 0:
return True
return False

array = [4, 2, -3, 1, 6]

print(subArray(array, len(array)))

#output : True

#.................................................................................................................#





