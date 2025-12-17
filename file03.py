a=open('data03.txt')
b=a.read()
def main(data:str):
    c=[]
    for i in b:
        if i.isdigit():
            c+=[i]
    return c
print(main(str))