import requests
import random
from  tkinter import * 
from tkinter import messagebox

URL='http://127.0.0.1:5000'  #TO CONNECT SERVER 
r = requests.get(URL+"/api/qbank")
fulldata =r.json()['data']
lastindex=fulldata[-1]['index']


def addtodata():
    #request
    newdata={'index': lastindex+1,'question': question.get("1.0",'end-1c'), 'answer': answer.get()
    , 'mark':mark.get()}
    headers=headers = {"Content-type": "application/json"} #needed
    requests.post(URL+'/api/qbank',json=newdata,headers=headers)
    #clear
    question.delete('1.0', END)
    answer.delete(0, 'end')
    mark.delete(0, 'end')
    messagebox.showinfo("ok", "new question added to database")
    

#gui
window = Tk()
window.rowconfigure([0,1,2,3], minsize=50, weight=1)
window.columnconfigure([0, 1, 2,3], minsize=50, weight=1)
window.title("add new question to database:")
window.geometry("800x600")
#gui elements
question= Text(window, height = 10, width = 40 )
question.grid(row=0, column=1)
l1 = Label( window, text='question',font=("Arial", 15))
l1.grid(row=0, column=0)
answer= Entry(window,width=30 )
answer.grid(row=1, column=1)
l2 = Label( window, text='answer',font=("Arial", 15))
l2.grid(row=1, column=0)
mark= Entry(window,width=30 )
mark.grid(row=2, column=1)
l3 = Label( window, text='mark',font=("Arial", 15))
l3.grid(row=2, column=0)
add_Button= Button(window,width=30,height=5,bg="gray",fg="white", text ="add", command = addtodata)
add_Button.grid(row=3, column=2)
window.mainloop()
