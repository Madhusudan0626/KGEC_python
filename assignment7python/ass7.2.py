'''Write a function, is_vowel that returns the value true if a given character is a vowel, and
otherwise returns false. Write another function main, in main() function accept a string
from user and count number of vowels in that string.'''

def is_vowel(c):
    s="aeiuAEIOU"
    if c in s:
        return True
    return False
    
def main():
    x=input("Enter the string\n")
    d=[]

    for i in x:
        if is_vowel(i):
            d.append(i)
    print("Number of vowels",len(d))
if __name__ == "__main__":
    main()
