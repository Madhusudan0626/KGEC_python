'''Write a Python function named feedback_analysis() to calculate and display the
following information:
Total feedbacks stored in the file.
Count of positive feedbacks.
Count of negative feedbacks'''

def feedback_analysis(f):
    p_count=n_count=0
    for i in f:
        if i.split()[0]=="Positive:":
            p_count+=1
        elif i.split()[0]=="Negative:":
            n_count+=1
    print("Number of positive feedbacks",p_count)
    print("Number of positive feedbacks",n_count)


f=open("feedback.txt","r")

feedback_analysis(f)

f.close()