#programa que retorna um máximo
x=float(input('insira um valor'))
y=float(input('insira um valor'))
z=float(input('insira um valor'))
def máx():
    if x>y and x>z:
        print("o valor máximo é: ",x)
    elif y>x and y>z:
        print("o valor máximo é: ",y)
    elif z>y and z>x:
        print("o valor máximo é: ",y)

máx()  
