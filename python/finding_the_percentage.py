def finding_the_percentage(grade_names, query_name):
    """
    Finds average of three grades for the given stundent - link below says it is percentage althought it is just an average
    https://www.hackerrank.com/challenges/finding-the-percentage/problem

    Args:
        grade_names (dictionary with name as key and grades as a list)
        query_name: name of the student whose average needs to be calcualted

    Return:
        average - or 'perencetage' as per the problem statemetn
    """
    return sum(grade_names[query_name])/3
