### About the App

App is live at this link: https://python-exchange-rate.onrender.com/

This is a Python based app which leverages Flask for web serving. It lets the user specify a number, a base currency, and the currency to convert the final value into. It uses the Exchange Rate API to fetch the exchange rate between the currency pair, calculates the amount in the converted currency, and displays the result. 

Following is a snapshot:

<img width="1366" alt="image" src="https://github.com/user-attachments/assets/0d9fd843-e69a-46ae-95dd-414ff3dd716a" />

Default values are:
* `1` for the `amount`
* `USD` for the `base_currency`
* `INR` for the `convert_to_currency`

***

#### Resources Used 
1. API used to query exchange rate: https://www.exchangerate-api.com/docs/free
2. Web service used to host: https://dashboard.render.com/

 
*** 

#### Decription of the file tree

* templates - contains `index.html` (first webpage), `currency.html` (query successful result page), and `try_again.html` (query failed page). All of them contain the form to enter a new currency pair and query again.
* static/styles - contains styles.css
* requirements.txt - conatins the requirements for deplying the application
* weather.py - contains the `get_currency_rate()` function which performs the API call to Exchange Rate and returns the resultant JSON object
* server.py - contains the flask app routing and serving logic, along with a few edge cases. It performs the end-to-end logic of the app, from fetching the exchange rate for the specified currency pair via the form input to rendering the corresponding html file based on the query result.
* init.sh - first steps used to setup the project during local development

*** 
