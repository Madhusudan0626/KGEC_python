'''Write a function, digit_count() in Python that counts and displays the number of digits in
the text file named 'sample.txt'''

def digit_count(f):
    count=0
    while True:
        c=f.read(1)
        if not c:
            break
        if c.isnumeric():
            count+=1
    return count

f=open("sample.txt","r")
print("Number of digits",digit_count(f))
f.close()
        




    
