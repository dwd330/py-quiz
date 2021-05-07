import requests
import random
from  tkinter import * 
from tkinter import messagebox
from tkinter import simpledialog

URL='http://127.0.0.1:5000'  #TO CONNECT SERVER 
r = requests.get(URL+"/api/qbank")
#to start test
asked=[]
totalmark=0.0
fulldata =r.json()['data']
def newQ():
	while(True):
		q=random.choice(fulldata)
		if q['index'] not in asked:
			asked.append(q['index'])
			break
	return q

def newuser():
	username = simpledialog.askstring(title="new test",
								  prompt="What's your Name?:")
    
	if username :
		return username
		
	else:
		return 'new user'
		
		
def checkanswer():
		global q
		global totalmark
		answer=str(q['answer']).lower()
		useranswer=answer_text.get("1.0",'end-1c')
		if(useranswer==answer):
			totalmark+=q['mark']
		q=newQ()
		var.set(q['question'])
		answer_text.delete('1.0', END)


		
			


def finish():
	global totalmark
	global usrname
	messagebox.showinfo('result', usrname+' '+"mark:"+' '+str(totalmark))
	totalmark=0.0
	answer_text.delete('1.0', END)
	usrname=newuser()


#init q
q=newQ()

#gui
window = Tk()
var = StringVar()
var.set(q['question'])
window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
window.title("quiz")
window.geometry("1000x800")
#gui elements
question = Label( window, textvariable=var,font=("Arial", 15),wraplength=300)
question.grid(row=0, column=0)
answer_text= Text(window, height = 10, width = 84)
answer_text.grid(row=1, column=0)
answer_Button= Button(window,width=30,height=5,bg="orange",fg="white", text ="answer", command = checkanswer)
answer_Button.grid(row=2, column=0)
finish_Button= Button(window,width=30,height=5,bg="green",fg="white", text ="finish", command = finish)
finish_Button.grid(row=2, column=1)
usrname=newuser() #get user name
window.mainloop()