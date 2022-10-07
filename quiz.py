counter = 1

sum = 0

while counter <= 6:

    sum = sum + counter

    counter = counter + 2

print(sum)

sum = 0

values = [1,3,5,6]

for number in values:

    sum = sum + number

print(sum)

def add(a, b):

    return a+5, b+5

 

result = add(3, 2)

print(result)

def outer_fun(a, b):

    def inner_fun(c, d):

        return c + d

 

    return inner_fun(a, b)

    return a

 

result = outer_fun(5, 10)

print(result)




class test:

      def __init__(self.a=""Welcome to Zuri""):

         self.a=a

 

      def display(self):

         print(self.a)

obj=test()

obj.display()