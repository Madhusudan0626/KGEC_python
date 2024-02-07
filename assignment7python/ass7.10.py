'''Write a function that accepts a dictionary as an argument. If the dictionary contains
duplicate values, it should return an empty dictionary. Otherwise, it should return a new
dictionary where the values become the keys and the keys become the values'''

def takedic(d):
    l=[]
    dic=dict()
    for i in d:
        if d[i] not in l:
           l.append(d[i])
    if len(l) != len(d):
        d.clear()
    else:
        dic=dict([(value,key) for (key,value) in d.items()])
    return dic
print("First case")

d1={
    'a':10,
    'b':20,
    'c':30
}
print(d1)
print(takedic(d1))
print("Second case")
d2={
    'a':10,
    'b':20,
    'c':20
}
print(d2)
print(takedic(d2))
