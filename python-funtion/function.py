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