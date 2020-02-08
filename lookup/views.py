from django.shortcuts import render

#API LINK 
'''
http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=20002&distance=25&API_KEY=CB02EA06-D4B1-459D-9A3F-3005A8692D8D
'''
def home(request):
    import json
    import requests  
    
    if request.method == 'POST':

        zipcode = request.POST['zipcode']
        apiRequest = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=25&API_KEY=CB02EA06-D4B1-459D-9A3F-3005A8692D8D")
        try:
            api = json.loads(apiRequest.content)
        except Exception as e:
            api = "Error"
            
        if api[0]['Category']['Name'] == "Good":
            category_description = "Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif api[0]['Category']['Name'] == "Moderate":
                category_description = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                category_description = "Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
        elif api[0]['Category']['Name'] == "Unhealthy":
                category_description = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_description = "Health alert: everyone may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Hazardous":
                category_description = "Health warnings of emergency conditions. The entire population is more likely to be affected."
        return render(request, 'home.html', {'api': api, 'category_description': category_description})

    else:
        
        apiRequest = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94954&distance=25&API_KEY=CB02EA06-D4B1-459D-9A3F-3005A8692D8D")
        try:
            api = json.loads(apiRequest.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Health alert: everyone may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health warnings of emergency conditions. The entire population is more likely to be affected."
        return render(request, 'home.html', {'api': api, 'category_description': category_description})
