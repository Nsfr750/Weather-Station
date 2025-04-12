import random

class WeatherStation:
    def __init__(self, mode="usb"):
        self.mode = mode

    def connect(self):
        if self.mode == "demo":
            return "Demo Mode: Connected"
        elif self.mode == "usb":
            return "USB: Connected"
        elif self.mode == "wifi":
            return "WiFi: Connected"
        else:
            return "Unknown Mode"

    def get_data(self):
        if self.mode == "demo":
            return {
                "temperature": random.uniform(20, 30),
                "humidity": random.uniform(30, 70),
                "wind_speed": random.uniform(0, 20),  # Wind speed in m/s
                "wind_direction": random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"]),  # Direction
                "rain_level": random.uniform(0, 50),  # Rain level in mm
                "solar_radiation": random.uniform(200, 1000),  # Solar radiation in W/m²
            }
        # Add USB/WiFi data retrieval logic here
        return {
            "temperature": 25.0,
            "humidity": 50.0,
            "wind_speed": 10.0,
            "wind_direction": "N",
            "rain_level": 5.0,
            "solar_radiation": 800.0,
        }