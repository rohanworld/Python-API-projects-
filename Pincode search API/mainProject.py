import requests
print("Pincode Search API Project \n")


def getData_via_Pincode(userInput):
    api = "https://api.postalpincode.in/pincode/"+userInput
    json_data = requests.get(api).json()
    data = json_data[0]['PostOffice'][0]
    for key, value in data.items():
        print(f"{key}: {value}")


def getData_via_Name(userInput):
    api = "https://api.postalpincode.in/postoffice/"+userInput
    json_data = requests.get(api).json()
    data = json_data[0]['PostOffice'][0]
    for key, value in data.items():
        print(f"{key}: {value}")


userInput = input("Search by Name or Pincode: ")
print()
if (userInput.isdigit()):
    getData_via_Pincode(userInput)
else:
    getData_via_Name(userInput)
