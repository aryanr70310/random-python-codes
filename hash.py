def hash_quartic(a):
    table=["-"]*23
    for k in a:
        if k in table:
            continue
        i=int((4*k+7)%23)
        temp=i
        j=0
        while table[i]!="-":
            i=(temp+j**4)%23
            j+=1
        table[i]=k
    return table
def hash_double(a):
    table=["-"]*23
    for k in a:
        if k in table:
            continue
        i=int((4*k+7)%23)
        temp=i
        j=0
        while table[i]!="-":
            i=(temp+j*(17-(k%17)))%23
            j+=1
        table[i]=k
    return table
