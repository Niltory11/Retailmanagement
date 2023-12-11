from tkinter import *
win=Tk()
win.title('Retail Management')

win.config(bg='gray')
win.geometry('1300x720+0+0')

topFrame=Frame(win,bd=9,relief=GROOVE)
topFrame.pack(side=TOP)
topFrame.pack(fill=X)

#variable list
name = StringVar()
contact = StringVar()
bill_no = StringVar()

veg_bean = IntVar()
veg_pepper = IntVar()
veg_potato = IntVar()
veg_tomato = IntVar()

fish_goldfish = IntVar()
fish_illisha = IntVar()
fish_whale = IntVar()
fish_catfish = IntVar()

fruits_apple = IntVar()
fruits_orange = IntVar()
fruits_mango = IntVar()
fruits_litchies = IntVar()

drink_sprite = IntVar()
drink_pepsi = IntVar()
drink_cocacola = IntVar()
drink_drinko = IntVar()

bill_list = list()




#body_2
LabelTittle= Label(topFrame,text="Retail Management System",font=('arial',30,'bold'),bg='gray')
LabelTittle.grid(row=0,column=0)
LabelTittle.pack(fill=X)

#body-2 discription=it shows top level freme

#body-3
customer_info=LabelFrame(win,text='Customer Details',font=('times new roman',15,'italic'),bg ='gray',bd=8,relief="groove")
customer_info.pack(fill=X)
#body-4

nameLable=Label(customer_info,text='Customer Name',font=('arial',12,'bold'),bg='gray',padx=20)
nameLable.grid(row=0,column=1,)

nameEntry=Entry(customer_info,bd=7,textvariable=name)
nameEntry.grid(row=0,column=2,padx=8)
#body-5
phoneLable=Label(customer_info,text='Phone Number',font=('arial',12,'bold'),bg='gray',padx=20)
phoneLable.grid(row=0,column=3)

phoneEntry=Entry(customer_info,bd=7,textvariable=contact)
phoneEntry.grid(row=0,column=4,padx=8)
#body-5
IDLable=Label(customer_info,text='Bill Number',font=('arial',12,'bold'),bg='gray',padx=20)
IDLable.grid(row=0,column=5,padx=8)

IDEntry=Entry(customer_info,bd=7,textvariable=bill_no)
IDEntry.grid(row=0,column=6,padx=8)

#body-6
searchLable=Button(customer_info,text='SEARCH',font=('arial',12,'bold'),bg='white',padx=5,bd=4,width=8,height=1)
searchLable.grid(row=0,column=8,padx=18,pady=8)
#body-7
productFrame=Frame(win)
productFrame.pack()


#body-8
FruitsFrame=LabelFrame(productFrame,text='Vegetable',font=('times new roman',12,'italic'),bg='gray',padx=20,bd=8,pady=15)
FruitsFrame.grid(row=0,column=0)


FruitsLabel=Label(FruitsFrame,text='Bean',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=0,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=veg_bean)
fruitsEntry.grid(row=0,column=1,padx=8)

#body-18
FruitsLabel=Label(FruitsFrame,text='Tomato',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=1,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=veg_tomato)
fruitsEntry.grid(row=1,column=1,padx=8)

#body-19
FruitsLabel=Label(FruitsFrame,text='Pepper',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=2,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=veg_pepper)
fruitsEntry.grid(row=2,column=1,padx=8)

#body-20
FruitsLabel=Label(FruitsFrame,text='Potato',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=3,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=veg_potato)
fruitsEntry.grid(row=3,column=1,padx=8)
#body-pass
FishFrame=LabelFrame(productFrame,text='Fish',font=('times new roman',12,'italic'),bg='gray',padx=20,bd=8,pady=15)
FishFrame.grid(row=0,column=1)

