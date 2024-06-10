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
result_even = numpy.where(random_data%2==0)
print(result_even);
result_odd = numpy.where(random_data %2!=0)
print(result_odd);

#search data from sorted array
sorted_data = numpy.array([1,2,3,4,5,7,8,9,10])
#it is binarysearch
result = numpy.searchsorted(sorted_data,8)
print(result);
print(numpy.searchsorted(sorted_data,100));
#search more then one element.
result = numpy.searchsorted(sorted_data,[4,8,1])
print(result);

#createing filter

data = numpy.array([10,15,17,9,8,11,20])
result =filter(lambda num: num%2==0,data);
for item in result:
  print(item,end=',');
print(result);

result = list(filter(lambda num : num%2 !=0,data))
print(result);

#createing filtering array

input = numpy.array([99, 88, 77, 66, 55])
filter_result = input>90;
print(filter_result);
print(input[filter_result]);
filter_result = input<90;
result = input[filter_result];
print(result);

input = numpy.array([1,2,3,4,5,6,7,8,9,10])
filter = input %2==0;
#all even number
print(input[filter]);

arange_data = numpy.arange(0,11);
print(arange_data);
arange_data = numpy.arange(1,10,2)
print(arange_data);