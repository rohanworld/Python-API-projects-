import tkinter as tk
import time
import requests
print("Weather API Project")

# api.openweathermap.org/data/2.5/weather?q=london& appid=5d518b1fc808483f0e845d236683e817

def getWeatherAPIdata(root):
    city = textField.get() #takes user input in the textField area using .get method
    
    '''below is the api key and url we got using free api from the internet Always remeber to use HTTPS:// at first of the url'''

    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5d518b1fc808483f0e845d236683e817"
    # api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5d518b1fc808483f0e845d236683e817"
    json_data = requests.get(api).json()
    weather_condition = json_data['weather'][0]['main']
    # converting kelvin to celsius and also converting it into integer format
    temperature = int(json_data['main']['temp'] - 273.15)
    min_temperature = int(json_data['main']['temp_min'] - 273.15)
    max_temperature = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    #wind speed
    windSpeed = int(json_data['wind']['speed'])
    #converting seconds to hours and minutes  and to convert to 24 hour format replace I with H
    #here we also subtract our time zone i.e. 5:30
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-19800))

    #create a string to contain all the data
    finalInfo = weather_condition+"\n"+str(temperature)+u"\N{DEGREE SIGN}C"
    finalData = "\n"+"Max Temp: "+str(max_temperature)+"\n"+"Min Temp: "+str(min_temperature)+"\n"+"Pressure: "+str(pressure)+"\n"+"Humidity: "+"\n"+str(humidity)+"\n"+"Wind Speed: "+"\n"+str(windSpeed)+"\n"+"Sunrise: "+"\n"+sunrise+"\n"+"Sunset: "+"\n"+sunset
    label1.config(text=finalInfo)
    label2.config(text=finalData)

root = tk.Tk()
root.geometry("499x534")
root.title("Rohan's Weather Project")
root.columnconfigure(0, weight=1)

f= ("Helvetica", 15, "bold")
t= ("Helvetica", 35, "bold")

textField = tk.Entry(root, font = t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeatherAPIdata)

label1 = tk.Label(root, font=t)
label1.pack()
label2 = tk.Label(root, font=f)
label2.pack()

root.mainloop()