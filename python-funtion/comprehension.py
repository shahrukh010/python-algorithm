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


#dictionary.

dict_data = {
  "name":"hector",
  "age":24,
  "city":"Hyd",
  "is_student":False,
  "grades":[85,77,90]
}

#dictionary function
print(dict_data['name'])
print(dict_data.values());
#print(type(dict_data.keys()));
print(dict_data.keys());

for key in dict_data.keys():
  print(key,'::',dict_data[key]);

get_key_list = [key for key in dict_data.keys()];
print(get_key_list);
get_value_list = [value for value in dict_data.values()]
print(get_value_list);

print(dict_data);
dict_data['age'] = 22;
print(dict_data);

#adding data to dictionary.
dict_data['designation'] = 'SDEII';
print(dict_data);
#delete key;
del dict_data['designation'];
print(dict_data);

#by default dictionary print key
for key in dict_data:
  print(key);


#initalize dictionary.

di = dict();
print(di);
for i in range(1,3):
  di[i] = i**2;
print(di);  

dict_tuple = dict(((1,1),(2,2),(3,3)));
print(dict_tuple);
dict_list = dict([[10,10],[20,20]])
print(dict_list);
print(dict_list.keys());
dict_str = dict(('an','he'));
print(dict_str);

#using zip function to create dictionary.
l1 = ['name','age','city']
l2 = ['Annie','23','Hyd']

dict_zip = dict(zip(l1,l2));
print(dict_zip);
str = 'ABC'
dict_zip = dict(zip(l1,str));
print(dict_zip);

#enumerate
list = ['annie','hector','bridget','nic'];
enumerated_data = [data for data in enumerate(list)]
#print(enumerated_data);
#convert enumerated_data to dictionary
dict_enumerate = dict((enumerated_data));
print(dict_enumerate)
#iterate dictionary;
for key,value in dict_enumerate.items():
  print(key,value);

list = ['one','two','three']
enumerate_dict = dict(enumerate(list));
for key,value in enumerate_dict.items():
  print(key,value);

for x in enumerate_dict:
  print(x,enumerate_dict.get(x))

#what if key is not avilable
print(dict_enumerate.get('one','invalid key'));

#dictionary method example

product_data = {
  "product_id":1,
  "product_name":"Laptop",
  "price":1000,
  "in_stock":True,
  "categories":["Electronic","Computers"]
}

print(product_data);
#create shallow copy
pdata = product_data.copy();
pdata['image'] = 'https://image.com/image.jpg'
print(pdata);

p_data = {"manufacturer":"ABC","color":"Silver"}

print(pdata.get('image','invalid key'));
print(p_data);
#update new dictionary to existing
pdata.update(p_data);
print(pdata);
for key,value in pdata.items():
  print(key,value);

print(pdata.get('price'));
#get method will throw None if key is not exists
print(pdata.get('brand'));
#setdefault method will add key if not exists value willbe None if you not privide
pdata.setdefault('brand','Lenovo')
print(pdata);

#fromkeys method it will take keys from list/iterable.

l = ['one','four','six'];
fromkeys_dict = {};
fromkeys_dict = fromkeys_dict.fromkeys(l,10);
#print(fromkeys_dict);
print(p_data);
#p_data.pop('color');
#popitem will delete item from last
p_data.popitem();
print(p_data);

p_data.clear();
print(p_data);


