import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_PanC0ghGyYnwhxk0TqFxJ8d1sOfUTRXt7rNcwIRk"


def get_actual_currencies():
    response = requests.get(URL + API_KEY)

    return response.json().get('data')
