order=''

def item_order(order):
    x=0
    y=0
    z=0
    countH=0
    x=order.find('hamburger')
    if(x!=-1):
        while True:
            x=order.find('hamburger',x+9,len(order))
            countH+=1
            if(x==-1):
                break
    countW=0
    y=order.find('water')
    if(y!=-1):
        while True:
            y=order.find('water',y+5,len(order))
            countW+=1
            if(y==-1):
                break
    countS=0
    z=order.find('salad')
    if(z!=-1):
        while True:
            z=order.find('salad',z+5,len(order))
            countS+=1
            if(z==-1):
                break
    
    print('salad:' + str(countS) + ' hamburguer:' + str(countH) + ' water:' + str(countW))

item_order(order)