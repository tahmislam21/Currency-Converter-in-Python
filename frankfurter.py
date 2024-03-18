from api import call_get

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
    def __init__(self):
        self.base_url = 'https://api.frankfurter.app'
        self.currencies_url = 'https://api.frankfurter.app' + '/' + 'latest' ## base_url + latest
        self.historical_url = 'https://api.frankfurter.app' + '/' + '1999-01-04' ## base_url + date
        self.currencies = self.get_currencies_list()

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        # => To be filled by student
        no parameters but self

        Pseudo-code
        ----------
        # => To be filled by student
        use the call_get function of api class to access the url endpoint and get the dictionary containing currency codes and rates
        
        Returns
        -------
        # => To be filled by student
        list
        """       
        curr_list = call_get('https://api.frankfurter.app/latest') ## get(base_url)
        return curr_list.get('rates').keys()
        

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        # => To be filled by student
        string

        Pseudo-code
        ----------
        # => To be filled by student
        function will check if the string is present in the key of the currencies dictionary data structure
            return true if present
            return false if not present

        Returns
        -------
        # => To be filled by student
        boolean value (true/false)
        """
        
        if currency in self.currency_list:
            return True
        else:
            return False    



    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

        Parameters
        ----------
        # => To be filled by student
        str, str, str(date), int

        Pseudo-code
        ----------
        # => To be filled by student
        function will get currency list for a specified date from the Frankfurt api
        find the ratio of (to_currency : from_currency) to get the exchange rate

        Returns
        -------
        # => To be filled by student
        float
        """
        
        currencies = call_get(self.base_url +'/' + from_date)
               
        hist_currency = currencies.get('rates')

        hist_exchange_rate = hist_currency[to_currency] / hist_currency[from_currency]   
        return hist_exchange_rate
