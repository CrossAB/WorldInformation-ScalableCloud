from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Endpoint to retrieve country information
@app.route('/country-info', methods=['GET'])
def country_info():
    country_name = request.args.get('country')  # Get country name from query parameter
    if not country_name:
        return jsonify({"error": "Country parameter is missing"}), 400

    # Fetch data from Rest Countries API
    url = f'https://restcountries.com/v3.1/name/{country_name}'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve data from external API"}), 500

    data = response.json()

    # Check if the country exists
    if not data:
        return jsonify({"error": "Country not found"}), 404

    # Extract relevant information
    country_info = {
        "name": data[0]["name"]["common"],
        "capital": data[0]["capital"][0] if data[0]["capital"] else "N/A",
        "area": data[0]["area"] if "area" in data[0] else "N/A",
        "region": data[0]["region"] if "region" in data[0] else "N/A",
        "subregion": data[0]["subregion"] if "subregion" in data[0] else "N/A",
        "languages": list(data[0]["languages"].values()) if "languages" in data[0] else "N/A",
    }

    return jsonify(country_info)


if __name__ == '__main__':
    app.run(debug=True)
