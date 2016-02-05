balance = 999999
annualInterestRate = 0.18

monthInt = annualInterestRate/12
low=balance/12
hi=(balance*((1+monthInt)**12))/12.0
epsilon=0.01
ans=(hi+low)/2

def payment(balance,lowPay):
    i=1
    while (i<=12):
        remPayment = balance-lowPay
        balance = remPayment + (remPayment * (monthInt))
        i+=1
    return balance

steps=0
testBalance=payment(balance,ans)

while (True):
    testBalance=balance
    testBalance=payment(balance,ans)
    if(testBalance>0):
        low=ans
    else:
        hi=ans
    ans=(hi+low)/2
    steps+=1
    if((abs(testBalance)<=epsilon)):
        break
    
print('Lowest Payment: '+str(round(ans,2)))