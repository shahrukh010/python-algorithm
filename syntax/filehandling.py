
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

import requests

api_url = "https://api.openai.com/v1/chat/completions";
access_token = "Bearer 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"

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "provide me opensource api for pyton"
        }
    ],
    "temperature": 1,
    "max_tokens": 1000
}

response = requests.post(api_url, json=data, headers=headers)

if response.status_code == 200:
    pass
#    print(response.json())
else:
    print("Error:", response.status_code)


result = response.json();
outpu_data = result['choices'][0]['message']['content']
#print(outpu_data);

try:
  gpt_data = open('blog.txt','w')
  gpt_data.write(outpu_data+"\n");
except FileNotFoundError as f_error:
  print(f_error);
finally:
  gpt_data.close()


