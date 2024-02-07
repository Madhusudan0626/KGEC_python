l = "aeiouAEIOU"

x=input("Enter the character\n")
if(len(x)==1):
    if x in l:
        print(x,"is vowel\n")
    else:
        print(x,"is consonant\n")
else:
    print("please enter only single character...\n")