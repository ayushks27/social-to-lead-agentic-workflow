from datetime import datetime
import csv

def mock_lead_capture(name: str, email: str, platform: str):
    with open("leads.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), name, email, platform])

    print(f"Lead captured successfully: {name}, {email}, {platform}")
