
def second_lowest_grade(grade_names):
    """ finds names having second lowest grades
     Args:
         arr (list of list): list of list in ["name",grade] format whose second lowest grade
         needs to be found
     Returns:
         list : sorted list of names who have the second lowest grades
    """
    if(len(grade_names) < 2):
        return [grade_names[0][1]]
    # remove duplicate grades by creating a set
    grades_set = set(x[1] for x in grade_names)
    # get the second lowest grade by sorting and picking up the second element
    s_lowest_grade = sorted(grades_set)[1]
    # create a list of names which have second lowest grade
    second_lowest_grade_names = [
        name_grade[0] for name_grade in grade_names if name_grade[1] == s_lowest_grade]
    return sorted(second_lowest_grade_names)
