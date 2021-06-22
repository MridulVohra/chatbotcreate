import datetime
import pytz
import requests
import pandas as pd
import dataclasses
from bs4 import BeautifulSoup

def convert_datetime_timezone(dt, tz1, tz2):
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)
    dt = datetime.datetime.strptime(dt,"%d/%m/%Y %H:%M")
    dt = tz1.localize(dt)
    dt = dt.astimezone(tz2)
    dt = dt.strftime("%d-%m-%Y %H:%M")
    return dt

def retrive():
    url = "https://www.gdacs.org/xml/gdacs_cap.xml"
    header = {"user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) XX"}
    soup = BeautifulSoup(requests.get(url, headers=header).text, "html.parser")
    earth = soup.find_all("title")
    print(earth)

    country = []
    people = []
    magnitude = []
    time = []

    for i in earth:
        l = str(i).split(" ")
        l1 = str(i).split(",")
        l2 = l1[0].split("(")
        if len(l) > 10 and len(l1) > 2 and len(l2) > 1:
            l3 = l1[-2].split(" ")
            time.append(convert_datetime_timezone((l3[-3] + " " + l3[-2]), 'Etc/UTC', 'Asia/Kolkata') + " IST")
            magnitude.append(l2[1])
            people.append((l1[2].split("<"))[0])
            country.append(l[7])

    data = list(zip(country, magnitude, time, people))
    data = pd.DataFrame(data)
    data.columns = ["Country", "Magnitude", "Time", "People"]
    return (data)


