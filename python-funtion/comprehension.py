import random;
random_function_name = [name for name in dir(random)]
for name in random_function_name:
  if name.startswith('_'):
    continue;
  print(name);

#create set
set_data = {x for x in range(10)}
print(set_data);

#comporehension data
import datetime;

fun_name = [fun for fun in dir(datetime)if  not fun.startswith('_')]
print(fun_name);

#square of number
square = [q**2 for q in range(2,12)];
print(square);

#make it upper case letter
uppercase_name = [upper.upper() for upper in dir(datetime) if not upper.startswith('_')];
print(uppercase_name)