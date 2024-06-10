import pandas;

data = pandas.read_csv('ticket.csv',header=None);

#print(data.head())
print(data.head(2));
#print(data.tail())

#Get the column name from the data.
data = pandas.read_csv('ticket.csv');
result = data.columns;
#print(result);
#print(result[2],result[4]);

#Get the data from the column
name = data[' Customer Name/ID'];
email = data[' Email Id'];
#print(name);
print(type(email));

#Convert servies to list;
result = list(name);
#print(result);

#Get The DataFrame data;
result = data[[' Customer Name/ID',' Email Id']]
print(type(result));
#print(result);


#Read the excel file
data = pandas.read_excel('Display-Brand.xlsx')
print(type(data));
#print(data);
result = data[['Brand name','Company']]
print(result);

#Generate new excel from excel file
result.to_excel('medicine.xlsx',index=False);

