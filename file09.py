a=open('data09.txt')
b=a.read()
def main(data:str):
    c=[]
    for i in b:
        if i.isdigit():
            c+=[int(i)]
    return min(c)
print(main(str))