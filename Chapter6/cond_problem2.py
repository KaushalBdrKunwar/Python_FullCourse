#WAP to find out whether a student has passed or failed if it 
#requires a total 40% and at least 33% in each subject to pass.
#Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter Marks sub1:"))
s1 = (sub1/100)*100
sub2 = int(input("Enter Marks sub2:"))
s2 = (sub2/100)*100
sub3 = int(input("Enter Marks sub3:"))
s3 = (sub3/100)*100
total = sub1+sub2+sub3
t = (total/300)*100
if(s1 >=33 and  s2 >=33 and s3 >= 33 and t >= 40):
    print("Passed",t)
else:
    print("Failed",t)
           