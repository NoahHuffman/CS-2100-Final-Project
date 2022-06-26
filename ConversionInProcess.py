from tkinter import *
from PIL import Image,ImageTk
from Currency import Currency

expression = ''
#Button Functions

infile = open("Exchrate.txt")
inRates = infile.readlines()
infile.close()
exchRates = {}
moneySymbol = {}
leftOrRight = {}
commaOrDecimal = {}
for i in inRates:
    tempItem = i.rstrip().split(',')
    exchRates[tempItem[0]] = tempItem[4]
    moneySymbol[tempItem[0]] = tempItem[1]
    leftOrRight[tempItem[0]] = tempItem[2]
    commaOrDecimal[tempItem[0]] = tempItem[3]

def CurrencyConversion(origNum, origCountry, convCountry):
    if origNum >= 0:
        convNum = (origNum / eval(exchRates[origCountry])) * eval(exchRates[convCountry])
        return convNum



def buttonSequence(num):
    pressNum(num)
    record()
    



def getText():
    return entName.get()

def updateEntry():
    try:
        entrySub.config(text="${:,.2f}".format(float(entName.get())))
    except: 
        entrySub.config(text = "$0.00")


#Formats the amount and displays it in the "result" widget
def record():
    getText()
    content=str(entName.get())
    selectedFrom = str(countries[countryFrom.curselection()[0]])
    selectedTo = str(countries[countryTo.curselection()[0]])
    symbol = moneySymbol[selectedTo]
    whichSide = leftOrRight[selectedTo]
    dotComma = commaOrDecimal[selectedTo]
    try:
        content=float(content)
        content = CurrencyConversion(content, selectedFrom, selectedTo)        
        if whichSide == "right":
            if dotComma == "decimal":
                content="{0:,.2f}{1:s}".format(content,symbol).replace(",","w").replace(".",",").replace("w",".")
                result["text"]=content
            elif dotComma == "comma":
                content="{0:,.2f}{1:s}".format(content,symbol)
                result["text"]=content 
        elif whichSide == "left":
            if dotComma == "decimal":
                content="{0:s}{1:,.2f}".format(symbol,content).replace(",","w").replace(".",",").replace("w",".")
                result["text"]=content
            elif dotComma == "comma":
                content="{0:s}{1:,.2f}".format(symbol,content)
                result["text"]=content       
    except Exception:
        print('Error')
    

def record2(event):
    content=entName.get()
    selectedFrom = str(countries[countryFrom.curselection()[0]])
    selectedTo = str(countries[countryTo.curselection()[0]])
    symbol = moneySymbol[selectedTo]
    whichSide = leftOrRight[selectedTo]
    dotComma = commaOrDecimal[selectedTo]
    try:
        content=float(content)
        content = CurrencyConversion(content, selectedFrom, selectedTo)        
        if whichSide == "right":
            if dotComma == "decimal":
                content="{0:,.2f}{1:s}".format(content,symbol).replace(",","w").replace(".",",").replace("w",".")
                result["text"]=content
            elif dotComma == "comma":
                content="{0:,.2f}{1:s}".format(content,symbol)
                result["text"]=content 
        elif whichSide == "left":
            if dotComma == "decimal":
                content="{0:s}{1:,.2f}".format(symbol,content).replace(",","w").replace(".",",").replace("w",".")
                result["text"]=content
            elif dotComma == "comma":
                content="{0:s}{1:,.2f}".format(symbol,content)
                result["text"]=content       
    except Exception:
        print('Error')





def pressNum(num): 
    global expression
    expression = expression+str(num)
    equation.set(expression)

    
def clear():
    global expression
    expression = ''
    equation.set(expression)
    

def selectionSequence(event):
    changeCountryFrom(event)
    record()



def changeCountryFrom(event):
        ################FLAG
        flagFile = str(countries[countryFrom.curselection()[0]])
        flag = ("%s.jpg" % flagFile)        
        imgfrom=Image.open(flag)
      #  imgfrom.resize((300,333),Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(imgfrom)
        imgLblfrom = Label(window,image=render1)
        imgLblfrom.grid(row=3,column=2,padx=10,sticky=W)

        eq = entName.get()
        eqFormatted = "{0:s}{1:,.2f}".format('$',float(eq))
        equationSub.set(eqFormatted)
        window.mainloop()
        ################FLAG
def changeCountryTo(event):
        ################FLAG
        flagFile = str(countries[countryTo.curselection()[0]])
        flag = ("%s.jpg" % flagFile)        
        imgto=Image.open(flag)
        render2 = ImageTk.PhotoImage(imgto)
        imgLblto = Label(window,image=render2)
        imgLblto.grid(row=3,column=5,padx=5,sticky=W)
        window.mainloop()
        ################FLAG

def help():
    frame = Tk()
    frame.title("Help Window")
    frame.geometry('325x200')
    mssgOne = Label(frame,text="1. Select a country to convert from.",font="Calibri, 14")
    mssgOne.grid(row=0,column=0,pady=7,sticky=W)
    mssgTwo = Label(frame,text='2. Select a country to convert to',font="Calibri, 14")
    mssgTwo.grid(row=1,column=0,pady=7,sticky=W)
    mssg3 = Label(frame,text="3. Enter an amount",font="Calibri, 14")
    mssg3.grid(row=2,column=0,pady=7,sticky=W)
    mssg4 = Label(frame,text="4. Press 'Record'",font="Calibri, 14")
    mssg4.grid(row=3,column=0,pady=7,sticky=W)
    frame.mainloop()



infile = open("Exchrate.txt")
countryDict = {}
countries = []
for line in infile:
    info = line.rstrip().split(',')
    currency = Currency(info[1],info[2]=="left",info[3]=="comma",float(info[4]))
    countryDict[info[0]] = currency
