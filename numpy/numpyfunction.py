import numpy;

#use repeat function to create array

input = numpy.repeat([3,2],5,axis=0)
print(input);

#uses of power function 
input = numpy.array([1,2,3,4,5])
print(numpy.power(input,[2]));
sq_result = numpy.power(input,[0,2,4,5,0]);
print(sq_result)

#use of sort function.
arr1 = [2,1,3,0,4]
arr2 = [7,6,9,8,10]

vsort_array = numpy.sort([arr1,arr2],axis=0)
print(vsort_array)
#horizentoall sort
print(numpy.sort([arr1,arr2],axis=1));



#search function in numpy
random_data = numpy.array([5, 10, 15, 20, 25])

result = numpy.where(random_data==10)
print(result);
result = numpy.where(random_data < 0)
print(result);
result = numpy.where(random_data > 10)
print(result);
