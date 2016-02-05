balance = 3926
annualInterestRate = 0.2

monthInt = annualInterestRate/12
lowPay = 10
totalPaid=0
def payment(balance,lowPay):
    i=1
    while (i<=12):
        remPayment = balance-lowPay
        balance = remPayment + (remPayment * (monthInt))
        i+=1
    return balance

testBalance=balance
while (testBalance>0):
    testBalance=payment(balance,lowPay)
    if(testBalance>0):
        lowPay+=10
        testBalance=balance
        testBalance=payment(balance,lowPay)

print('Lowest Payment: '+str(round(lowPay,2)))