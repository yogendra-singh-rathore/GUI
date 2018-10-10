from tkinter import *
import backend

def get_selected_row(event):
    global seleted_tuple
    index=list1.curselection() [0]
    seleted_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,seleted_tuple[1])
    e2.delete(0,END)
    e2.insert(END,seleted_tuple[2])
    e3.delete(0,END)
    e3.insert(END,seleted_tuple[3])
    e4.delete(0,END)
    e4.insert(END,seleted_tuple[4])
    e5.delete(0,END)
    e5.insert(END,seleted_tuple[5])
    e6.delete(0,END)
    e6.insert(END,seleted_tuple[6])

def view_command():
    list1.delete(0,END)
    for row in  backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(order_date.get(),Customer_name.get(),customer_details.get(),order_name.get(),payment_method.get(),payment_status.get()):
        list1.insert(END,row)
def add_command():
    backend.insert(order_date.get(),Customer_name.get(),customer_details.get(),order_name.get(),payment_method.get(),payment_status.get())
    list1.delete(0,END)
    list1.insert(END,(order_date.get(),Customer_name.get(),customer_details.get(),order_name.get(),payment_method.get(),payment_status.get()))
def delete_command():
    backend.delete(seleted_tuple[0])
def update_command():
    backend.update(seleted_tuple[0],order_date.get(),Customer_name.get(),customer_details.get(),order_name.get(),payment_method.get(),payment_status.get())


window=Tk()
window.wm_title('Project Data')

l1=Label(window,text="Order Date")
l1.grid(row=0,column=0)

l2=Label(window,text="Customer Name")
l2.grid(row=0,column=2)

l3=Label(window,text="Customer Details")
l3.grid(row=0,column=4)

l4=Label(window,text="Order Name")
l4.grid(row=1,column=0)

l5=Label(window,text="Payment Method")
l5.grid(row=1,column=2)

l6=Label(window,text="Payment Status")
l6.grid(row=1,column=4)

order_date=StringVar()
e1=Entry(window,textvariable=order_date)
e1.grid(row=0,column=1)

Customer_name=StringVar()
e2=Entry(window,textvariable=Customer_name)
e2.grid(row=0,column=3)

customer_details=StringVar()
e3=Entry(window,textvariable=customer_details)
e3.grid(row=0,column=5)

order_name=StringVar()
e4=Entry(window,textvariable=order_name)
e4.grid(row=1,column=1)

payment_method=StringVar()
e5=Entry(window,textvariable=payment_method)
e5.grid(row=1,column=3)

payment_status=StringVar()
e6=Entry(window,textvariable=payment_status)
e6.grid(row=1,column=5)

list1=Listbox(window, height=20,width=100)
list1.grid(row=2,column=0,rowspan=6,columnspan=4)

sb1=Scrollbar(window)
sb1.grid(row=2,column=4,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=15,command=view_command)
b1.grid(row=2,column=5)

b2=Button(window,text="Search Entry", width=15,command=search_command)
b2.grid(row=3,column=5)

b3=Button(window,text="Add Entry", width=15,command=add_command)
b3.grid(row=4,column=5)

b4=Button(window,text="Update Entry", width=15,command=update_command)
b4.grid(row=5,column=5)

b5=Button(window,text="Delete Entry", width=15,command=delete_command)
b5.grid(row=6,column=5)

b6=Button(window,text="Close", width=15,command=window.destroy)
b6.grid(row=7,column=5)

window.mainloop()
