import numpy;

#create a numpy nd array
digits = numpy.array([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
print(digits);

#single daimension array
digit = numpy.array([1,2,3,4,5]);
print(digit);
print(digit.data);
#shape of array.
print(digit.shape);
print(digits.shape);
#data type of array
print(digit.dtype);

print(digit.strides)

data = numpy.array([(0.1,2,3),(2.5,3.6,7),(5.5,6,7)],dtype=float)
print(data);


#create array of zeors
zeros = numpy.zeros((4,3))
print(zeros);
#create radom
random_data = numpy.random.random((4,4));
print(random_data);
random_data = numpy.random.randint(10,20,size=(4,4),dtype=numpy.int16)
print(random_data);

#data_arrange = numpy.arange(10,25,5);
data_arange = numpy.arange(1,10,1);
print(data_arange);

