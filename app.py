from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "Your_api_key_(Openweather API)"

def classify(condition):
    c = condition.lower()
    if "clear" in c:
        return "clear"
    if "rain" in c or "drizzle" in c:
        return "rain"
    if "snow" in c:
        return "snow"
    if "thunder" in c:
        return "thunder"
    if "cloud" in c or "mist" in c or "fog" in c or "haze" in c:
        return "clouds"
    return "clear"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    bg_class = "clear"
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            r = requests.get(url)
            try:
                data = r.json()
            except Exception:
                data = {}
            if r.status_code == 200 and "main" in data:
                condition = data["weather"][0]["main"]
                bg_class = classify(condition)
                weather = {
                    "city": data.get("name", city),
                    "temp": round(data["main"].get("temp", 0), 1),
                    "desc": data["weather"][0].get("description", "").title(),
                    "icon": data["weather"][0].get("icon")
                }
            else:
                weather = {"error": data.get("message", "Could not fetch weather")}
    return render_template("index.html", weather=weather, bg_class=bg_class)

if __name__ == "__main__":
    app.run(debug=True)
