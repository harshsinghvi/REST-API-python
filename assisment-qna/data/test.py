import json
f=open('questions.json')

y = json.loads(f.read())
print(type(y))
print(y)
responses={}
responses['responses']={}

name=input(">> name: ")
responses['name']=name
for i in y:
    print(i,":  ",y[i]['que'])
    for j in range(len(y[i]['choices'])):
        print("         ",j,". ",y[i]['choices'][j])
    responce= input(">> YOUR CHOICE INT: ")
    responses['responses'][i]=responce





file=open('responses.json')
file_dict=json.loads(file.read())['responses']
file.close()

file_dict.append(responses)
print(type(file_dict))
print(file_dict)
# print(type(file_list))

f=open('responses.json','w')
f.write(json.dumps(file_dict))
# print(json.dumps(responses))
