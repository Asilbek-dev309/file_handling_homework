a=open('data05.txt')
b=a.read()
def main(data:str):
    c=[]
    d=[]
    for i in b:
        if i.isdigit():
            c+=[i]
        else:
            d+=[i]
    return [len(c),len(d)]
print(main(str))