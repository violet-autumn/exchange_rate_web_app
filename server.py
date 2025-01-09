from flask import Flask, render_template, request
from waitress import serve
from currency import get_currency_rate

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/exchange')
def get_currency():
    # Get the input values - remove extra white spaces and make it upper case
    number=request.args.get('number').strip()
    base_currency = request.args.get('base_currency').strip().upper()
    convert_to_currency = request.args.get('convert_to_currency').strip().upper()

    # Check if the input values are empty
    if not bool(number):
        number=1

    if not bool(base_currency):
        base_currency="USD"

    if not bool(convert_to_currency):
        convert_to_currency="INR"
    
    # Run the API call
    currency_rates = get_currency_rate(base_currency)

    # Check if results are successful 
    if not currency_rates["result"] == "success":
        return render_template('try_again.html')

    # Return results 
    return render_template(
        'currency.html',
        base_code=currency_rates["base_code"],
        convert_code=convert_to_currency,
        amount=f"{float(number)*currency_rates['rates'][convert_to_currency]:.3f}",
        number=number
    )





if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)