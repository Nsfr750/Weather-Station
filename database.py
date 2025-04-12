import sqlite3

class WeatherDatabase:
    def __init__(self, db_name="weather_data.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    temperature REAL,
                    humidity REAL,
                    wind_speed REAL,
                    wind_direction TEXT,
                    rain_level REAL,
                    solar_radiation REAL
                )
                """
            )

    def save_data(self, timestamp, temperature, humidity, wind_speed, wind_direction, rain_level, solar_radiation):
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO weather (timestamp, temperature, humidity, wind_speed, wind_direction, rain_level, solar_radiation)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (timestamp, temperature, humidity, wind_speed, wind_direction, rain_level, solar_radiation),
            )

    def retrieve_data(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM weather").fetchall()