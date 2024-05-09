import numpy

#create a numpy nd array
digits = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(digits)

#single daimension array
digit = numpy.array([1, 2, 3, 4, 5])
print(digit)
print(digit.data)
#shape of array.
print(digit.shape)
print(digits.shape)
#data type of array
print(digit.dtype)

print(digit.strides)

data = numpy.array([(0.1, 2, 3), (2.5, 3.6, 7), (5.5, 6, 7)], dtype=float)
print(data)

#create array of zeors
zeros = numpy.zeros((4, 3))
print(zeros)
#create radom
random_data = numpy.random.random((4, 4))
print(random_data)
random_data = numpy.random.randint(10, 20, size=(4, 4), dtype=numpy.int16)
print(random_data)

#data_arrange = numpy.arange(10,25,5);
data_arange = numpy.arange(1, 10, 1)
print(data_arange)

#iterate nd-array.
a = numpy.array([[1, 2, 3], [4, 5, 6]])
for x in numpy.nditer(a):
  print(x)

data = numpy.array([['apple', 'banana'], ['cat', 'dog'], [20, 30]])

#iterate nd-array using nditer.
for d in numpy.nditer(data):
  print(d)

#iterate only specific exits
data = numpy.array([[1, 2, 3], [4, 5, 7], [8, 9, 10]])
for d in numpy.nditer(data, flags=['buffered'], op_dtypes=['str']):
  #print(type(d));#numpy.array
  #print(type(d.dtype));#Float
  print(type(d.dtype))

#print the first and second columns from all rows
for nums in numpy.nditer(data[:, :2]):
  print(nums)

# By using the nditer() function, we can retrieve only the data without the indexes. To access the indexes, we can utilize the ndenumerate() function.

for index, nums in numpy.ndenumerate(data):
  print(f"[{index}]={nums}")

#Get the shape of array;
print(data.shape)

#perform arithmatic operation on array.

a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])
c = a + b
# it will perform arithmetic operation because of daimension and shape both are same.
print(c)

b = numpy.array([4, 5, 6, 7])
#print(b.shape);
#c = a+b; #not perform because of shape are not same.3X4

a = numpy.array([10, 20, 30])
b = numpy.array([40])
c = a + b
#in this case we are getting result because of numpy using broadcasting b array becomes like [40,40,40]
print(c)

#perform arithmatic operation on ndarray.
a = numpy.array([[10, 20], [30, 40], [50, 60]])
b = numpy.array([10,20]);
c = a+b;
print("a+b")
print(c);


                                  #Accessing 1-d array multiple way

#To access random data from ndarray using random index
input = numpy.array([10,20,30,40,50,60,70,80,90,100])

indexes = numpy.array([0,2,4,6,8]);
result = input[indexes];
print(result);
#we can pass list to the array.
l = [1,3,5,7,9];#list
print(input[l]);

result = input[[0,1,2,0,0,7,7]]#we can see here same element can access multiple times
print(result);


#Accessing Elements From 2nd array.
input = numpy.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]);
result = input[[0,1,2,3],[0,1,2,3]]#accessing 2nd array element.
print(result);#1,6,11,16
print(type(result))

result = input[[1,3],[0,2]]#specific result.
print(result);


#Access Eelement From 3-d Array

input = numpy.array([[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]],
[[13,14,15,16],
[17,18,19,20],
[21,22,23,24]]
])
print(input.shape);

result = input[[0,1],[0,1],[0,1]];
print(result);


#Accessing array element based on some condition
input = numpy.array([10,-5,20,30,-40,50,60,-70,80,90,-100]);
#it will give all boolean result[true,false,....]
boolean_array = input < 0;
print(boolean_array);

#select all the element which are less than 0.
result = input[input < 0]
print(result);
#select all the element which are greater than 30
result = input[input > 30]
print(result);

#print(input);
a = input[0:6]#numpy slice it will create view of object
print(a);
a[0] = 100;#if you change the value of a it will change the value of input array.(because of it logical view of physical)
print(input);
print(a);


#advance indexing to create view of array.
input = numpy.array([10,20,30,40,50,60]);
nums = input[[0,2,4]];
print(nums);
nums[0] = 100;
print(input);
print(nums);
print(input);#it will not change the value of input array. because of instead of sclice we are using indexes to create nums array.



#perform arithmatic operation.
print(10+5);
print(10-5);
print(10/50.0);
print(10/10);
print(10//10);
print(10%10);
print(10*2);#multiplecation.
print(10**2);#square

#arithmatic operation on ndarray.
print(input);
print(input+2)
print(input-2)
print(input%2);
print(input*2)
print(input**2);
#print(input / 0)

#arithmatic operation array with array
a = numpy.array([100,200,300,400])
b = numpy.array([10,20,30,4]);
print(a+b);
print(a-b);
print(a*b);
print(a/b);
print(a%b);
print(a**b);

nums = numpy.array([[1,2,3,4],[5,6,7,8]])
#adding multiple daimensional array.
print(nums+nums);


#perform arithmatic operation using function.
print("**********")
a = numpy.array([10,20,30,40]);
b = numpy.array([1,2,3,4]);
print(numpy.add(a,b));
print(numpy.subtract(a,b));
print(numpy.multiply(a,b));
print(numpy.power(a,b));
print(numpy.mod(a,b));
