cat=int(input())
n=0
for i in range(cat):
    a=input()
    cata=list(a)
    for i in range(len(cata)):
        if cata[i]=='к' and cata[i+1]=='о' and cata[i+2]=='т' or cata[i]=='К' and cata[i+1]=='о' and cata[i+2]=='т':
            n=n+1
if n>=1:
    print('МЯУ')
else:
    print('НЕТ')
                
