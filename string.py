def commonString (s, t):
    if(s.find(t) >= 0):
        return(s)
    elif(t.find(s) >= 0):
        return(t)
    else:
        lowerS = s.find(t[0])
        upperS = s.find(t[-1])
        print(lowerS)
        print(upperS)
        if (lowerS>=0 or upperS >=0):
            if(len(s)>=len(t)):
                s.split(s.find(t[0]):(s.find(t[0])+len(t))
            elif(len(t)>len(s)):

        else:
            return print(s+t)


print(commonString('champak', 'pakbhu'))

