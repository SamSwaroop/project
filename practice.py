def inputting():
    h=input()
    user=h.split()
    for i in range(len(user)):
        user[i]=int(user[i])
    return user


def counting(l):
    count={}
    p=[1,2,3,4,5,6,7,8,9,10]
    for j in range(len(p)):
        for k in l:
        
            if j==k:
                count[j]=count[j]+1
            else:
                count[j]=1
    return count








d=counting(inputting())
for key,value in d.items():
    print(f"{key}: {value}")