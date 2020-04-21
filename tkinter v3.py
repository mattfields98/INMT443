from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk() 
textBox1=Text(root, height=2, width=30)
textBox1.insert(END,"Filing Status")
textBox1.pack() 
textBox2=Text(root, height=2, width=30)
textBox2.insert(END,"Taxable Income")
textBox2.pack()
ttk.Label(root, text = "Please enter your filing status (Single, Married Filing Jointly, or Head of Household)").pack()
ttk.Label(root, text = "Please enter your taxable income for the year.").pack()
ttk.Button(root, text = "Enter", command = lambda:callback()).pack()        
ttk.Button(root, text="Exit", command=quit).pack()

Taxratedic = {
    "Single": float(12200.00),
    "Married Filing Jointly": float(24400.00),
    "Head of Household": float(18350.00)
    }

def callback():
    UserFilingStatus=textBox1.get("1.0","end-1c")
    FilingStatus=str.lower(UserFilingStatus)
    TaxableIncomeBD=textBox2.get("1.0","end-1c")
    TIBD = verifyTIBD(TaxableIncomeBD)
    verifyFS(FilingStatus)
    SD = SDAmount(FilingStatus,Taxratedic)
    TIAD = CalculateTIAD(TIBD,SD)
    if FilingStatus == "head of household":
        TaxRate = CheckHOHRate(FilingStatus,TIAD)
    elif FilingStatus == "single":
        TaxRate = CheckSingleRate(FilingStatus,TIAD)
    else: TaxRate = CheckMFJRate(FilingStatus,TIAD)
    TaxesDue = CalcTaxesDue(TIAD, TaxRate)
    messagebox.showinfo("TaxesDue", "Your standard deduction amount is: "+"${:,.2f}".format(SD)+" and your taxes due are "+"${:,.2f}".format(TaxesDue))

def verifyFS(FilingStatus):
    if FilingStatus == "single":
     FilingStatusCheck = True
    elif FilingStatus == "married filing jointly":
     FilingStatusCheck = True
    elif FilingStatus == "head of household":
     FilingStatusCheck = True
    else:
     FilingStatusCheck = False
     messagebox.showinfo("Error message", "Please enter a correct filing status.")
     sys.exit()

def verifyTIBD(TaxableIncomeBD):
    if str.isnumeric(TaxableIncomeBD):
        TIBD = float(TaxableIncomeBD)
        TIBD = round(TIBD,2)
        return TIBD
    else:
        messagebox.showinfo("Error","Please enter a correct taxable income.")
        sys.exit()
        
def SDAmount(FilingStatus,Taxratedic):
    if FilingStatus == "single":
        SD = Taxratedic.get("Single")
    elif FilingStatus == "married filing jointly":
        SD = Taxratedic.get("Married Filing Jointly")
    else: 
        SD = Taxratedic.get("Head of Household")
    return SD

def CalculateTIAD(TIBD,SD):
    TIAD = TIBD - SD
    return round(TIAD,2)

def CheckSingleRate(FilingStatus,TIAD):
    while FilingStatus == "single":
     if TIAD <= 9700:
          TaxRate = .10
     elif TIAD <= 39475:
          TaxRate = .12
     elif TIAD <= 84200:
          TaxRate = .22
     elif TIAD <= 160725:
          TaxRate = .24
     elif TIAD <= 204100:
          TaxRate = .32
     elif TIAD <= 510300:
          TaxRate = .35
     else:
          TaxRate = .37
     return TaxRate

def CheckMFJRate(FilingStatus,TIAD):
    while FilingStatus == "married filing jointly":
     if TIAD <= 19400:
          TaxRate = .10
     elif TIAD <= 78950:
          TaxRate = .12
     elif TIAD <= 168400:
          TaxRate = .22
     elif TIAD <= 321450:
          TaxRate = .24
     elif TIAD <= 408200:
          TaxRate = .32
     elif TIAD <= 612350:
          TaxRate = .35
     else:
          TaxRate = .37
     return TaxRate
    
def CheckHOHRate(FilingStatus,TIAD):
    while FilingStatus == "head of household":
     if TIAD <= 13850:
          TaxRate = .10
     elif TIAD <= 52850:
          TaxRate = .12
     elif TIAD <= 84200:
          TaxRate = .22
     elif TIAD <= 160700:
          TaxRate = .24
     elif TIAD <= 204100:
          TaxRate = .32
     elif TIAD <= 510300:
          TaxRate = .35
     else:
          TaxRate = .37
    return TaxRate

def CalcTaxesDue(TIAD, TaxRate):
    TaxesDue = TaxRate * TIAD
    return TaxesDue

def quit():
    root.destroy()

root.mainloop

