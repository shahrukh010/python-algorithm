
#opening file.
file = open("file.txt")
#print(file.read());
#read only first 5 characters;
print(file.read(5));
print(file.read(10));
file.close();

try:
  file = open("file.txt")
  print(file.read(20));
except FileNotFoundError as f_error:
  print(f_error);
finally:#use for close the external resource.
  file.close();

file = open("demo.txt","w")
file.write("Hello world\n")
file.write("This is my first file\n");

