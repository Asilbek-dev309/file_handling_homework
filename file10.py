a=open('data10.txt')
b=a.readlines()
def main(data:str):
    d=[]
    for i in b:
        d+=[len(i)-1]
    return max(d)
print(main(str))