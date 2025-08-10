import requests

def fetch_data(lat,lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)  
    data = response.json()

    if "latitude" in data and "longitude" in data:
        latitude = data["latitude"]
        longitude = data["longitude"]
        time = data["current_weather"]["time"]
        temp = data["current_weather"]["temperature"]
        windspeed = data["current_weather"]["windspeed"] 
        
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Time:",time)
        print("Temperature:",temp)
        print("Windspeed:",windspeed)

        weathercode = data["current_weather"]["weathercode"]
        if weathercode == 0:
            print("Weather: Clear Sky")
        elif 1 <= weathercode <= 3:
            print("Weather: Mainly Clear")
        elif 45 <= weathercode <= 48:
            print("Weather: Fog")
        elif 51 <= weathercode <= 67:
            print("Weather: Rain or Drizzle")
        elif 71 <= weathercode <= 77:
            print("Weather: Snow")
        elif 80 <= weathercode <= 82:
            print("Weather: Rain Showers")
        elif 95 <= weathercode <= 99:
            print("Weather: Thunderstorm")
        else:
            print("Weather: Unknown condition")
        
  
    else:
        raise Exception("Failed to fetch data")

try:
    lat = float(input("Enter your latitude  : "))
    lon = float(input("Enter your longitude : "))
    fetch_data(lat,lon)
except ValueError:
    print("Please enter valid numbers for latitude and longitude.")
except Exception as e:
    print(str(e))