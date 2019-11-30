def find_runner_up_builtin_1(arr):
    """ finds second biggest number using built in sorted and sets
     Args:
         arr (list of ints): list of ints whose second max value
         needs to be found
     Returns:
         int : second max value in arr
    """
    set_arr = set(arr)
    sorted_arr = sorted(set_arr, reverse=True)

    if len(sorted_arr) <= 1:
        print("can't find runner up score")
        return None
    else:
        return sorted_arr[1]


def find_runner_up_builtin_2(arr):
    """ finds second biggest number using built in max method
     Args:
         arr (list of ints): list of ints whose second max value
         needs to be found
     Returns:
         int : second max value in arr
    """
    max_val = max(arr)
    arr = [x for x in arr if x != max_val]
    return max(arr)


def find_runner_up(arr):
    """ finds second biggest number without using any builtins
     Args:
         arr (list of ints): list of ints whose second max value
         needs to be found
     Returns:
         int : second max value in arr
    """
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    arr = [x for x in arr if x != max_val]

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num

    return max_val
