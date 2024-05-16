#variable length argument
def fun(a,b,*args):
  for x in args:
    print(x)
  print(a,b);

fun(10,20,1,2,3,4);

#unpack argument
def unpack(a,b,c):
  return a+b+c;


l = [1,2,3];
#unpack depends on the length of list item
print(unpack(*l));

#function can return multiple item;
def multiple(a,b,c,d):
  return a+1,b**2,c-2,d/2;

add,mul,sub,div = multiple(1,2,3,5);
print(add,mul,sub,div);

#keyword argument function
def keywordfun(**kwargs):
  for key in kwargs:
    print(key,kwargs[key]);

keywordfun(name="annie",age=22,city="Hyd")

#mixed argument
def mixed(a,b,*args,**kwargs):
  pass
#note:-> first must be postional argument->variable length->keword argument  


#yield is used save the function same state.
def days():
  L = ['sun','mon','tue','wed','thu','fri','stat']
  i = 0;
  while True:
    x = L[i];
    i = (i+1)%7
    yield x;

day = days();
print(next(day));
print(next(day));
print(next(day));
print(next(day));
print(next(day));
print(next(day));
print(next(day));

#global variable vs local variable.

g = 10;
def globalLocal(a,b,):
  c = a+b;#local
  print(c);#local
  print(g);#global

variable = globalLocal(1,2);

#change global from local
def funglobal():
  global g;
  g = g+1
  print(g);

fun = funglobal();

print(g);

#print the local variable
def local(a=10,b=20):
  x,y,z = 1,2,3
  print(locals())#locals() will print the local variable.
l = local()
#globals() will print the global variable.
#print(globals())

#builtin function
print(abs(10.5));
print(abs(-5.0))#absolute value.
print(ascii('a'));
print(bool(0))
print(bool(1));
print(bool('annie'))
print(bool(''))
print(chr(65))
l = [5,4,3,2,1];
print(l);
print(sorted(l));

#filter
L = [1,2,3,4,5,6,7,8,9,10];
def even(value):
  if value%2==0:
    return True;
  else:
    return False;

result = filter(even,L);
for r in result:
  print(r);

def odd(x):
  if x%2 !=0:
    return True;
  else:
    return False;

oddresult = filter(odd,L);
for odd in oddresult:
  print(odd);


#check attribute.
s = "annie";
print(hasattr(s,'lower'));
print(hasattr(s,'upper'))
print(hasattr(s,'len'))

#instance 
s = "abc"
n = 10;
f = 10.5;
#use isinstance() this function before use any object check instance of it or not.
print(isinstance(s,str));
print(isinstance(n,int))
print(isinstance(f,float))


#function as object.
def display(name=None):
  print("hello",name)

#assign function as object to d
d = display
d('hector');

#define inner function
def Outer():
  def inner():
    print("inner function");
  inner();

Outer();


#function as parameter.
def add(x,y):
  print(x+y)
def sub(x,y):
  print(x-y)
def fun(f,x,y):
  f(x,y);

#passing function as parameter.
fun(add,10,20);
fun(sub,20,15)

#return as function
def Outer():
  def display():
    print("hello fun")
  return display;#returning display function as object.

d = Outer();
d();


#use of lambda
sum = lambda x,y:x+y;

total = sum(10,20);
print(total);
square = lambda a:a**a;
print(square(2));

def miles2km(miles):
  kms = 1.6*miles;
  return kms;

print(miles2km(10))

kms = lambda miles:1.6*miles;
print(kms);


#working with random function
print("******************************")
print("******************************")
print("******************************")
import random;
print(random.random());
print(random.random());
result = random.uniform(1,10);
print(result);
import math
print(math.floor(result))
print(random.randint(1,10))#only integer number

print(random.randrange(1,10,3));

l = [ 'annie','hector','bridget']
print(random.choice(l));
print(random.choices(l,k=3))#three random data will be printed from list

l = [1,2,3,4,5]
random.shuffle(l);
print(l);

