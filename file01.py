f=open('data01.txt','r')
a=f.read()
s=[]
def main(data:str):
    for i in a:
        if i.isdigit():
            s.append(int(i))
print(main(str))
print(s)