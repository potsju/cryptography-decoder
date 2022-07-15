
from re import A


def main(num):
    m=""
    a= str(num)
    length = 3
    X=[1000000000000]
    Y=[1000000000000]
    for i in range(0, int(len(a)),length):
            if (int(a[i:i+1]) == 0):
                X.append(a[i+1:i+2])
                Y.append(a[i+2:i+3])
            elif(int(a[i:i+2]) * int(a[i+2:i+3]) > 26):
                X.append(a[i:i+1])
                Y.append(a[i+1:i+3])
            else:
                X.append(a[i:i+2])
                Y.append(a[i+2:i+3])
        
    for j in range(0,(len(a)//3)+1):
        p=int(X[j])*int(Y[j])
        if(p==26):
            m+="A"
        if(p==18):
            m+="B"
        if(p==9):
            m+="C"
        if(p==2):
            m+="D"
        if(p==21):
            m+="E"
        if(p==15):
            m+="F"
        if(p==1):
            m+="G"
        if(p==19):
            m+="H"
        if(p==12):
            m+="I"
        if(p==10):
            m+="J"
        if(p==4):
            m+="K"
        if(p==3):
            m+="L"
        if(p==24):
            m+="M"
        if(p==25):
            m+="N"
        if(p==6):
            m+="O"
        if(p==7):
            m+="P"
        if(p==8):
            m+="Q"
        if(p==13):
            m+="R"
        if(p==5):
            m+="S"
        if(p==17):
            m+="T"
        if(p==14):
            m+="U"
        if(p==20):
            m+="V"
        if(p==11):
            m+="W"
        if(p==23):
            m+="X"
        if(p==16):
            m+="Y"
        if(p==22):
            m+="Z"
    return m


if __name__ == "__main__":
    num = input("Enter the number:")
    print(main(num))

    
