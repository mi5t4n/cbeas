import requests
from requests.exceptions import HTTPError

try:
    # Get the weather data
    response = requests.get('http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
    # Raise error if there is any.
    response.raise_for_status()
except HTTPError as httpError:
    print(f'HTTP error occurreed : {httpError}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    # Decode content as json
    contentJson = response.json()
    # Print content-type header
    print(response.headers['content-type'])
    # Print the coordinates.
    print(contentJson['coord'])

