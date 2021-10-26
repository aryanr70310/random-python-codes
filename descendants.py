
def nextdescendant(n,m,lis):#finds next descendant
    while n!=0:
        m+=lis[n%10]
        n=int(n/10)
    return m
def checkstrength(n,a,k,lis):#finds strength of each number
    while True:
        if len(a)>k:
            break
        elif nextdescendant(n,0,lis) in a:
            break
        else:
            n=nextdescendant(n,0,lis)
            a.append(n)
    return len(a)
def descendants(n1,n2,k):
    a=[]
    lis={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}#list of factorials
    for i in range(n1,n2):
        if checkstrength(i,[],k,lis)==k:
            a.append(i)
    return len(a)

    