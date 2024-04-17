#Join two sets
#Union() method
set1 = {"a","b" ,"c"}
set2 = {3,4,5}
set3 = set1.union(set2)
print(set3)

#update() method
set1.update(set2)
print(set1)

#keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

#keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#Symmetric_difference() method will return a new set, that contains only the elements that are not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
