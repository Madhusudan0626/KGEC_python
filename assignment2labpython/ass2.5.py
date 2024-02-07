'''Write a program that prompts the user to input number of calls and calculate the monthly
telephone bills as per the following rule:
Minimum Rs. 200 for up to 100 calls.
Plus Rs. 0.60 per call for next 50 calls.
Plus Rs. 0.50 per call for next 50 calls.
Plus Rs. 0.40 per call for any call beyond 200 calls.'''

try:
    calls = int(input("Enter the numbers of calls : \n"))
    t=calls
    if calls <= 100:
        bill = 200.00
    elif calls > 100 and calls <= 150:
        calls = calls - 100
        bill = 200 + (calls * 0.60)
    elif calls > 150 and calls <= 200:
        calls = calls - 150
        bill = 200 + (50 * 0.60) + (calls * 0.50)
    else:
        calls = calls - 200
        bill = 200 + (calls * 0.40) +(50 * 0.60)+ (50 * 0.50)
    print("Bill for the ",t," calls ",bill)
except:
    print("Invalid input datatype")