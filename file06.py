a=open('data06.txt')
b=a.read()
def main(data:str):
    d=b.split()
    c=[]
    for i in d:
        c+=[len(i)]
    return c
print(main(str))