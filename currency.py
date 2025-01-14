import sys
from typing import Any
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, date,  from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = 1 
        self.rate = 1 ## The rate will be assigned once the api is called
        self.inverse_rate = self.reverse_rate()
        self.date = date
        self.api = Frankfurter()
        
    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        """
        currency_list = self.api.get_currencies_list()
        
        if self.from_currency not in currency_list:
            if self.to_currency not in currency_list:
                print(f"{self.from_currency} and {self.to_currency} are not valid currency codes")
                sys.exit(0)

        if self.to_currency not in currency_list:
            if self.from_currency in currency_list:
                print(f"{self.to_currency} is not a valid currency code")
                sys.exit(0)
                 
        if self.from_currency not in currency_list:
            if self.to_currency in currency_list:
                print(f"{self.from_currency} is not a valid currency code")
                sys.exit(0)
        

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        """
        return round(1/self.rate, 4)


    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.
        """
        rate = round(rate, 4)
        return rate

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief
        """
        historical_rate = self.round_rate(self.api.get_historical_rate(self.from_currency, self.to_currency, self.date, self.amount))
        print(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {historical_rate}.")
        self.rate = historical_rate        
        
        inverse_rate = (self.reverse_rate())
        inverse_rate_rounded = self.round_rate(inverse_rate)
        print(f"The inverse rate was {inverse_rate_rounded}")
        

        
