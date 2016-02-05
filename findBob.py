s='obobobobogjgjbbobbboboobbobobjogjbob'
count=0
x=s.find('bob')
if(x!=-1):
    while True:
        x=s.find('bob',x+2,len(s))
        count+=1
        if(x==-1):
            break

print('Number of times bob occurs is: ' + str(count))