import matplotlib.pyplot as plt

def plot_data(data, plot_format="line"):
    timestamps = [row[1] for row in data]
    temperatures = [row[2] for row in data]
    humidities = [row[3] for row in data]
    wind_speeds = [row[4] for row in data]
    rain_levels = [row[6] for row in data]
    solar_radiations = [row[7] for row in data]

    plt.figure(figsize=(10, 5))
    if plot_format == "line":
        plt.plot(timestamps, temperatures, label="Temperature (°C)", color="red")
        plt.plot(timestamps, humidities, label="Humidity (%)", color="blue")
        plt.plot(timestamps, wind_speeds, label="Wind Speed (m/s)", color="green")
        plt.plot(timestamps, rain_levels, label="Rain Level (mm)", color="purple")
        plt.plot(timestamps, solar_radiations, label="Solar Radiation (W/m²)", color="orange")
    elif plot_format == "bar":
        width = 0.15  # Bar width
        plt.bar(timestamps, temperatures, width, label="Temperature (°C)", color="red", alpha=0.7)
        plt.bar(timestamps, humidities, width, label="Humidity (%)", color="blue", alpha=0.7)
        plt.bar(timestamps, wind_speeds, width, label="Wind Speed (m/s)", color="green", alpha=0.7)
        plt.bar(timestamps, rain_levels, width, label="Rain Level (mm)", color="purple", alpha=0.7)
        plt.bar(timestamps, solar_radiations, width, label="Solar Radiation (W/m²)", color="orange", alpha=0.7)
    elif plot_format == "scatter":
        plt.scatter(timestamps, temperatures, label="Temperature (°C)", color="red")
        plt.scatter(timestamps, humidities, label="Humidity (%)", color="blue")
        plt.scatter(timestamps, wind_speeds, label="Wind Speed (m/s)", color="green")
        plt.scatter(timestamps, rain_levels, label="Rain Level (mm)", color="purple")
        plt.scatter(timestamps, solar_radiations, label="Solar Radiation (W/m²)", color="orange")

    plt.xlabel("Timestamp")
    plt.ylabel("Values")
    plt.title("Weather Data")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate timestamps for better visibility
    plt.tight_layout()
    plt.show()