CP = float(input('enter the cost of product:'))
CGST = float(input('enter tax % imposed by centre,i.e. CGST:'))
SGST = float(input('enter tax % imposed by state, i.e. SGST;'))
total = 0
amount_CGST = ((CGST/100)*CP)
amount_SGST = ((SGST/100)*CP)
total = CP + amount_CGST + amount_SGST
print('total cost of product: rs ',total)
