import requests

def getSensors():
    url = "http://hendrickfs.pythonanywhere/sensors"
    response = requests.get(url)
    return response.json()

def postLog(sensorId, rfid):
    url = "http://hendrickfs.pythonanywhere/log"
    data = {
        "employee": rfid,
        "id": sensorId
    }
    response = requests.post(url, json=data)
    return response.json()
