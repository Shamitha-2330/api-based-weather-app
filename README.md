# 🌦️ Weather App using OpenWeather API

A real-time weather application that fetches live weather data for any city using the OpenWeatherMap API.

---

## 🚀 Features

* 🌍 Search weather by city name
* 🌡️ Displays temperature and weather conditions
* 💨 Shows humidity, wind speed, and pressure
* 🖥️ Two implementations:

  * Flask Web Application (Dynamic UI)
  * HTML + JavaScript (Static Web Page)
* ⚡ Real-time API integration

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML, CSS, JavaScript
* OpenWeatherMap API

---

## 📂 Project Structure

```
Weather-App/
│
├── app.py                # Flask backend
│
├── templates/
│   └── index.html        # Flask frontend
│
├── Web_Page/
│   └── index.html        # Static HTML version
│
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/Shamitha-2330/api-based-weather-app.git
cd api-based-weather-app
```

---

### 2️⃣ Install dependencies

```
pip install flask requests
```

---

### 3️⃣ Run Flask App

```
python app.py
```

---

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 💻 Run HTML Version

Open directly in browser:

```
Web_Page/index.html
```

---

## 🔑 API Key Setup

Replace your API key in `app.py` and `index.html`:

```
API_KEY = "YOUR_API_KEY"
```

Get your API key from: https://openweathermap.org/api

---

## ⭐ Acknowledgements

* OpenWeatherMap API
* Flask Documentation
