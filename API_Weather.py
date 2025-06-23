# Import required libraries
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Securely fetch the API key

# Ask user for the city name
city = input("Enter the city name to get weather forecast: ")

# Build the API request URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

# Make the API request
response = requests.get(url)

# Check if request was successful
if response.status_code != 200:
    print("Something went wrong. Please check your city name or API key.")
    exit()

# Extract the data from the API response
data = response.json()
forecast_list = data["list"]

# Filter one forecast per day (every 24 hours)
filtered_data = []  # List to store daily forecasts
seen_dates = set()  # Set to track already added dates

for entry in forecast_list:
    time = datetime.fromtimestamp(entry["dt"])  # Convert timestamp to datetime
    date_only = time.date()  # Extract only the date

    # If data for this date hasn't been added yet
    if date_only not in seen_dates:
        seen_dates.add(date_only)  # Mark this date as seen
        temp = entry["main"]["temp"]  # Get temperature
        weather = entry["weather"][0]["main"]  # Get weather condition (e.g., Rain, Clouds)

        # Add the data to the list
        filtered_data.append({
            "Date": date_only,
            "Temperature": temp,
            "Weather": weather
        })

# Convert the list into a DataFrame
df = pd.DataFrame(filtered_data)

# Print a summary in the console
print("\n5-Day Forecast Summary:\n")
for row in df.itertuples():
    print(f"{row.Date}: {row.Temperature:.1f}°C - {row.Weather}")

# Plotting the temperature graph
plt.style.use('ggplot') # Use a clean and readable graph style
plt.figure(figsize=(10, 7)) # Set the size of the plot

# Plot temperature values with markers
plt.plot(df["Date"], df["Temperature"], marker='o', linestyle='-', color='tomato', label='Temperature (°C)')

# Add temperature values as labels above each data point
for i in range(len(df)):
    plt.text(df["Date"][i], df["Temperature"][i] + 0.5, f"{df['Temperature'][i]:.1f}°C", ha='center', fontsize=9)

# Set the title and axis labels with extra padding on the title
plt.title(f"Weather Forecast for {city}", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)

# Rotate x-axis dates for better readability
plt.xticks(rotation=45)

# Add grid and legend
plt.grid(True)
plt.legend()

# Adjust layout to avoid overlap
plt.tight_layout()
plt.subplots_adjust(top=0.9)  # Adds extra space

# Display final output
plt.show()




