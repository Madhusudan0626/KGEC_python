import stackclas as st1

s = input("Enter your postfix expression\n")

st=st1.stackpro(len(s))
for i in s:
    if i.isdigit():
        st.push_s(i)
    else:
        x=st.pop_s()
        y=st.pop_s()
        st.push_s(str(eval(y + i + x)))
print(st.a[st.top])