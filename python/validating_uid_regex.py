
import re


def is_valid_uid(uid: str):
    # conditions = {
    #     "minimum two uppercase": lambda s: re.search(r'[A-Z]{2}', s),
    #     "atleast three digits": lambda s: re.search(r'\d\d\d', s),
    #     "only alpha nummeric": lambda s: re.search(r'[^a-zA-Z0-9]', s),
    #     "no char should repeat": lambda s: re.search(r'(.)\1', s),
    #     "exact 10 chars": lambda s: len(s) == 10
    # }
    conditions = {
        "minimum two uppercase": lambda s: bool(re.search(r'(?=(?:[a-z\d]*[A-Z]){2})', uid)),
        "atleast three digits": lambda s: bool(re.search(r'(?=(?:.*\d){3})', uid)),
        "exact 10 alphanumeric chars": lambda s: bool(re.search(r'(?:([a-zA-Z\d])(?!.*\1)){10}$', uid))
    }

    return True if all(conditions[condition](uid) for condition in conditions) else False


if __name__ == '__main__':
    print('Valid' if is_valid_uid("B1CD102354") else "Invalid")
    print('Valid' if is_valid_uid("B1CDEF2354") else "Invalid")
    print('Valid' if is_valid_uid("944A4NKtE2") else "Invalid")
