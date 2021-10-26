def palindrome(s):
    if s==s[::-1]:
        return len(s)
    return 1
def LP(s):
    S=s[0]
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            S+="ϱ"#adds ϱ between consecutive letters
        S+=s[i]
    f=LOP(S)#f is LOP of S
    c=0
    for i in range(len(S)):
        if i+f>len(S):
            break
        else:
            if palindrome(S[i:i+f])==f:
                c=S[i:i+f].count("ϱ")#calculates c which is to be subtracted from f to get answer
                break
    return f-c
def LP2(s):
    S=s[0]
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            S+="ϱ"#adds ϱ between consecutive letters
        S+=s[i]
    a=[]
    f=0
    for i in range(len(S)):
        if LOP(S[i:len(S)]+S[0:i])>f:
            f=LOP(S[i:len(S)]+S[0:i])
    for i in range(len(S)):
        if LOP(S[i:len(S)]+S[0:i])==f:
            a.append(S[i:len(S)]+S[0:i])#all possible strings which may contain longest palindrome
    c=0
    d=len(S)
    for j in range(len(a)):
        for i in range(len(a[j])):
            if palindrome((a[j])[i:i+f])==f:
                c=(a[j])[i:i+f].count("ϱ")#calculates d which is to be subtracted from f to get answer
        if d>c:
            d=c
    return f-d