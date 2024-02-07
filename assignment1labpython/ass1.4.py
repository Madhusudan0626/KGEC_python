'''Write a program which accept principle, rate and time from user and print the
simple interest. The formula to calculate simple interest is: simple interest =
principle x rate x time / 100
'''

p,t,r=[float(x) for x in input("Enter the principle , rate of interest , time \n").split( )]
print("Simple interest is ",(p*t*r)/100)