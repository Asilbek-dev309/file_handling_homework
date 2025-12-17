a=open('data07.txt')
b=a.read()
def main(data:str):
    c=0
    for i in b:
        if i.isdigit():
            c+=int(i)
    return c
print(main(str))