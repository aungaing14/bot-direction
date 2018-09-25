n=0
mapp=['North', 'East', 'South' , 'West']
xy=[0,0]
L=(-1)
R=1
A=0


ipdirec = input('Input Direction : ')
num=len(ipdirec)

def loop_R(n):
    n=n+R

def loop_L(n):
    n=n+L

def loop_W(newii):

    if (mapp[n]=='North'):  
        xy[1] = xy[1]+newii
    elif (mapp[n]=='East'):
        xy[0] = xy[0]+newii
    elif (mapp[n]=='South'):
        xy[1] = xy[1]-newii
    elif (mapp[n]=='West'):
        xy[0] = xy[0]-newii

def ans():
    print ("X : ",xy[0],"y : ",xy[1],"Direction : ",mapp[n])
    
def mistake():
    print ("Check the command again!!")
    xy[0] = '0'
    xy[1] = '0'
    mapp[n] = 'North'
    
for i in range(num): 
    if (ipdirec[i]=="W"):
        A=i+1
        newi=""
        if(ipdirec[A].isnumeric()):    
            while (ipdirec[A].isnumeric()):
                newi=newi+ipdirec[A]
                A += 1
                if (A>=num):
                    break
                    newii=int(newi)
                    loop_W(newii)
            newii=int(newi)
            loop_W(newii)
        else:
            mistake()            

    elif (ipdirec[i]=="R"):
        n=n+R
        loop_R(n)
        n=n%4
    
    elif (ipdirec[i]=="L"):
        n=n+L
        loop_L(n)
        n=n%-4
    
    elif(ipdirec[i].isnumeric()):
        continue
    
    else:
        mistake()
        break

ans()
         
