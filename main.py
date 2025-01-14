import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
   
    print("Launching app")
    args = sys.argv[1:]
    
    check_arguments(args)
    check_date(args[0])    

    converter1 = CurrencyConverter(args[0], args[1], args[2])
    converter1.check_currencies()    

    converter1.get_historical_rate()
    
