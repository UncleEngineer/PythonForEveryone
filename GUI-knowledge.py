from tkinter import * # import all function inside main package
from tkinter import ttk
import csv

def writecsv(data):
    # data = ['john',14,500]
    with open('knowledge.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # FW = File Writer
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมบันทึกความรู้ by Loong')
GUI.geometry('500x500')

L1 = ttk.Label(GUI,text='หัวข้อความรู้',font=('Angsana New',18))
L1.pack()


v_title = StringVar()

E1 = ttk.Entry(GUI,textvariable=v_title ,font=('Angsana New',20),width=50)
E1.pack()

L2 = ttk.Label(GUI,text='รายละเอียด',font=('Angsana New',18))
L2.pack()

T1 = Text(GUI,font=('Angsana New',18),height=8,width=56)
T1.pack()

def save():
    title = v_title.get()
    textbox = T1.get(1.0,"end-1c")
    print('-------')
    print(title)
    print('-------')
    print(textbox)
    print('-------')
    data = [title,textbox]
    writecsv(data)
    v_title.set('') #clear data after save
    T1.delete('1.0',END) # clear text box

B1 = ttk.Button(GUI,text='บันทึก',command=save)
B1.pack(pady=10,ipadx=20,ipady=10)

GUI.mainloop()