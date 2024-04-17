import numpy

nilai1 = [85,76,94,83,83,82,77,77,79,79,85]
nilai2 = [80,82,80,87,82,84,77,84,83,80,82]
nilai3 = [84,84,85,85,82,90,86,84,85,90,88]
nilai4 = [83,86,83,90,79,90,84,90,86,90,90]

seluruh = [nilai1,nilai2,nilai3,nilai4]
for x in seluruh:
    a = numpy.mean(seluruh)
    print(a)

a = numpy.mean(nilai1)
b = numpy.mean(nilai2)
c = numpy.mean(nilai3)
d = numpy.mean(nilai4)

print(a)
print(b)
print(c)
print(d)