import os
import requests
import json

def main():
    ##### Step 1: retrieve InSight data #####
    api_key = os.environ['nasa_api_key']
    response = requests.get("https://api.nasa.gov/insight_weather/?api_key={key}&feedtype=json&ver=1.0".format(key=api_key))
    assert response.status_code == requests.codes.ok
    data = json.loads(response.text)


if __name__ == "__main__":
    main()