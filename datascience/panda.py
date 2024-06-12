from operator import index
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
#print(result);
#Generate new excel from excel file
result.to_excel('medicine.xlsx',index=False);
#this will give the statistical(numrical data of the data.
print(data.describe())

#check the type of columns.
result = data.dtypes;
print(result);

#Get the data from the multiple columns;

result = data[['Company','Brand name']];
#print(result);

#Get the data which have object type only.
result = data[data.dtypes[data.dtypes == 'object'].index].head(2);
#describe:use for count,unique,top,freq of data(properties of data)
result = data[data.dtypes[data.dtypes == 'object'].index].describe();
#print(result);

result = data[data.dtypes[data.dtypes == 'int64'].index];
#print(result);
result = data[data.dtypes[data.dtypes == 'float64'].index]
#print(result);

#Get the columns
column = data.columns;
#print(column);

#Get the data from the column [from..to ]
result = data[['Company']][20:24];
#print(result);

#Load the csv data from utl
titanic = pandas.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv');
print(titanic.columns);
#print(titanic[['Name']]);

#print(titanic[['Survived']])
result = pandas.Categorical(titanic['Survived']);
#print(result);
print(titanic['Cabin'].unique())

print(titanic['Sex'] == 'male');
result = titanic[titanic['Sex'] == 'male']
print(result);

#use and opearation
result = titanic[(titanic['Sex'] == 'male') & (titanic['Age'] > 30)];
result = result[['Age','Sex']]
# print(result);
# print(result);

max_fare = titanic[titanic['Fare'] == max(titanic['Fare'])];
max_fare = max_fare[['Name','Fare']];
#print(max_fare);
max_fare = titanic[titanic['Fare'] == max(titanic['Fare'])][['Name','Fare']];
#print(max_fare);

print(titanic[['Fare','Name']].max());

print("------------------------------------------------------------------------------------------------");
print("------------------------------------------------------------------------------------------------");

df = pandas.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv');
columns = df.columns
#print(columns)

#change index instead of number use character or name
indexes = ['a','b','c','d','e','f','g','h']
s = df['Name'][0:8];
#print(s);
rename_indexes = pandas.Series(list(s),index=indexes);
#print(rename_indexes);
#print(rename_indexes['c']);

df = pandas.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv');
print(df.columns);
drop_column = df.drop('PassengerId',axis=1);
print(drop_column.columns)
#drop column permanently.
df.drop('PassengerId',axis=1,inplace=True);
print(df.columns)
print(df.head());
df.drop(2,axis=0,inplace=True);
print(df.head());

#Read dataframe
data = {
  "Name":['Annie','Hector','Nic','Bridget'],
  "Age":[20,30,40,50],
  "City":["Mumbai","Chennai","Hyderabad","Banglaure"]
}
print(pandas.DataFrame(data))
print(type(pandas.DataFrame(data)));
data = df[['Name','Cabin']];
#print(data);
#drop NaN data from file
#data.dropna(inplace=True);
print(data);

#Replace Nan value with 0
data.fillna(0,inplace=True);
print(data);


data = {
  "medicine_name":['Crocin','Paracetamol','Aspirin','Ibuprofen'],
  
  "drug_type":['Pain Reliever','Pain Reliever','Pain Reliever','Pain Reliever'],
  "mrp":[10,15,20,25],
  "selling_price":[20,25,30,35]
}
medicine = pandas.DataFrame(data);
#print(medicine)
#medicine with custom index name
medicine_index = pandas.DataFrame(data,index=['a','b','c','d'])
#print(medicine_index)



#Get the index of medicines from medicine_name column.
print(medicine_index['medicine_name']['d']);

#Reindex data
medicine_index.reindex(['d','c','a','b']);
print(medicine_index)

def total_sum(medicine):
  return medicine.sum();
result = medicine.apply(total_sum);
print(result);



mrp_seling_price = medicine[['mrp','selling_price']]
print(mrp_seling_price)
square_mrp = mrp_seling_price.applymap(lambda price : price**2);
print(square_mrp)
# nums = [x for x in range(4,10)];
# print(nums);
print(square_mrp.sort_values(by='mrp',ascending=False));

tech_dataframe= pandas.DataFrame({"technologies":[
    "**Artificial Intelligence (AI)** is a broad field of computer science that focuses on creating intelligent agents, which are systems that can reason, learn, and act autonomously. AI techniques include machine learning, deep learning, natural language processing, and computer vision, enabling machines to perform tasks that typically require human intelligence, such as understanding language, recognizing images, and making decisions.",
    "**Machine Learning (ML)** is a subset of AI that allows computers to learn from data without being explicitly programmed. ML algorithms can identify patterns, make predictions, and improve their performance over time. This is achieved by training models on large datasets, allowing them to generalize and adapt to new situations.",
    "**Deep Learning (DL)** is a specialized form of ML that utilizes artificial neural networks with multiple layers. These networks are designed to mimic the structure and function of the human brain, enabling them to learn complex patterns from vast amounts of data. DL has revolutionized various fields, including image recognition, natural language processing, and speech synthesis.",
    "**Cloud Computing** refers to the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the internet (“the cloud”). Cloud providers such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform offer a wide range of services that can be accessed on demand, allowing businesses to scale their resources and pay only for what they use.",
    "**Blockchain Technology** is a distributed ledger that securely records transactions across multiple computers. It is characterized by its immutability, transparency, and decentralization, making it ideal for applications such as cryptocurrency, supply chain management, and digital identity verification. Blockchain technology has the potential to revolutionize various industries by enhancing security, trust, and efficiency."
]})

#print(tech_dataframe['technologies'])
print(tech_dataframe);

#Add new Column which is (len) and add length of each character in the string.
tech_dataframe['len'] = tech_dataframe['technologies'].apply(len);
#print(tech_dataframe)

#count the word from string
tech_dataframe['word_count'] = tech_dataframe['technologies'].apply(lambda word : len(word.split()));
print(tech_dataframe)