'''

"abcde" , "cde"--> "cde"
"abcde" , "aBcDe"--> "ace"
"ababcbcde", "abbccdde"--> "abbccde"

que esten en ambas dos cadenas, las concatena y devuelve

'''

def lcs(a,b):
    alist=list(a)
    blist=list(b)
    sol=""
    for i in blist:
        if i in alist:
            if i in list(sol):
                if alist.count(i)>=blist.count(i):
                    sol+=i
            else:
                sol += i
    return sol

print(lcs("abcde" , "cde"))
print(lcs("abcde","aBcDe"))
print(lcs("ababcbcde", "abbccdde"))

