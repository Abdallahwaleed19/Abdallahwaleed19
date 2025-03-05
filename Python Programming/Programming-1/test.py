def temperture (c,k,f):
    c=(f-32)*5/9
    k=c+273.15
    return f"the temperture in celsius = {c},the temperture in kelvin = {k}"
f=int(input("Enter your number : "))
c=0
k=0
print(temperture(c,k,f))


print("--------------------------------------------------------------------")


import math
def recpol (x,y,r,theta):
    r=math.sqrt(x**2+y**2)
    theta=math.atan(y/x)
    return f"the value of r is = {r},the value of theta is = {theta}"
x,y=map(int,input("Enter your numbers : ").split())
r=0
theta=0
print(recpol(x,y,r,theta))


print("--------------------------------------------------------------------")


def student_grade(scores, list_of_grades, list_of_scores):
    for score in scores:
        if score >= 90:
            list_of_scores.append(score)
            list_of_grades.append('A')
        elif 90 > score >= 80:
            list_of_scores.append(score)
            list_of_grades.append('B')
        elif 80 > score >= 70:
            list_of_scores.append(score)
            list_of_grades.append('C')
        elif 70 > score >= 60:
            list_of_scores.append(score)
            list_of_grades.append('D')
        else:
            list_of_scores.append(score)
            list_of_grades.append('F')
    print(list_of_grades, list_of_scores)
    percent = sum(list_of_scores)/len(list_of_scores) 
    print("The percent of grades =",percent,'%')

scores = list(map(int, input("Enter your scores: ").split()))
list_of_grades = []
list_of_scores = []
student_grade(scores, list_of_grades, list_of_scores)


print("-------------------------------------------------------------------------")

