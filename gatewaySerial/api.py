import requests

base_url = "http://hendrickfs.pythonanywhere.com"
# base_url = "http://localhost:8000"



def getSensors():
    url = base_url+"/sensors/"
    response = requests.get(url)
    return response.json()

def getEmployee(rfid):
    url = base_url+"/employees/"+rfid+"/"
    response = requests.get(url)
    return response.json()

def postLog(sensorId, rfid):
    url = base_url+"/logs/"
    data = {
        "employee": rfid,
        "id": sensorId
    }
    response = requests.post(url, json=data)
    print(response)
    # return response.json()
