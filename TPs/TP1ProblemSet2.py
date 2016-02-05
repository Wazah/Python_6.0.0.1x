balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
i=1
totalPaid=0
while (i<=12):
    minPayment = balance*monthlyPaymentRate 
    totalPaid += minPayment
    remPayment = balance-minPayment
    balance = remPayment + (remPayment * (annualInterestRate/12))
    print("Month: "+str(i))
    print("Minimum monthly payment: "+str(round(minPayment,2)))
    print("Remaining balance: "+str(round(balance,2)))
    i+=1

print('Total paid: '+str(round(totalPaid,2)))
print('Remaining balance: '+str(round(balance,2)))