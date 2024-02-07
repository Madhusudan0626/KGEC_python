
'''Write a program which prompts the user to input principle, rate and time and
calculate compound interest. The formula is:
CI = P(1+R/100)^T - P'''
p,t,r=[float(x) for x in input("Enter the principle , rate of interest , time \n").split( )]
print("Compound Interest : ",(p*(1+r/100)**t)-p)