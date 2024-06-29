#A Set is an unordered collection data type that is unindexed, mutable, and has no duplicate elements. Sets are created with braces.

my_set = {"apple", "banana", "cherry"}
print(my_set)

#or use the set the function
my_set2 = set(["one", "two", "three"])
my_set2 = set(["one", "two", "three"])
print(my_set2)

my_set3 = set("aaaabbbcccddccffffff")
print(my_set3)

#add element
my_set = set()

#use add method to add elements
my_set.add(42)
my_set.add(True)
my_set.add("Hello")
print(my_set)

#remove elements
my_set = set(["apple", "orange", "banana", "cherry"])
my_set.remove("banana")
print(my_set)
my_set.discard("cherry") ## discard(x): removes x, does nothing if element is not present
print(my_set)
my_set.clear()
print(my_set)

a= {True, 2, False, "hi", "hello"}
print(a.pop()) #pop(): return and remove a random element
print(a)

#check if element is in set
my_set = {"apple", "banana", "cherry"}
if "cherry" in my_set:
    print("yes")
else:
    print("no")

#iterating using for-loop
my_set = {"apple", "banana", "cherry"}
for x in my_set:
    print(x)


#union and intersection
odds = {1,3, 5, 7, 9}
even = {2,4,6, 7, 8,10}
primes ={2,3,5,7}

u = odds.intersection(even)
print(u)

i = odds.intersection(primes)
print(i)    

i = even.intersection(primes)
print(i)

#difference: returns a set with all the element from setA that are not in setB
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff_set = setA.difference(setB)
print(diff_set)

#A.difference(B) is not the same as B.difference(A)
diff_set = setB.difference(setA)
print(diff_set)

# symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
diff_set = setA.symmetric_difference(setB)
print(diff_set)

# A.symmetric_difference(B) = B.symmetric_difference(A)
diff_set = setB.symmetric_difference(setA)
print(diff_set)

#Updating Sets
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

#update: update the set with elements from different sets
setA.update(setB)
print(setA)

#intersection_update: update the set by keeping only the elements found in both
setA.intersection_update(setB)
print(setA)

#difference_update: update the set by removing elements from another set
setA = {1,2,3,4,5,6,7,8,9}
setA.difference_update(setB)
print(setA)

#symmetric_difference_update: update the set by only keeping the elements found in either set, but not in both
setA = {1,2,3,4,5,6,7,8,9}
setA.symmetric_difference_update(setB)
print(setA)


#COPYING



