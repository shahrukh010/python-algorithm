
                #handling exception
dummy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
  index = int(input("Enter your index"));
  print(dummy_list[index]);
except:
  print('invalid index.')

#raise exception with custom message

try:
  n = int(input('Enter your number'));
  if n > 5:
    raise Exception(f'Number should be less then 5 {n=}');
finally:
  pass

#useing assert 
n = 5;
assert(n>1),f"Number should be less then 1 {n=}"  
print(n);


def linux_interaction():
  import sys;
  if 'linux' not in sys.platform:
    raise RuntimeError('This function is only for linux');
  print('Doing linux things');
  #print(dir(sys.platform));

try:
  linux_interaction();
except RuntimeError as error:
  print('**5')
  print(error);
  print('Linux is not supported');
else:#else block will be executed if there is not any aception
  try:
    with open('file.log') as file:
      read_data = file.read();

  except FileNotFoundError as fnf_error:
    print(fnf_error);
    

# try:
#   with open('file.log') as file:
#     read_data = file.read();
# except FileNotFoundError as error:
#    print(error);


#Create custom exception

class PlatformException(Exception):
  pass

def linux_interaction():
  import sys;
  if 'linux' not in sys.platform:
    raise PlatformException('THIS FUNCTION IS ONLY FOR LINUX')

  print('Doing linux things');

linux_interaction();


#consumeing api

import requests;
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url);
print(response.status_code);
print(response.headers['Content-Type'])
data = response.json();

#print(data);
for key,value in data.items():
  print(key,value);


#post the data 
product_data = {
  "Id":101,
  "Name":"Laptop",
  "Price":19.00,
  "category":"Electronics"
}
api_url = "https://jsonplaceholder.typicode.com/todos";
post_response = requests.post(api_url,json = product_data);
print(post_response.status_code);
#print(post_response.json());
response = requests.get(api_url+'/'+'101');
print(response.json());