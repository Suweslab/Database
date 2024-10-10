import sqlite3
import requests

conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()


def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2cb58eb346889872e8a873c4051746e6"
    response = requests.get(url)
    return response.json()

def store_weather_data(cursor, weather_data):
    city_id = weather_data['id']
    date = weather_data['dt']  # timestamp
    temperature = weather_data['main']['temp'] - 273.15  # convert to Celsius
    humidity = weather_data['main']['humidity']
    insert_weather_record(cursor, city_id, date, temperature, humidity)

def create_weather_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS WeatherRecords (
        id INTEGER PRIMARY KEY,
        city_id INTEGER,
        date TEXT NOT NULL,
        temperature REAL NOT NULL,
        humidity INTEGER NOT NULL
    )''')


def insert_weather_record(cursor, city_id, date, temperature, humidity):
    cursor.execute('''
    INSERT INTO WeatherRecords (city_id, date, temperature, humidity)
    VALUES (?, ?, ?, ?)''', (city_id, date, temperature, humidity))


#call function to create table created
# #check weather_data.db to view table
create_weather_table(cursor)
