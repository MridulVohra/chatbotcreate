import requests
import string
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import data
disaster=data.retrive()
print (disaster)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'


@app.route('/')
def index_get():

    disaster_data = []
    coun=list(disaster.Country)
    mag=list(disaster.Magnitude)
    time=list(disaster.Time)
    peop=list(disaster.People)
    for i in range(len(coun)):
        data={
            "Country":coun[i],
            "Magnitude":mag[i],
            "Time":time[i],
            "People":peop[i]
        }
        disaster_data.append(data)

    return render_template('disaster.html', disaster_data=disaster_data)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False )