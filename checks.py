from datetime import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => To be filled by student
    list

    Pseudo-code
    ----------
    # => To be filled by student
    check if length of list is equal to 3 components
    if not, print error message and exit the program

    Returns
    -------
    # => To be filled by student
    NULL
    """

    # => To be filled by student
    if len(args) != 3:
        print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        sys.exit(0)
        

def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => To be filled by student
    str(date)

    Pseudo-code
    ----------
    # => To be filled by student
    check if date is in the correct format
    if not, print error message and exit the program

    Returns
    -------
    # => To be filled by student
    """
    # => To be filled by student
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except:
        print("Provided date is invalid")
        sys.exit(0)    