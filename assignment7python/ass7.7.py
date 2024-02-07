'''Write a method in python to display the elements of list thrice if it is a number and display
the element terminated with ‘#’ if it is not a number.'''
def modifylist(l):
    ls=[]
    for i in l:
        if i.isnumeric():
            ls.append(i*3)
        else:
            ls.append(i+"#")
    for x in ls:
        print(x)
ThisList=["41","DROND","GIRIRAJ", "13","ZARA"]
modifylist(ThisList)