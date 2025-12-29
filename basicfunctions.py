def oneplusone():
 x = 1 + 1
 return x
output = oneplusone()
print(output)

def dividedbytwo(x):
    output = x / 2
    return output
dividend = 10
y = dividedbytwo(dividend)
print(y)

def product(x,y,z):
    output = x * y * z
    return (output)
a,b,c = 1,3,4
print (product(a,b,c))

def circle_area(r):
    pi = 3.1415926
    output = pi * r * r
    return output
radius = 8
print(circle_area(radius))

def sum_list(mylist):
    sum1 = 0
    for x in mylist:
      sum1 = sum1 + x
    
    sum2 = sum(mylist)
    return sum1,sum2
a = range(101)
print(sum_list(a)[0],sum_list(a)[1])

def product_list(mylist):
    product1 = 1
    for x in mylist:
        product1 = product1 * x
    #product2 = prod()
    return product1
b = [1,2,3,4]
a = a[1:]
print(product_list(a))

def sum_variant(mylist):
    index = 0
    sum1 = 0
    for x in mylist:
        index = index + 1
        if index % 2 == 0:
          x = x * -1
        sum1 = sum1 + x
    return sum1
c = [0,1,2,3,4,5,6]
print(sum_variant(c))