FishLabel=Label(FishFrame,text='Gold fish',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FishLabel.grid(row=0,column=0)
FishEntry=Entry(FishFrame,bd=7,textvariable=fish_goldfish,)
FishEntry.grid(row=0,column=1,padx=8)

FishLabel=Label(FishFrame,text='Ilisha ',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FishLabel.grid(row=1,column=0)
FishEntry=Entry(FishFrame,bd=7,textvariable=fish_illisha,)
FishEntry.grid(row=1,column=1,padx=8)

FishLabel=Label(FishFrame,text='Whale',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FishLabel.grid(row=2,column=0)
FishEntry=Entry(FishFrame,bd=7,textvariable=fish_whale,)
FishEntry.grid(row=2,column=1,padx=8)

FishLabel=Label(FishFrame,text='Cat fish',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FishLabel.grid(row=3,column=0)
FishEntry=Entry(FishFrame,bd=7,textvariable=fish_catfish,)
FishEntry.grid(row=3,column=1,padx=8)

#body-21
DrinksFrame=LabelFrame(productFrame,text='Drinks',font=('times new roman',12,'italic'),bg='gray',padx=20,bd=8,pady=15)
DrinksFrame.grid(row=1,column=1)

DrinksLabel=Label(DrinksFrame,text='Sprite',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=1,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_sprite)
DrinksEntry.grid(row=1,column=1,padx=8)

#body-22
DrinksLabel=Label(DrinksFrame,text='Pepsi',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=7,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_pepsi)
DrinksEntry.grid(row=7,column=1,padx=8)

#body-23
DrinksLabel=Label(DrinksFrame,text='SevenUP',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=8,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_cocacola)
DrinksEntry.grid(row=8,column=1,padx=8)

#body-24
DrinksLabel=Label(DrinksFrame,text='Drinko',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=9,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_drinko)
DrinksEntry.grid(row=9,column=1,padx=8)

#body-17
FruitsFrame=LabelFrame(productFrame,text='Fruits',font=('times new roman',12,'italic'),bg='gray',padx=20,bd=8,pady=15)
FruitsFrame.grid(row=1,column=0)


FruitsLabel=Label(FruitsFrame,text='Apple',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=1,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=fruits_apple)
fruitsEntry.grid(row=1,column=1,padx=8)

#body-18
FruitsLabel=Label(FruitsFrame,text='Orange',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=7,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=fruits_orange)
fruitsEntry.grid(row=7,column=1,padx=8)

#body-19
FruitsLabel=Label(FruitsFrame,text='Mango',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=8,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=fruits_mango)
fruitsEntry.grid(row=8,column=1,padx=8)

#body-20
FruitsLabel=Label(FruitsFrame,text='Lychee',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
FruitsLabel.grid(row=9,column=0)

fruitsEntry=Entry(FruitsFrame,bd=7,textvariable=fruits_litchies)
fruitsEntry.grid(row=9,column=1,padx=8)

#body-21
DrinksFrame=LabelFrame(productFrame,text='Drinks',font=('times new roman',12,'italic'),bg='gray',padx=20,bd=8,pady=15)
DrinksFrame.grid(row=1,column=1)

DrinksLabel=Label(DrinksFrame,text='Sprite',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=1,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_sprite)
DrinksEntry.grid(row=1,column=1,padx=8)

#body-22
DrinksLabel=Label(DrinksFrame,text='Pepsi',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=7,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_pepsi)
DrinksEntry.grid(row=7,column=1,padx=8)

#body-23
DrinksLabel=Label(DrinksFrame,text='SevenUP',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=8,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_cocacola)
DrinksEntry.grid(row=8,column=1,padx=8)

#body-24
DrinksLabel=Label(DrinksFrame,text='Drinko',font=('arial',12,'bold'),bg='gray',padx=20,pady=15)
DrinksLabel.grid(row=9,column=0)

DrinksEntry=Entry(DrinksFrame,bd=7,textvariable=drink_drinko)
DrinksEntry.grid(row=9,column=1,padx=8)

#body-25
billFrame=Frame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label (billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,height=12,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)
#dody-25 = it creats bill fream

# functions



def clear():
    textarea.delete(1.0,END)
    veg_pepper.set(0)
    veg_potato.set(0)
    veg_bean.set(0)
    veg_tomato.set(0)
    fish_catfish.set(0)
    fish_goldfish.set(0)
    fish_illisha.set(0)
    fish_whale.set(0)
    fruits_apple.set(0)
    fruits_litchies.set(0)
    fruits_mango.set(0)
    fruits_orange.set(0)
    drink_cocacola.set(0)
    drink_drinko.set(0)
    drink_pepsi.set(0)
    drink_sprite.set(0)
    name.set("")
    contact.set("")
    bill_no.set("")
    bill_list.clear()



def create():
    top = (f"  Name: {name.get()}\n  Contact: {contact.get()}\t\t\t\tInvoice: {bill_no.get()}\n")
    textarea.insert(1.0,top)
    bill_list.append(f"=======================================================\n  Item\t\t\t Qty\t\tPrice\n=======================================================\n")

    if veg_tomato.get() > 0:
        bill_list.append(f"  Tomato".ljust(25)+f"{veg_tomato.get()} pc\t\t\t\t\t{veg_tomato.get()*80}tk\n")
    if veg_potato.get() > 0:
        bill_list.append(f"  Potato".ljust(25)+f"{veg_potato.get()} pc\t\t\t\t\t{veg_potato.get()*70}tk\n")
    if veg_bean.get() > 0:
        bill_list.append(f"  Bean".ljust(25)+f"{veg_bean.get()} pc\t\t\t\t\t{veg_bean.get()*40}tk\n")
    if veg_pepper.get() > 0:
        bill_list.append(f"  Paper".ljust(25)+f"{veg_pepper.get()} pc\t\t\t\t\t{veg_pepper.get()*150}tk\n")

    if fish_goldfish.get() > 0:
        bill_list.append(f"  Goldfish".ljust(25)+f"{fish_goldfish.get()} pc\t\t\t\t\t{fish_goldfish.get()*800}tk\n")
    if fish_whale.get() > 0:
        bill_list.append(f"  Whale".ljust(25)+f"{fish_whale.get()} pc\t\t\t\t\t{fish_whale.get()*100000}tk\n")
    if fish_catfish.get() > 0:
        bill_list.append(f"  Catfish".ljust(25)+f"{fish_catfish.get()} pc\t\t\t\t\t{fish_catfish.get()*1800}tk\n")
    if fish_illisha.get() > 0:
        bill_list.append(f"  Illisha".ljust(25)+f"{fish_illisha.get()} pc\t\t\t\t\t{fish_illisha.get()*2000}tk\n")

    if fruits_apple.get() > 0:
        bill_list.append(f"  Apple".ljust(25)+f"{fruits_apple.get()} pc\t\t\t\t\t{fruits_apple.get()*100}tk\n")
    if fruits_orange.get() > 0:
        bill_list.append(f"  Orange".ljust(25)+f"{fruits_orange.get()} pc\t\t\t\t\t{fruits_orange.get()*60}tk\n")
    if fruits_mango.get() > 0:
        bill_list.append(f"  Mango".ljust(25)+f"{fruits_mango.get()} pc\t\t\t\t\t{fruits_mango.get()*120}tk\n")
    if fruits_litchies.get() > 0:
        bill_list.append(f"  Litchie".ljust(25)+f"{fruits_litchies.get()} pc\t\t\t\t\t{fruits_litchies.get()*280}tk\n")

    if drink_sprite.get() > 0:
        bill_list.append(f"  Sprite".ljust(25)+f"{drink_sprite.get()} pc\t\t\t\t\t{drink_sprite.get()*70}tk\n")
    if drink_pepsi.get() > 0:
        bill_list.append(f"  Pepsi".ljust(25)+f"{drink_pepsi.get()} pc\t\t\t\t\t{drink_pepsi.get()*70}tk\n")
    if drink_cocacola.get() > 0:
        bill_list.append(f"  CocaCola".ljust(25)+f"{drink_cocacola.get()} pc\t\t\t\t\t{drink_cocacola.get()*80}tk\n")
    if drink_drinko.get() > 0:
        bill_list.append(f"  Drinko".ljust(25)+f"{drink_drinko.get()} pc\t\t\t\t\t{drink_drinko.get()*40}tk\n")

    for text in bill_list:
        textarea.insert(END,text)



button_clear = Button(productFrame,text="Clear",command=clear,bg='red',padx=15,pady=10).grid(row=1,column=2,padx=2)
button_clear = Button(productFrame,text="Email",command=clear,padx=15,pady=10).grid(row=1,column=3,padx=2)
button_create = Button(productFrame,text="Create",command=create,bg='green',padx=15,pady=10).grid(row=1,column=4,padx=2)
win.mainloop()
