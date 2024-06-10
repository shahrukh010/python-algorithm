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

#working with csv data
import csv

data = [['name','email_id','phone_number'],
        ['Hector','hector@gmail.com','9505663563'],
        ['James','james@gmail.com','9505663563'],
        ['Jack','jack@gmail.com','9505663564'],
        ['Jill','jill@gmail.com','9097620737']]

#write a csv file
with open('data.csv','w') as file:
  writer = csv.writer(file)
  for row in data:
    writer.writerow(row)


# #read a csv file
# with open('data.csv','r') as file:
#   read_data = csv.reader(file)
#   for read in read_data:
#     print(read);

# #read ticket csv 
# with open('ticket.csv','r') as ticket:
#   ticket = csv.reader(ticket);
#   for data in ticket:
#     print(data)
  

import io;

#write a binary file data
# with open('new_file.txt','wb') as bf:
#   buffer_writer = io.BufferedWriter(bf);
#   buffer_writer.write(b"Hello world");
#   buffer_writer.close()

with open('new_file.txt','rb') as br:
  reader_file = io.BufferedReader(br);
  print(reader_file.read());

  