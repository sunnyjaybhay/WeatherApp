# WeatherApp

WeatherApp is a Python-based weather application with a user authentication system and the ability to display real-time weather information. The app integrates OpenWeatherMap's API to fetch weather details for any city. Additionally, it includes user registration and login functionalities using a JSON-based database. This application also provides options to search for weather using either a city name or coordinates.

# Features:
Real-Time Weather Data: Get live weather information for a specific city including temperature, humidity, weather condition, sunrise and sunset times.
User Authentication: Users can register, log in, and save their login credentials securely in a JSON-based database (db.json).
Search by City or Coordinates: Users can search for weather details by city name or by geographic coordinates.
Database Integration: Stores user login information (email and password) in a db.json file. Passwords are stored securely as plain text for simplicity in this example (consider hashing passwords for production).
Simple GUI: A user-friendly graphical interface built with Tkinter for easy interaction.

# Files:
api.py: Contains the API client for interacting with OpenWeatherMap's API, responsible for fetching weather data based on city names.
app.py: The main application file that creates the GUI and manages user interactions (login, registration, searching for weather).
DataBase.py: Manages user authentication by checking login credentials and registering new users. The data is stored in a simple JSON file (db.json).
db.json: The file that stores user login information, including usernames and passwords (for this demo, passwords are stored as plain text).

# Technologies Used:
Python: Core programming language.
Tkinter: Used for creating the graphical user interface (GUI).
Requests: For making HTTP requests to the weather API.
JSON: Used to store user login data locally in db.json.
OpenWeatherMap API: Provides the weather data (requires an API key).

Login: Enter your registered email and password to log in.
Register: If you're not yet registered, you can sign up by providing a username, email, and password.
Search for Weather: Once logged in, you can search for weather by:
City name: Enter a city's name to view its weather details.
Coordinates: Enter latitude and longitude to search for weather based on geographic coordinates.
Logout: You can log out at any time to return to the login screen.

File Details:
api.py: Fetches weather information from OpenWeatherMap using the provided city name.
app.py: Manages the Tkinter GUI, user interaction (login, registration), and weather display logic.
DataBase.py: Handles the authentication system by checking and storing user details in db.json.

# To run the WeatherApp project on a new laptop, follow these steps:
Step-by-Step Instructions for Running WeatherApp on a New Laptop:
1. Install Python
Ensure that Python is installed on your laptop. WeatherApp requires Python to run.

Download Python from the official website: Python.org.
Run the installer and follow the prompts. Make sure to check the box to add Python to your system's PATH.
After installation, verify Python is installed by running this command in your terminal/command prompt:

bash
Copy code
python --version
2. Clone the Repository
To get the project files, clone the WeatherApp repository from GitHub to your local machine.

Open your terminal (Command Prompt, PowerShell, or any terminal of your choice).
Navigate to the directory where you want to store the project.
Run the following command to clone the repository:
bash
Copy code
git clone https://github.com/yourusername/WeatherApp.git
Replace yourusername with your actual GitHub username if the repository is personal.

Alternatively, if you don't have Git installed, you can download the ZIP version of the repository from GitHub and extract it.

3. Install Required Python Packages
WeatherApp requires some Python libraries. You need to install these dependencies using pip:

Navigate to the project directory (where the WeatherApp files are located).
Open the terminal/command prompt and run the following command:
bash
Copy code
pip install requests
You can add additional libraries if the project has other dependencies, but requests is the primary one for API communication.

4. Set Up OpenWeatherMap API Key
The WeatherApp fetches weather data from the OpenWeatherMap API. You will need an API key.

Go to OpenWeatherMap API and create a free account.
Once logged in, navigate to your API keys section and copy your API key.
Open the api.py file in the project folder.
Find the following line and replace "a70266fb86f93cb7d50d09dec44247bc" with your actual API key:
python
Copy code
self.api_key = "your_openweathermap_api_key"
5. Ensure Database (db.json) Exists
The project uses a db.json file to store user login information (email and password).

In the project folder, make sure the db.json file exists. If it doesn't, you can create an empty JSON file. A sample db.json file structure could look like this:

json
Copy code
{
  "user@example.com": ["username", "password"]
}
Alternatively, the app will create this file automatically the first time a user registers.

6. Run the WeatherApp
After setting up the API key and ensuring the required packages are installed, you can run the app.

Navigate to the project folder in the terminal/command prompt.
Run the following command:
bash
Copy code
python app.py
This will start the WeatherApp with a Tkinter GUI. You'll be presented with a login screen where you can either log in or register as a new user. Once logged in, you can search for weather by city name or coordinates.

7. Troubleshooting
If you encounter any issues, try the following:

Ensure that Python is added to your system's PATH.
Verify that you correctly installed all required dependencies (requests library).
Double-check your OpenWeatherMap API key and ensure it is correctly placed in api.py.
If any errors occur, read the error message to identify which part of the app is causing the issue and try to fix it.
Summary:
Install Python and Git (if not already installed).
Clone the WeatherApp repository from GitHub.
Install required Python packages (use pip install requests).
Set up your OpenWeatherMap API key in api.py.
Ensure db.json exists or will be created when the user registers.
Run app.py to launch the WeatherApp.
Once you follow these steps, the app should run on your new laptop without any issues. Enjoy using the WeatherApp!

Contributing:
Feel free to contribute by reporting issues or submitting pull requests. Improvements are welcome!
