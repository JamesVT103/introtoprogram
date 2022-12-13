from tkinter import *
from tkinter import ttk
import currency, requests, json

app = Tk()
app.title("ExChange Rate")

# get api
def getData(url):
    response_API = requests.get(url)
    data = json.loads(response_API.text)["conversion_rates"]
    
    return data

# input
money = StringVar()
Label(text = "Amount", padx = 10, font = 100).grid(row = 0, sticky = W)
mainApp = ttk.Entry(width=30, font=30, textvariable=money)
mainApp.grid(row = 0, column = 1)

choice1 = StringVar(value = "Your currency")
Label(text = "Your currency", padx = 10, font = 30).grid(row = 1, sticky = W)
combo = ttk.Combobox(width = 30, font = 30, textvariable = choice1)
combo["values"] = currency.CURRENCY
combo.grid(row = 1, column = 1)

# select currency
choice = StringVar(value = "Please choose currecy")
Label(text = "Choose currency", padx = 10, font = 30).grid(row = 2, sticky = W)
combo = ttk.Combobox(width = 30, font = 30, textvariable = choice)
combo["values"] = currency.CURRENCY
combo.grid(row = 2, column = 1)

# output
Label(text=f"Rate", padx = 10, font = 30).grid(row = 3, sticky = W)
mainApp2=Entry(font = 30, width = 30)
mainApp2.grid(row = 3, column = 1)

# calculate the money
def calculate():
    amount = money.get()
    curr = choice.get()
    initCur = choice1.get()
    print(amount, initCur, curr)
    mainApp2.delete(0, END)
    realRate = float(getData(currency.API)[curr]) / float(getData(currency.API)[initCur])
    result = ((float(amount) * realRate), curr)
    mainApp2.insert(0, result)

# delete 
def delete():
    mainApp.delete(0, END)
    mainApp2.delete(0, END)

# show and clear
Button(text="Exchange", font = 30, width = 15, command = calculate).grid(row = 4, column = 1, sticky = W)
Button(text="Clear", font = 30, width = 15, command = delete).grid(row = 4, column = 1, sticky = E)

app.mainloop() 