infile.close()
for c in countryDict.keys():
    countries.append(c)


window = Tk()
window.title("Currency Converter")

window.geometry('665x560')
window.iconbitmap('Conversion.ico')
bg = (PhotoImage(file = "Anotherbackground.png"))
bg2 =(PhotoImage(file='background2.png'))

label1 =Label(window,image=bg)
label1.place(x=0,y=0)


titleTop = Label(window,bg="salmon")
titleBot = Label(window,bg="salmon")
converMssg1 = Label(window,text="    Convert from     ")
converMss2 = Label(window,text= "       Convert to        ")
result = Label(window,text="$0.00")


titleTop.grid(row=0,column=0,columnspan=7,sticky=EW)
titleBot.grid(row=6,column=0,columnspan=7,sticky=EW)
converMssg1.grid(row=2,column=1,padx=10,pady=10,sticky=W)
converMss2.grid(row=2,column=4,padx=10,pady=10,sticky=W)
result.grid(row=2,column=5,padx=10,pady=5,sticky=EW)


buttonFrame = Frame(window)
background_frame = Label(buttonFrame)#,image=bg2)
background_frame.place(x=0,y=0)
buttonFrame.grid(row=5,column=0,columnspan=6,padx=100,pady=65)



#Flag images -- setting default
imgfrom = Image.open("america.jpg")
render1 = ImageTk.PhotoImage(imgfrom)
imgto = Image.open("america.jpg")
render2 = ImageTk.PhotoImage(imgto)
imgLblfrom = Label(window,image=render1)
imgLblto = Label(window,image=render2)
imgLblfrom.grid(row=3,column=2,padx=10,sticky=W)
imgLblto.grid(row=3,column=5,padx=5,sticky=W)



equation = StringVar()

#Entrybox for Buttons
conOfentNum = StringVar(window, value = equation)
entName = Entry(window, textvariable=equation)
entrySub = Label(window, textvariable=equation)
entrySub.grid(row=2,column=2,sticky=EW)
entName.grid(row=1,column=1)
#entName.bind("<Key>",lambda v: window.after(10,updateEntry))
#entName.focus_set()


btn1 = Button(buttonFrame,text="1",width=4,bg='silver',font=('Calibri 18'),command=lambda: buttonSequence(1))
btn1.grid(row=0,column=0,padx=10,pady=5)
btn2 = Button(buttonFrame,text="2",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence(2))
btn2.grid(row=0,column=1,padx=10,pady=5)
btn3 = Button(buttonFrame,text="3",width=4,bg='silver',font=('Calibri 18'),command= lambda:buttonSequence(3))
btn3.grid(row=0,column=2,padx=10,pady=5)
btn4 = Button(buttonFrame,text="4",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence(4))
btn4.grid(row=1,column=0,padx=10,pady=5)
btn5 = Button(buttonFrame,text="5",width=4,bg='silver',font=('Calibri 18'),command= lambda:buttonSequence(5))
btn5.grid(row=1,column=1,padx=10,pady=5)
btn6 = Button(buttonFrame,text="6",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence(6))
btn6.grid(row=1,column=2,padx=10,pady=5)

btn7 = Button(buttonFrame,text="7",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence(7))
btn7.grid(row=3,column=0,padx=10,pady=5)
btn8 = Button(buttonFrame,text="8",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence(8))
btn8.grid(row=3,column=1,padx=10,pady=5)
btn9 = Button(buttonFrame,text="9",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence(9))
btn9.grid(row=3,column=2,padx=10,pady=5)
btn0 = Button(buttonFrame,text="0",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence(0))
btn0.grid(row=1,column=3,padx=10,pady=5)
btndot = Button(buttonFrame,text=".",width=4,bg='silver',font=('Calibri 18'),command=lambda:buttonSequence('.'))
btndot.grid(row=1,column=4,padx=10,pady=5)
btnClear = Button(buttonFrame,text="C",width=4,bg='silver',font=('Calibri 18'),command=lambda:clear())
btnClear.grid(row=1,column=5,padx=10,pady=5)


#Record button
btn_record = Button(buttonFrame,text="Record",width=16,bg='red',font=('Calibri 18'),command=lambda:record())
btn_record.grid(row=0,column=3,columnspan=3)

#Help button
btn_help = Button(buttonFrame,text="Help", width=16,bg = 'silver', font=('Calibri 18'),command=lambda: help())
btn_help.grid(row=3, column=3, columnspan=3)

#ListBox Left Side
conOfCountryFrom = StringVar()
countryFrom = Listbox(window,exportselection=0,listvariable=conOfCountryFrom)    
countryFrom.grid(row=3,column=1,sticky=W)
conOfCountryFrom.set(tuple(countries))
countryFrom.bind("<<ListboxSelect>>", selectionSequence)

#Listboxt Right Side
conOfCountryTo = StringVar()
countryTo =Listbox(window,exportselection=0,listvariable=conOfCountryTo)
countryTo.grid(row=3,column=4,sticky=W,columnspan=1)
conOfCountryTo.set(tuple(countries))
countryTo.bind('<<ListboxSelect>>', selectionSequence)

#ScrollWheels
scrollLS = Scrollbar(window,orient=VERTICAL)
scrollLS.grid(row=3,column=0,sticky=NS)
scrollLS["command"] = countryFrom.yview

scrollRS = Scrollbar(window,orient=VERTICAL)
scrollRS.grid(row=3,column=3,sticky=NS)
scrollRS['command']= countryTo.yview

countryFrom.selection_set(first=0)
countryTo.selection_set(first = 0)
window.mainloop()