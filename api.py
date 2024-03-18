import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => To be filled by student
    string

    Pseudo-code
    ----------
    # => To be filled by student
    make a request to the url endpoint. 
        If successfull, status code will be 200. 
            Then return the object 
        If not succesfull, status code will not be 200
            Then system will flag error message and terminate the program     

    Returns
    -------
    # => To be filled by student
    dictionary
    """
    
    resp = requests.get(url)
    if resp.status_code == 200:
       return resp.json()
    else:
        print("There is an error with Frankfurter API")
        sys.exit(0)   
    return {}
