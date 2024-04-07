**WorldInformationAPI**

This API is a simple Flask-based web service that provides country information. 
It exposes a single endpoint /country-info which accepts a GET request with a query parameter country specifying the name of the country for which information is requested. 
The API then retrieves data from the Rest Countries API, specifically version 3.1, to fetch details about the specified country.

The information returned by this API includes the country's name, capital city, area, region, subregion, and languages spoken. 
It provides a concise overview of essential details about a given country. The API is designed to be lightweight and easy to use, making it suitable for applications that require basic country information retrieval.
