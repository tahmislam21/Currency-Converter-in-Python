# <project title>
Currency Converter in Python

## Author
Name: Tahmidul Islam

## Description
The application takes a certain date and two currency codes and input. It then fetches conversion data from Frankfurt api and displays the currency conversion rate between those two codes, on that date. It also calculates the inverse rate.

I plan to develop a UI for this application to provide greater UX and enable more flexibility.

## How to Setup

STEP 1: 
Download python from the link "https://www.python.org/downloads/". It is more wise to make sure the latest version is not downloaded, rather a few versions older is preferred.

STEP 2: 
Download an IDE of your choice. My favorite is Visual Studio Code. You can download it from the link: "https://code.visualstudio.com/download"

STEP 3: 
You have now downloaded all the necessary tools. Go to VS Code, create new file and make sure to save it with a .py extension.


python 3.9.6

The in-built packages sys, datetime, and requests were used.

## How to Run the Program
On the folder where the files are saved, open powershell and run the command: 
"python main.py 2020-05-25 AUD USD"
The first argument is the date for which you want to find the conversion rates for. The second and third arguments are for which country codes you want to find the exchange rates.

## Project Structure
main.py: main program used for running business logics
checks.py: python script that will contain the code for checking inputted arguments and date validity
  
api.py: python script that will contain the code for making API calls

frankfurter.py: python script that will contain the class used for calling relevant Frankfurter endpoints

currency.py: python script that will contain the class used for extracting currency conversion rate and calculating the inverse rate

## Citations
API used from https://www.frankfurter.app/ 

