def HEX(n):#int
    HEX=[]
    while n!=0:
        HEX.insert(0,n%16)
        n=n//16
    return(HEX)

def BIN(n):#int
    BIN=[]
    while n!=0:
        BIN.insert(0,n%2)
        n=n//2
    return(BIN)

def invertlist(a):#list
    n=len(a)
    invert=[]
    for i in range(n):
        invert.insert(0,a[i])
    return invert

def euclidalgo(a,b):#int
    qlist=[a//b]
    rlist=[a%b]
    qlist.append(b//rlist[-1])
    rlist.append(b%rlist[-1])
    while rlist[-1]!=0:
        qlist.append(rlist[-2]//rlist[-1])
        rlist.append(rlist[-2]%rlist[-1])
    qlist.pop(-1)
    rlist.pop(-1)
    return [qlist,rlist]

def diophantine(a,b):#int
    [q,r]=euclidalgo(a,b)
    x=[1,0]
    y=[0,1]
    n=len(q)
    for i in range(n):
        x.append(x[-2]-x[-1]*q[i])
        y.append(y[-2]-y[-1]*q[i])
    return [x[-1],y[-1]]

def r1solve(r,p):#int
    return diophantine(p,r)[1]%(p)

def RSA(r,n,a):#int
    x=invertlist(BIN(r))
    l=len(x)
    powers=[a]
    cipher=1
    for i in range(l-1):
        powers.append((powers[-1]**2)%n)
    for i in range(l):
        if x[i]==1:
            cipher*=powers[i]
    return cipher%n


def iRSA(r,n,x,p):#int
    q=n/p
    r1=r1solve(r,(p-1)*(q-1))
    return RSA(r1,n,x)

def ASCII(a):#str
    lista=list(a)
    ASCII=[]
    for elem in lista:
        x=ord(elem)
        n=len(str(x))
        while n!=3:
            ASCII.append('0')
            n+=1
        ASCII.append(str(x))
    return ''.join(ASCII)

def iASCII(a):#str
    while len(a)%3!=0:
        lista=list(a)
        lista.insert(0,'0')
        a=''.join(lista)
    lista=[a[i:i+3] for i in range(0,len(a),3)]
    ASCII=[]
    for elem in lista:
        ASCII.append(chr(int(elem)))
    return ''.join(ASCII)

def encrypt(r,n,message):#str
    a=int(ASCII(message))
    return str(RSA(r,n,a))

def decrypt(r,n,x,p):#str
    a=iRSA(r,n,int(x),p)
    return iASCII(str(a))
