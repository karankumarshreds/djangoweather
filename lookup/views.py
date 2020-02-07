from django.shortcuts import render

#API LINK 
'''
http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=20002&distance=25&API_KEY=CB02EA06-D4B1-459D-9A3F-3005A8692D8D
'''
def home(request):
    import json
    import requests

    apiRequest = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=CB02EA06-D4B1-459D-9A3F-3005A8692D8D")

    try:
        api = json.loads(apiRequest.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api': api})
