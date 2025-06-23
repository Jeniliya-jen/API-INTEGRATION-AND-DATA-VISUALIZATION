# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: JENILIYA J

*INTERN ID*: CT04DG574

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

# API-INTEGRATION-AND-DATA-VISUALIZATION – CodTech Internship Task 1
This project is part of Task 1 for the CodTech Python Internship. The objective is to integrate a public API (OpenWeatherMap) into a Python script and generate a data visualization dashboard using libraries such as matplotlib or seaborn. This task demonstrates my ability to fetch, process, and visualize real-time data using industry-relevant tools, practices, and coding standards.

## Project Overview
This project uses the **OpenWeatherMap API** to fetch a 5-day weather forecast for a user-specified city. The data retrieved includes temperature and weather conditions for various timestamps throughout the coming days. Using this data, the script filters and displays one weather entry per day (usually the earliest forecast available), ensuring a simple and clear daily summary. The resulting data is then visualized using Python’s **matplotlib** library, showing temperature trends over the forecast period in the form of a plotted line graph.

The visualization helps users easily understand upcoming weather patterns, including temperature fluctuations and overall conditions, by converting numerical API data into an easy-to-read graph. This dashboard is useful for anyone needing a quick visual snapshot of the weather in their area or a city of interest.

## Features Implemented
1. **API Integration**: The script fetches real-time weather forecast data from OpenWeatherMap’s REST API using the requests library.

2.**User Interaction**: The user can input any city name, and the script will fetch and display the relevant forecast data.

3.**Data Processing**: The script filters raw API data to show only one entry per day, providing a concise summary.

4.**Data Visualization**: A clean and informative temperature vs. date graph is generated using matplotlib, enhancing readability and usefulness.

5.**Forecast Summary**: The script also prints a 5-day temperature forecast on the console in a user-friendly format.

## Technologies Used
-Python
-OpenWeatherMap API
-Matplotlib (for data visualization)
-Requests (for API handling)
-Dotenv (for environment variable handling)
-Pandas (for data manipulation and tabular structure)

## Visualization Dashboard
The chart is created using **Matplotlib** with the ggplot style. Each day's temperature is marked with a circular dot (marker='o') and the temperature value is displayed above the point. The x-axis represents the date, and the y-axis represents the temperature in Celsius. A legend is added, and the chart is grid-aligned for clarity.

## Deliverables
-Python script (main.py) for weather data fetching and plotting.
-.env file (excluded from GitHub using .gitignore).
-Visualization dashboard (Matplotlib plot).
-README documentation for better understanding.

## Conclusion
This project provided an insightful experience in integrating real-time data from the **OpenWeatherMap API** and visualizing it using Python libraries like **matplotlib** and **pandas**. The script effectively displays a five-day weather forecast based on user input, offering both a textual summary and a clear graphical dashboard. By handling data securely through environment variables and applying clean coding practices, I was able to build a reliable and informative tool. I am sincerely thankful to **CodTech** for offering this opportunity, which enhanced my practical skills in **API handling**, **Data processing**, and **Visualization**.

