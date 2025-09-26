# IoT Presence Register System

A comprehensive IoT-based employee presence tracking system using RFID cards and RF24 wireless communication modules. The system consists of distributed RFID sensors, a central communication hub, and a Django-based backend with REST API.

## 🏗️ System Architecture

```
┌─────────────┐    RF24     ┌──────────────┐    Serial    ┌─────────────────┐
│ RFID Nodes  │◄───────────►│ Central Node │◄────────────►│ Gateway/Backend │
│ (Arduino)   │   Wireless  │  (Arduino)   │      USB     │    (Python)     │
└─────────────┘             └──────────────┘              └─────────────────┘
      │                                                           │
      │                                                           │
   ┌──▼──┐                                                     ┌──▼──┐
   │RFID │                                                     │ API │
   │Card │                                                     │     │
   └─────┘                                                     └─────┘
```

### Components:
- **RFID Nodes**: Arduino-based sensors with RFID readers and RF24 transceivers
- **Central Node**: Arduino hub that collects data from RFID nodes via RF24
- **Gateway Serial**: Python application that processes serial data from central node
- **Backend**: Django REST API for data storage and management

## 📋 Features

- **Real-time RFID Detection**: Multiple distributed RFID sensor nodes
- **Wireless Communication**: RF24 modules for long-range wireless data transmission
- **Automatic IN/OUT Tracking**: Smart logic to determine employee entry/exit
- **REST API**: Full CRUD operations for employees, sensors, and logs
- **Web Interface**: Django admin panel for system management
- **Scalable Architecture**: Easy to add more sensor nodes
- **Employee Management**: RFID-based employee identification
- **Location Tracking**: Multiple sensor locations supported

## 🛠️ Hardware Requirements

### RFID Nodes
- Arduino (Uno/Nano/Pro Mini)
- MFRC522 RFID Module
- NRF24L01+ RF Module
- RFID Cards/Tags
- Power supply (3.3V/5V)

### Central Node
- Arduino (Uno/Nano/Pro Mini)
- NRF24L01+ RF Module
- USB connection to computer

### Gateway Computer
- Computer with USB port
- Python 3.8+
- Serial port access

## 📦 Software Requirements

### Backend Dependencies
```bash
Django==5.1.3
djangorestframework==3.15.2
pyserial==3.5
requests==2.32.3
```

### Arduino Libraries
- MFRC522
- RF24
- SPI

## 🚀 Installation & Setup

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend/iotBackend

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Load initial data (optional)
python manage.py loaddata rfidLog/fixtures/initialData.json

# Create superuser (optional)
python manage.py createsuperuser

# Start the Django server
python manage.py runserver
```

### 2. Hardware Setup

#### RFID Node Wiring
```
MFRC522    Arduino
VCC    ->  3.3V
RST    ->  D9
GND    ->  GND
MISO   ->  D12
MOSI   ->  D11
SCK    ->  D13
NSS    ->  D10

NRF24L01   Arduino
VCC    ->  3.3V
GND    ->  GND
CE     ->  D7
CSN    ->  D8
SCK    ->  D13
MOSI   ->  D11
MISO   ->  D12
```

#### Central Node Wiring
```
NRF24L01   Arduino
VCC    ->  3.3V
GND    ->  GND
CE     ->  D7
CSN    ->  D8
SCK    ->  D13
MOSI   ->  D11
MISO   ->  D12
```

### 3. Arduino Programming

1. Install required libraries in Arduino IDE:
   - MFRC522 by GithubCommunity
   - RF24 by TMRh20

2. Upload code to devices:
   - Upload `rfidNode/src/main/main.ino` to RFID sensor nodes
   - Upload `centralNode/src/main/main.ino` to central hub
   - Update node addresses in the code (myAddress variable)

### 4. Gateway Setup

```bash
# Navigate to gateway directory
cd gatewaySerial

# Update COM port in serialReader.py
# Update API base URL in api.py

# Run the gateway application
python main.py
```

## 🔧 Configuration

### Node Addresses
Each node must have a unique address:
- Node 01: `16`
- Node 02: `22`
- Central: `50`
- Add more nodes with unique IDs

### Serial Port Configuration
Update COM port in `gatewaySerial/serialReader.py`:
```python
ser = serial.Serial('COM5', 9600)  # Change COM5 to your port
```

### API Endpoint Configuration
Update base URL in `gatewaySerial/api.py`:
```python
base_url = "http://hendrickfs.pythonanywhere.com"  # Change to your server
# base_url = "http://localhost:8000"  # For local development
```

### Django Settings
Update `backend/iotBackend/iotBackend/settings.py`:
- Add your domain to `ALLOWED_HOSTS`
- Configure database settings
- Update secret key for production

## 📡 API Endpoints

### Employees
- `GET /employees/` - List all employees
- `GET /employees/{rfid}/` - Get employee by RFID
- `POST /employees/` - Create new employee
- `PUT /employees/{rfid}/` - Update employee
- `DELETE /employees/{rfid}/` - Delete employee

### Sensors
- `GET /sensors/` - List all sensors
- `GET /sensors/{id}/` - Get sensor by ID
- `POST /sensors/` - Create new sensor

### Logs
- `GET /logs/` - List all logs
- `GET /logs/employee/{rfid}/` - Get logs for specific employee
- `POST /logs/` - Create new log entry

### Log Entry Format
```json
{
  "employee": "12345678",
  "id": "16"
}
```

## 🗄️ Database Schema

### Employee Model
```python
class employee(models.Model):
    rfid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    icon = models.CharField(max_length=100, default="./assets/person.jpg")
```

### Sensor Model
```python
class sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
```

### RFID Log Model
```python
class rfidLog(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3)  # 'IN' or 'OUT'
    sensor = models.ForeignKey(sensor, on_delete=models.CASCADE)
```

## 🔄 Data Flow

1. **RFID Detection**: Employee scans RFID card at sensor node
2. **Local Processing**: Node processes card UID and packages data
3. **Wireless Transmission**: Data sent via RF24 to central node
4. **Serial Communication**: Central node forwards data via USB serial
5. **Gateway Processing**: Python gateway processes serial data
6. **API Call**: Gateway makes HTTP POST to Django backend
7. **Database Storage**: Log entry created with automatic IN/OUT detection
8. **Response**: Confirmation sent back through the chain


## 🔐 Security Considerations

- Change Django SECRET_KEY for production
- Use HTTPS for API communications
- Implement proper authentication for API endpoints
- Secure RFID cards against cloning
- Use encrypted communication for sensitive deployments

## 📈 Scaling the System

### Adding More Nodes
1. Program new Arduino with unique address
2. Add sensor entry to database
3. Deploy hardware at new location
4. System automatically handles new node data

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **HendrickFS** - *Initial work* - [HendrickFS](https://github.com/HendrickFS)

## 🙏 Acknowledgments

- MFRC522 library contributors
- RF24 library contributors
- Django and Django REST Framework teams
- Arduino community

---

*Last updated: September 2025*