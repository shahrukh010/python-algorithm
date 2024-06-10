import logging
from os import remove

# logging.basicConfig(filename="test.log", level=logging.INFO)
# logging.info("test log....")
# logging.info("program is success")
# logging.warning('warning message');
# logging.error("this is my error message");

# logging.shutdown();

import os
if (os.path.exists('app.log')):
  os.remove('app.log')

logging.basicConfig(filename='app.log',
                    level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s")
# logging.info("this is info logging.")
# logging.debug("this is debug")
# logging.warning('this is warning')

input = [1, 2, 3, [4, 5, 6], 'annie', 'hector', 'bridget', 'nic']

result_int = []
result_str = []

logging.info("filtering out the integers from the list")
for i in input:
  logging.info(f"checking the type of {i}")
  if (type(i) == list):
    logging.info(f"the type of {i} is list")
    for j in i:
      logging.info(f"checking the type of {j}")
      if type(j) == int:
        result_int.append(j)
  elif (type(i) == int):
    result_int.append(i)
  else:
    result_str.append(i)

print(result_int)
print(result_str)

import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))
# print(ds.sayHello());
