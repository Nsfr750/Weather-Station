# Weather Station

## Overview
The Weather Station project is a Python-based application designed to monitor and control weather-related data. It provides real-time data acquisition, data visualization, and storage capabilities using a SQLite database.

## Features
- **Data Monitoring**: Retrieve real-time weather data, including temperature, humidity, wind speed, wind direction, rain level, and solar radiation.
- **Data Storage**: Save and load weather data to/from a local SQLite database.
- **Data Visualization**: Plot data in various formats such as line, bar, and scatter charts using interactive GUI.
- **Connection Modes**: Supports USB, WiFi, and Demo modes for flexibility in data acquisition.

## Project Structure
- `main.py` - Entry point of the application
- `weather_station.py` - Core weather station functionality
- `database.py` - Database operations and data management
- `gui.py` - Graphical user interface implementation
- `plot.py` - Data visualization and plotting functions

## Requirements
- Python 3.x
- SQLite3
- Python packages listed in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Nsfr750/Weather-Station.git
   cd Weather-Station
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the application:
   ```bash
   python3 main.py
   ```

2. Select your preferred connection mode (USB/WiFi/Demo)
3. The GUI will display real-time weather data and plotting options
4. Data is automatically saved to the SQLite database (`weather_data.db`)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Social Links
- [GitHub](https://github.com/sponsors/Nsfr750)
- [Patreon](https://www.patreon.com/Nsfr750)
- [Discord](https://discord.gg/BvvkUEP9)
- [Paypal](https://paypal.me/3dmega)