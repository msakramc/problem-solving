n = input()
n=list(n)
a = []
for i in n:
    if i == '{' or i=='[' or i=='(':
        a.append(i)
    elif i == '}' or i==']' or i==')':
        if len(a)!=0:
            if a[len(a)-1]=='{' and i=='}': 
                a.pop()
            elif a[len(a)-1]=='[' and i==']':
                a.pop()
            elif a[len(a)-1]=='(' and i==')':
                a.pop()
            else:
                a.append(i)
        else:
            a.append(i)
if len(a)==0:
    print("true")
else:
    print("false")