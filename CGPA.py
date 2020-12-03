from extensioncgpa import *
from functools import reduce
name = input("please enter your name : ")

Faculty,Department = input("please enter your Faculty : "),input("please enter your Department : ")

total_points = int(input("please enter institution total CGPA point accumulation : "))

#number of sessions in institution
sessions = int(input("enter total number of sessions : "))

total,CGPA,total_units = (0,0,0)

for yr in range(1,sessions+1):

    # creating empty lists for courses, results and units
    Courses = []
    Results = []
    units = []

    # lsts is a list of lists courses,results and units
    lsts = [Courses, Results, units]

    # number_of_inputs is the number of course taken or course input
    number_of_inputs = int(input("please enter number of inputs : "))
    for lst in lsts:
        # lst goes over x for each courses,results etc
        for n in range(number_of_inputs):
            if lst == Courses:
                nxt = input("enter next Course : ")
            elif lst == Results:
                nxt = int(input("enter Results : "))
            else:
                nxt = int(input("enter units : "))
            # remember j is courese,results etc which are lists so i can append
            lst.append(nxt)

    data1 = dict(zip(Courses,Results))
    data2 = dict(zip(Courses,units))
    #adding all the units
    unit = reduce(lambda a,b : a+b, units)

    # f makes the increment possile
    s,f = (0,0)
    for result in Results:
        if result >= 70:
            result = 5
        elif result <70 and result >59:
            result = 4
        elif result <60 and result >49:
            result = 3
        elif result <50 and result > 44:
            result = 2
        elif result <45 and result > 39:
            result = 1
        else:
            result = 0
        f = result*units[s]
        total += f
        s += 1
    total_units += unit

    print(data1, 'courses and grades')
    print(data2, 'courses and units')
    print(total, 'total ')
    print(total_units, 'total units')
    CGPA = (total/total_units)
    print(f'{round(CGPA,2)} grade point for session {yr}')

print()
print(name, Faculty, Department)
print(f'{round(CGPA,2)}/{total_points} cummulative CGPA')

grade(CGPA)






