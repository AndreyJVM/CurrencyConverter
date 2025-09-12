import requests
import os
from flask import Flask, render_template, request, session
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
# session secret key.
app.secret_key = "xyzcurr_"
# variable to access the API key stored as environment variable.
app_api_key = os.getenv("CURRENCY_API_KEY")

exchange_rate_json = {}
currency_list_json = {}
currency_code_arr = []
currency_name_arr = []

# Routing to the home page of the web app.
@app.route('/',methods=["POST","GET"])
@app.route('/index',methods=["POST","GET"])
def index():
    # Check if the key 'last_checked_time' is present in session or not. If not present, insert the key and assign None as value.
    if "last_checked_time" not in session:
        session["last_checked_time"] = None
    # URL to fetch currency exchange rates from CurrencyAPI.
    url = "https://api.currencyapi.com/v3/latest"
    headers = {
        'apikey': app_api_key
    }
    # Get the current date and time as timestamp.
    current_time = datetime.now().timestamp()
    if session.get("last_checked_time")!=None:
        t1 = session.get("last_checked_time")
        t2 = current_time
        # Calculate the difference between the timestamps.
        difference = t2-t1
        # Since this is not the first time of using the web app, mark the value of key 'first_time' as False in session.
        session["first_time"] = False
        session["last_checked_time"] = current_time
        # Store the difference in minutes from the current time and the last checked time of API response by dividing by 60.
        session["minutes_diff"] = difference/60
    else:
        # Since this is the first time of using the web app, mark the value of the key 'first_time' as True.
        session["first_time"] = True
        session["last_checked_time"] = current_time
    # If it is a GET HTTP method.
    if request.method=="GET":
        # Get the response from the API only if this is the first time of using the web app, or when its been more than 40 minutes from the time it is lastly fetched from API.
        if session.get("first_time")==True or (session.get("first_time")==False and session.get("minutes_diff")>40):
            # Fetching the response from exchange rates API.
            response = requests.request("GET", url, headers=headers)
            status = response.status_code
            # URL to fetch list of currencies from CurrencyAPI.
            currency_list_url = "https://api.currencyapi.com/v3/currencies"
            currency_list_response = requests.request("GET",currency_list_url,headers=headers)
            currency_list_status_code = currency_list_response.status_code
            # Check if the status of exchange rate url and status of currency list url are active.
            if status==200 and currency_list_status_code==200:
                global exchange_rate_json, currency_list_json
                exchange_rate_json = response.json()
                # Store the JSON response fetched from exchange rate url to session for 40 minutes.
                session["exchange_rates"] = exchange_rate_json["data"]
                currency_list_json = currency_list_response.json()
                currency_code_arr = []
                currency_name_arr = []
                for every_item in currency_list_json["data"].keys():
                    currency_code_arr.append(every_item)
                    currency_name_arr.append(currency_list_json["data"].get(every_item)["name"])
                return render_template("index.html",currency_code_arr=currency_code_arr)
            else:
                # If the status code of the API url is not 200.
                return "Internal API error!"
        else: # Do not fetch the response again from API because it is not the first time of using this web app, or when its been only less than 40 minutes since the last time the API response is fetched.
            # Get the source currency code from select tag with name 'from_currency_choice'.
            from_choice = request.args.get("from_currency_choice")
            # Get the destination currency code from select tag with name 'to_currency_choice'.
            to_choice = request.args.get("to_currency_choice")
            # Get the user input amount to convert from source to destination currency.
            currency_input = request.args.get("currency_input")
            currency_code_arr = []
            converted = ""
            # When the variables 'from_choice', 'to_choice', and 'currency_input' are not None.
            if from_choice and to_choice and currency_input:
                converted = convert_currency(from_choice,to_choice,float(currency_input))
            for every_item in session.get("exchange_rates").keys():
                currency_code_arr.append(every_item)
            return render_template("index.html",
                                   currency_code_arr=currency_code_arr,ans=converted,source_currency=from_choice,
                                   destination_currency=to_choice,user_input=currency_input)

# Routing function to show the exchange rates for all currencies with USD as base currency.
@app.route('/exchange_rate')
def show_exchange_rates():
    if exchange_rate_json!={}:
        live_exchange_rates = session.get("exchange_rates")
        currency_list_dict = currency_list_json["data"]
        return render_template("exchangerate.html",exchange_rate_dict=live_exchange_rates)
    elif len(session.get("exchange_rates"))>0:
        exchange_rate_dict = session.get("exchange_rates")
        return render_template("exchangerate.html",exchange_rate_dict=exchange_rate_dict)
    else:
        return "Could not fetch exchange rates at the moment!"

# Function to convert currency value from source to destination for the given user input value.
def convert_currency(source_currency_code,destination_currency_code,user_input_value):
    user_input_value = user_input_value
    exchange_rates = session.get("exchange_rates")
    source_currency_value = exchange_rates.get(source_currency_code).get("value")
    source_currency_value_1 = 1/source_currency_value
    destination_currency_value = exchange_rates.get(destination_currency_code).get("value")
    destination_currency_value_1 = 1/destination_currency_value
    source_currency_at_1 = (source_currency_value_1/destination_currency_value_1)
    converted_total_value = source_currency_at_1*user_input_value
    return converted_total_value

# Function to route to any random web page.
@app.route('/<anypage>')
def anypage(anypage):
    return "Page Not Found"

if __name__=="__main__":
    app.run(debug=True)

