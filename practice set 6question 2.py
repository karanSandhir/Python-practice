print("welcom to the program of student 's  perctage to check he or she i pass or fail")
a=int(input("enter the marks of stuent 1 in maths = "))
b=int(input("enter the marks of stuent 1 in scince= "))
c=int(input("enter the marks of stuent 1 in s.s.t= "))
total_perctange=(100*(a+b+c))/300
if (total_perctange>40 and a>33 and b>33 and c>33):
    print("stdent is pass : ",total_perctange)
else:
    print("student is fail : ",total_perctange)
