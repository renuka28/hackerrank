def validate_and_parse_email(emails):
    """ validates if a list of given emails are in valid format or not
        https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
        A valid email address meets the following criteria:

            It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
            The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
            The domain and extension contain only English alphabetical characters.
            The extension is 1,2  or 3  characters in length.
     Args:
         arr (list): list emails 
     Returns:
         list : list of valid emails
    """
    import re
    email_pattern = r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>'
    valid_emails = []
    for name_email in emails:
        if re.match(email_pattern, name_email.split(' ')[1]):
            valid_emails.append(name_email)
    return valid_emails
