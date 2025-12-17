a=open('data04.txt')
b=a.read()
def main(data:str):
    c=[]
    for i in b:
        if i.isalpha():
            c+=[i]
    return c
print(main(str))