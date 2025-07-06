# Weather App

A simple command-line application to fetch and display the current temperature for a given city using the OpenWeatherMap API.

## Features
- Fetches real-time weather data for any city
- Displays temperature in Celsius
- Handles API errors gracefully

## Requirements
- Python 3.7 or higher
- [OpenWeatherMap API key](https://openweathermap.org/api)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd weather-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application from the command line:

```bash
python weather_app.py
```

You will be prompted to enter a city name. The app will display the current temperature in Celsius.

## Docker

You can run the app in a Docker container:

1. **Build the Docker image:**
   ```bash
   docker build -t weather-app .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -it weather-app
   ```

## Configuration

- The API key is currently hardcoded in `weather_app.py`. For production use, consider using environment variables or a configuration file to store sensitive information.

## License

This project is licensed under the MIT License. 