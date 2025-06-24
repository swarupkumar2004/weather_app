# weather_app
# 🌦️ Weather Forecast App

A simple Django web application that allows users to check the current weather of any city using the OpenWeatherMap API.

## 🚀 Features

- Search current weather by city name
- Displays temperature, humidity, and weather conditions
- Responsive UI using HTML and CSS
- Error handling for invalid city names

## 📸 Demo

![Screenshot](![Screenshot 2025-06-24 164330](https://github.com/user-attachments/assets/868af562-aead-4ac3-9960-bca46bf93dd2)
) 

## ⚙️ Technologies Used

- Python 3
- Django 5.2
- HTML/CSS
- OpenWeatherMap API

## 📂 Project Structure

```

weather\_project/
│
├── weather/                  # Django app
│   ├── templates/
│   │   └── weather/
│   │       └── weather.html  # HTML template
│   ├── views.py              # Logic for fetching and displaying weather
│   └── urls.py               # App routing
│
├── weather\_project/
│   └── urls.py               # Project-level URL routing
│
├── manage.py
├── requirements.txt
└── README.md

````

## 🔑 Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenWeatherMap API key in views.py:

   ```python
   api_key = 'befe3d29f7fedcaec40025c653eeefa2'
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```
```

