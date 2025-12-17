a=open('data08.txt')
b=a.read()
def main(data:str):
    c=[]
    for i in b:
        if i.isdigit():
            c+=[int(i)]
    return max(c)
print(main(str))