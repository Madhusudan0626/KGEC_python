'''Write the definition of a function zero_ending(scores) to add all those values in the list of
scores, which are ending with zero and display the sum.'''

def zero_ending(score):
    sum=0
    for i in score:
        if i % 10==0:
            sum+=i
    print("sum of all ending zero elements",sum)

l=[int(x) for x in input("Enter the elements of list \n").split()]
zero_ending(l)

