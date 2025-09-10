from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Set your API URL and key (sign up for Open Exchange Rates)
API_URL = "https://openexchangerates.org/api/latest.json"
API_KEY = "your-api-key-here"  # Replace with your own API key

@app.route('/api/exchange_rate', methods=['GET'])
def get_exchange_rate():
    try:
        # Make the API request to Open Exchange Rates
        response = requests.get(f"{API_URL}?app_id={API_KEY}")
        data = response.json()

        if response.status_code == 200:
            # Extract exchange rate data
            rates = data['rates']
            return jsonify({
                'status': 'success',
                'rates': rates
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Unable to fetch exchange rates'
            }), 500
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
