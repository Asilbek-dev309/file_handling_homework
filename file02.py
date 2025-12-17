a=open('data02.txt')
b=a.read()
def main(data:str):
    c=0
    for i in b:
        c+=len(i)
    return c
print(main(str))
