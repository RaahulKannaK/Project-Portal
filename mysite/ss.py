def minion_game(string):
    count=0  #Stuart
    count1=0 #Kevin
    e=len(string)
    for i in range(e):
        a=string[i]
        if (a not in ['A','E','I','O','U']):
            b=i
            b1=b+1
            f=e+1
            while True:
                if b1==f:
                    break
                else:

                    count+=1
                    b1+=1
        else:
            b=i
            b1=b+1
            f=e+1
            while True:
                if b1==f:
                    break
                else:
                    count1+=1
                    b1+=1
    if count>count1:
        print("Stuart",count)  
    elif count1>count:
        print("Kevin",count1)
    else:
        print("Draw")   
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)