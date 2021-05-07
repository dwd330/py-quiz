import requests
import random

URL='http://127.0.0.1:5000'  #TO CONNECT SERVER 
r = requests.get(URL+"/api/qbank")
asked=[]
totalmark=0.0
fulldata =r.json()['data']
print(fulldata[-1]['index'])
for x in range(2):
    q=random.choice(fulldata)
    if q['index'] not in asked:
        asked.append(q['index'])
        print(q['question'])
        userinput=input('your answer:')
        answer=str(q['answer']).lower()
        if(userinput==answer):
            print('alright')
            totalmark+=q['mark']



print(asked)
print(totalmark)



newdata={'index': 2,'question': 'fish ?', 'answer': True, 'mark': 7.0}
headers=headers = {"Content-type": "application/json"} #needed
#q=requests.post(URL+'/api/qbank',json=newdata,headers=headers)
