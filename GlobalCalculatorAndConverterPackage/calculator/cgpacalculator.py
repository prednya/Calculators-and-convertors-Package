def gpa_calc(grades: list,credits: list):
    total_credits=0
    gpa=0.0
    for grade,credit in zip(grades,credits):
        gpa+=grade*credit
        total_credits+=credit
        final_gpa=gpa/total_credits
    return str(final_gpa)[:5]




# grades=[10,9,10,8,10]
# creditss=[4,3,4,3,2]
# print(gpa_calc(grades,creditss))