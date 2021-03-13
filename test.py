from functools import reduce



#ensure part of module is not executed elsewhere
if __name__ == '__main__':

    class GPA:
        def __init__(self, name, faculty, department, total_points, sessions):
            self.name = name
            self.faculty = faculty
            self.department = department
            self.sessions = sessions
            self.total_points = total_points

        def calculate(self):

            total, CGPA, total_units = (0, 0, 0)

            for yr in range(1, self.sessions + 1):

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

                data1 = dict(zip(Courses, Results))
                data2 = dict(zip(Courses, units))
                # adding all the units
                unit = reduce(lambda a, b: a + b, units)

                # f makes the increment possile
                s, f = (0, 0)
                for result in Results:
                    if result >= 70:
                        result = 5
                    elif 59 < result < 70:
                        result = 4
                    elif 49 < result < 60:
                        result = 3
                    elif 44 < result < 50:
                        result = 2
                    elif 39 < result < 45:
                        result = 1
                    else:
                        result = 0
                    f = result * units[s]
                    total += f
                    s += 1
                total_units += unit

                print(data1, 'courses and grades')
                print(data2, 'courses and units')
                print(total, 'total ')
                print(total_units, 'total units')
                CGPA = (total / total_units)
                print(f'{round(CGPA, 2)} grade point for session {yr}')

            print()
            print(self.name, self.faculty, self.department)
            print(f'{round(CGPA, 2)}/{self.total_points} cummulative CGPA')


    student = GPA(input('enter name : '), input('enter faculty : '), input('enter department : '),
                  int(input('enter institution CGPA point accumulation : ')),
                  int(input('enter number of sessions : ')))

    student.calculate()
