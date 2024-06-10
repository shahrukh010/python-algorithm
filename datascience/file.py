import os

from pandas.io.parquet import json;
data = open('newfile.txt','r');

read_data = data.read();
#print(read_data);
print(data.readline());
#start again from the begining of the file.
data.seek(0);
#print(data.readline());

#Get the size of file
size = os.path.getsize("newfile.txt");
print(size);

#os.rename('file.txt','newfile.txt')

import shutil

#copy fill̥e
new_file = shutil.copy("newfile.txt",'new_file.txt')

#working on json data
data = {
  'name':"Hector",
  'mail_id':'hector@gmail.com',
  'phone_number':9505863563,
  'subject':['numpy','pandas','python','machine learning']
}
import json
#write a dictonary to a json file.
with open('data.json','w') as file:
  json.dump(data,file);

#read a json file.
with open('data.json','r') as file:
  data1 = json.load(file);

#print(data1);
result = data1['subject'];
print(result);
result = data1['subject'][2];
print(result);


  

