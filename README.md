# <project title>
Currency Converter in Python

## Author
Name: Tahmidul Islam

## Description
It is a Python program that will convert currency using data fetched from [Frankfurter](https://www.frankfurter.app/), an open-source API.

The program will convert currency between 2 currency codes at a specific date. It has also been designed to calculate the inverse conversion rate between these 2 currencies.

## How to Setup

  1. Unzip the zip folder
  2. Open PyCharm or other similar development environment
  3. Upload or connect all files into the development environment
  4. Make sure the Python version is as given below
  5. Upload all the packages and their version as given below


Python version: Python 3.9.6

The in-built packages sys, datetime, and requests were used.

## How to Run the Program
The command terminal will take a specific date in the given format and 2 currency codes as input arguments. Here is the command for running the script:

**`python main.py [date] [currency1] [currency2]`**

The script will return the given outputs for different scenarios:

| Scenario | Example | Output |
| ------------------- | --------------------------------- | ------------------------- |
| Success | `python main.py 2022-08-30 USD AUD` | The conversion rate on 2022-08-30 from USD to AUD was 1.4423. The inverse rate was 0.6933 |
| Missing argument | `python main.py` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2] |
| Missing argument | `python main.py 2022-01-01` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2]|
| Missing argument | `python main.py 2022-01-01 AUD` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2] |
| Too many argument | `python main.py 2022-01-01 AUD EUR GBP` | [ERROR] Need to provide 3 arguments in the following order: [date] [currency1] [currency2] |
| Incorrect currency | `python main.py 2022-01-01 usd AAA` | AAA is not a valid currency code |
| Incorrect currency | `python main.py 2022-01-01 AAA USD` | AAA is not a valid currency code |
| Incorrect currencies | `python main.py 2022-01-01 AAA bbb` | AAA and bbb are not valid currency codes |
| Incorrect date | `python main.py 2022/01/01 AAA USD` | Provided date is invalid |
| Incorrect date | `python main.py 2022-01-41 EUR bbb` | Provided date is invalid |
| API error | | There is an error with Frankfurter API |



## Project Structure

***Files structure:***

  - **main.py:** main program used for running your business logic
  - **checks.py:** Python script that will contain the code for checking inputted arguments and the date validity
  - **api.py:** python script that will contain the code for making API calls
  - **frankfurter.py:** Python script that will contain the class used for calling relevant Frankfurter endpoints
  - **currency.py:** python script that will contain the class used for extracting currency conversion rate and calculating the inverse rate
  - **README.md:** a markdown file containing details of the student, a description of the project, a listing of all Python versions and packages and instructions for running your code


## Citations
API used from https://www.frankfurter.app/ 

