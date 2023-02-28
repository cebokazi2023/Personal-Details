  
from tkinter import *  

#import tkinter.messagebox

#def validate():
    #FullName= Entry.get()
  #  Email= Entry.get()
   # ContactNumber= Entry.get()
   # Age= Entry.get()
   # Gender= vars.get()
   # Country = cv.get()
   # Language=vars2.get()
   # if (FullName=="" or Email=="" or ContactNumber=="" or Age=="" or Country== 'Select your country'or Language== 0 or Gender == 0):
        #tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty!")

   # else:
       # tkinter.messagebox.showinfo('Success Message',"Successfully registered!")

base = Tk()  
  
base.geometry("550x550") 

#base['bg'] = 'black'


base.title('Personal Details')  
   
lbl_0 = Label(base, text="Personal Details", width=20,font=("bold",20))  

lbl_0.place(x=90,y=60)  
lbl_1 =Label(base, text= "FullName", width=20,font=("bold",10))  
lbl_1.place(x=80,y=130)  
  
enter_1 = Entry(base)  
enter_1.place(x=240,y=130)  
  
lbl_3 = Label(base, text="Email", width=20,font=("bold",10))  
lbl_3.place(x=67,y=170)  
 
enter_3 = Entry(base)  
enter_3.place(x=240,y=180)  

lb4= Label(base, text="Contact Number", width=20,font=("bold",10))  
lb4.place(x=95, y=215)  

en4= Entry(base)  
en4.place(x=240, y=215)

labl_4 = Label(base, text="Age:",width=20,font=("bold", 10))  
labl_4.place(x=62,y=250)  
en4 = Entry(base)
en4.place(x=240, y=250)

lbl_4 = Label(base, text="Gender", width=20,font=("bold",10))  
lbl_4.place(x=67,y=275)  
  
vars = IntVar()  


Radiobutton(base, text="Male", padx= 5, variable= vars, value=1).place(x=240, y=275)  
Radiobutton(base, text="Female", padx= 20, variable= vars, value=2).place(x=295,y=275)  
  
lbl_5=Label(base, text ="Country", width=20,font=("bold",10))  
lbl_5.place(x=70,y=315)  
  
list_of_cntry=[ 'India' ,'Canada' ,'SA' ,'Germany' ,'UK']   
cv = StringVar()  
drplist = OptionMenu(base, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set('Select your Country')  
drplist.place(x=235, y=315)  
  
lbl_6=Label(base, text="Language", width=20,font=('bold',10))  
lbl_6.place(x=75,y=360)  
vars1=IntVar()  
 
Checkbutton(base, text="English", variable = vars1).place(x=235,y=360)  
vars2=IntVar()  

Checkbutton(base, text="German", variable=vars2).place(x=295, y=360)  

Button(base, text='Submit' , width=20, bg="black",fg='white').place(x=200,y=450)  

base.mainloop()  
