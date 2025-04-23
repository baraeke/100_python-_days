import time
import requests
from datetime import datetime, timezone
import smtplib

# === Configuration ===
MY_LAT = 4.664030
MY_LNG = 6.036987
my_email = "ifiemi2love@gmail.com"
my_password = "vctfeuwtenmagfoa"

CHECK_INTERVAL_SECONDS = 60

# === Parameters for Sunrise-Sunset API ===
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

# === Utility Function ===
def within_margin(actual, desired, margin):
    return desired - margin <= actual <= desired + margin

# === Main ISS Check Function ===
def iss_overhead_notifier():
    try:
        # Get sunrise/sunset data
        sas_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
        sas_response.raise_for_status()
        sas_data = sas_response.json()

        # Get ISS position data
        iss_response = requests.get("http://api.open-notify.org/iss-now.json")
        iss_response.raise_for_status()
        iss_data = iss_response.json()

        # Extract time values (all in UTC)
        sunrise_hour = int(sas_data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset_hour = int(sas_data["results"]["sunset"].split("T")[1].split(":")[0])
        current_hour = datetime.now(timezone.utc).hour

        # Get ISS location
        iss_latitude = float(iss_data["iss_position"]["latitude"])
        iss_longitude = float(iss_data["iss_position"]["longitude"])

        # Check if ISS is overhead and it's dark
        if (
            within_margin(iss_latitude, MY_LAT, 5) and
            within_margin(iss_longitude, MY_LNG, 5) and
            (current_hour >= sunset_hour or current_hour <= sunrise_hour)
        ):
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="eke0211@pg.babcock.edu.ng",
                    msg="Subject: ISS Overhead Notifier\n\nLook up! The ISS is overhead."
                )
            print("✅ Notification sent.")
        else:
            print("ℹ️ ISS not overhead or it's daytime.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

# === Run Check Periodically ===
while True:
    iss_overhead_notifier()
    time.sleep(CHECK_INTERVAL_SECONDS)
