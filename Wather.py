import requests
API_URL ="https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data. Please try again later.")
        return None

def get_temperature_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['pressure']
    return None

def main():
    data = get_weather_data()
    if data is None:
        return

    while True:
        print("\n1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (yyyy-mm-dd): ")
            temperature = get_temperature_by_date(data, date)
            if temperature:
                print(f"The temperature on {date} is {temperature}°C")
            else:
                print("No data available for the given date.")

        elif choice == '2':
            date = input("Enter the date (yyyy-mm-dd): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed:
                print(f"The wind speed on {date} is {wind_speed} m/s")
            else:
                print("No data available for the given date.")

        elif choice == '3':
            date = input("Enter the date (yyyy-mm-dd): ")
            pressure = get_pressure_by_date(data, date)
            if pressure:
                print(f"The pressure on {date} is {pressure} hPa")
            else:
                print("No data available for the given date.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
