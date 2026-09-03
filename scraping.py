import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
response = requests.get(url)
"""
if response.status_code == 200:
    data = response.json()
    earthquakes = data['features']
    for earthquake in earthquakes:
        properties = earthquake['properties']
        place = properties['place']
        magnitude = properties['mag']
        time = properties['time']
        print(f"Place: {place}, Magnitude: {magnitude}, Time: {time}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

"""

#print(response.text)

app = Flask(__name__)

@app.route('/')
def show_earthquakes():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response = requests.get(url)
    data = response.json()

    records =[]
    for earthquake in data['features']:
        properties = earthquake['properties']
        records.append({
            'place': properties['place'],
            'magnitude': properties['mag'],
            'time': properties['time'],
            'link': properties['url']
        })
        records.append({})
    return render_template('earthquakes.html', records=records)
if __name__ == '__main__':
    app.run(debug=True)
