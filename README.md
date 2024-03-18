# <project title>
Currency Converter in Python

## Author
Name: Tahmidul Islam
Student ID: 24587139

## Description
<What your application does>
The application takes a certain date and two currency codes and input. It then fetches conversion data from Frankfurt api and displays the currency conversion rate between those two codes, on that date. It also calculates the inverse rate.
<Some of the challenges you faced>
The main challenge for me was to implement the unit tests in the modules. In addition, deciding on how to assign values to some of the class attributes was also tricky for me.
<Some of the features you hope to implement in the future>
I hope to develop a UI for this application to provide greater UX and enable more flexibility.

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
STEP 1: 
Download python from the link "https://www.python.org/downloads/". It is more wise to make sure the latest version is not downloaded, rather a few versions older is preferred.

STEP 2: 
Download an IDE of your choice. My favorite is Visual Studio Code. You can download it from the link: "https://code.visualstudio.com/download"

STEP 3: 
You have now downloaded all the necessary tools. Go to VS Code, create new file and make sure to save it with a .py extension.

<Which Python version you used>
python 3.9.6
<Which packages and version you used>
The in-built packages sys, datetime, and requests were used.

## How to Run the Program
<Provide instructions and examples>
On the folder where the files are saved, open powershell and run the command: 
"python main.py 2020-05-25 AUD USD"
The first argument is the date for which you want to find the conversion rates for. The second and third arguments are for which country codes you want to find the exchange rates.

## Project Structure
<List all folders and files of this project and provide quick description for each of them>
main.py: main program used for running business logics
checks.py: python script that will contain the code for checking inputted arguments and date validity
api.py: python script that will contain the code for making API calls
frankfurter.py: python script that will contain the class used for calling relevant Frankfurter endpoints
currency.py: python script that will contain the class used for extracting currency conversion rate and calculating the inverse rate
test_checks.py: python script for testing code from checks.py
test_frankfurter.py: python script for testing code from frankfurter.py
test_api.py: python script for testing code from api.py
test_currency.py: python script for testing code from currency.py

## Citations
<Mention authors and provide links code you source externally>
API used from https://www.frankfurter.app/ 

