import tkinter as tk
import time
import requests
print("WeatherAPI.com")


def getWeatherAPIdata(root):
    city = textField.get()
    api = "https://api.weatherapi.com/v1/current.json?key=42a3704fec7b4000b7733044220603&q="+city+"&aqi=no"
    json_data = requests.get(api).json()
    region = json_data['location']['region']
    country = json_data['location']['country']
    localTime = json_data['location']['localtime']
    condition = json_data['current']['condition']['text']
    temperature = json_data['current']['temp_c']
    humidity = json_data['current']['humidity']
    windSpeed = json_data['current']['wind_kph']
    finalInfo = "Region: "+str(region)+"\n"+"Country: "+str(country)+"\n"+"Temperature: "+str(temperature)+u"\N{DEGREE SIGN}C"+"\n"+"Condition: "+str(condition)
    finalData = "\n"+"Local Time in "+city.upper()+": "+str(localTime)+"\n"+"Humidity: "+str(humidity)+"\n"+"Wind Speed: "+str(windSpeed)+" kmph"
    label1.config(text=finalInfo)
    label2.config(text=finalData)


root = tk.Tk()
root.geometry("500x400")
root.title("Rohan's Weather Project from weatherapi.com")
root.columnconfigure(0, weight=1)

f = ("Helvetica", 15, "bold")
t = ("Helvetica", 25, "bold")

textField = tk.Entry(root, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeatherAPIdata)

label1 = tk.Label(root, font=t)
label1.pack()
label2 = tk.Label(root, font=f)
label2.pack()

root.mainloop()
