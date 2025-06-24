# weather/views.py
import requests
from django.shortcuts import render

def get_weather(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'befe3d29f7fedcaec40025c653eeefa2'

        # Current weather API URL
        current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        # Forecast weather API URL
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

        # API Requests
        current_response = requests.get(current_url)
        forecast_response = requests.get(forecast_url)

        if current_response.status_code == 200 and forecast_response.status_code == 200:
            current_data = current_response.json()
            forecast_data = forecast_response.json()

            forecast_list = []
            for item in forecast_data['list'][:5]:  # Next 5 intervals (3-hourly)
                forecast_list.append({
                    'time': item['dt_txt'],
                    'temp': item['main']['temp'],
                    'description': item['weather'][0]['description']
                })

            weather_data = {
                'city': city,
                'temperature': current_data['main']['temp'],
                'humidity': current_data['main']['humidity'],
                'description': current_data['weather'][0]['description'],
                'icon': current_data['weather'][0]['icon'],
                'forecast': forecast_list
            }
        else:
            weather_data['error'] = 'City not found or API error.'

    return render(request, 'weather/weather.html', {'weather': weather_data})
