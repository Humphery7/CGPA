def grade(x):
    #function determines grade section
    if x >= 4.50:
        print("1st class division")
    elif x < 4.50 and x >= 3.5:
        print("2nd class upper division")
    elif x < 3.5 and x >= 3.0:
        print("2nd class lower division")
    elif x < 3.0 and x >= 2.0:
        print("3rd class division")
    elif x < 2.0 and x >= 1.0:
        print("pass division")
    else:
        print("advice for withdrawal, please report to department")



