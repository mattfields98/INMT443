with open("Version2Code.txt","r") as mytaxfile:
     data = mytaxfile.read()
taxlist = data.splitlines()

FilingStatus = taxlist[0]
TaxableIncomeBD = taxlist[1]


Taxratedic = {
    "Single": float(12200.00),
    "Married Filing Jointly": float(24400.00),
    "Head of Household": float(18350.00)
    }

if FilingStatus == "single":
     FilingStatusCheck = True
elif FilingStatus == "married filing jointly":
     FilingStatusCheck = True
elif FilingStatus == "head of household":
     FilingStatusCheck = True
else:
    print("Please enter a correct filing status.")
    FilingStatusCheck = False
    import sys
    sys.exit()

TIBD = float(TaxableIncomeBD)
TIBD = round(TIBD,2)


if FilingStatus == "single":
    SD = Taxratedic.get("Single")
elif FilingStatus == "married filing jointly":
    SD = Taxratedic.get("Married Filing Jointly")      
else:
     SD = Taxratedic.get("Head of Household")

TIAD = TIBD - SD


i = 1
while FilingStatus == "single" and i < 2:
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
     i += 1

while FilingStatus == "married filing jointly" and i < 2:
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
     i += 1

while FilingStatus == "head of household" and i < 2:
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
     i += 1     

TaxesDue = TaxRate * TIAD
print("Your standard deduction amount is: "+"${:,.2f}".format(SD)+ " and your taxes due are "+"${:,.2f}".format(TaxesDue))
