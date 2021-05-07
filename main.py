import requests
import random
from  tkinter import * 
from tkinter import messagebox

URL='http://127.0.0.1:5000'  #TO CONNECT SERVER 
r = requests.get(URL+"/api/qbank")
#to start test
asked=[]
totalmark=0.0
fulldata =r.json()['data']
print(fulldata[-1]['index'])
for x in range(0):
    q=random.choice(fulldata)
    if q['index'] not in asked:
        asked.append(q['index'])
        print(q['question'])
        userinput=input('your answer:')
        answer=str(q['answer']).lower()
        if(userinput==answer):
            print('alright')
            totalmark+=q['mark']



#to add data
newdata={'index': 2,'question': 'fish ?', 'answer': True, 'mark': 7.0}
headers=headers = {"Content-type": "application/json"} #needed
#q=requests.post(URL+'/api/qbank',json=newdata,headers=headers)



def checkanswer():
    var.set('object has no attribute')
    #checck ans
    messagebox.showinfo("mark:", totalmark)


#gui
window = Tk()
var = StringVar()
window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
window.title("quiz")
window.geometry("800x600")
#gui elements
question = Label( window, textvariable=var,font=("Arial", 20))
question.grid(row=0, column=0)
answer_text= Text(window, height = 10, width = 84)
answer_text.grid(row=1, column=0)
send_Button= Button(window,width=30,height=5,bg="orange",fg="white", text ="answer", command = checkanswer)
send_Button.grid(row=2, column=0)

window.mainloop()