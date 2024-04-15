import requests
import json
from datetime import datetime
from flask import Flask , render_template 

app = Flask(__name__)
dateLyouma=datetime.today().strftime("%Y-%m-%d")

url="https://api.open-meteo.com/v1/forecast?latitude=31,51&longitude=-9,77&hourly=temperature_2m&hourly=windspeed_10m&hourly=precipitation&hourly=cloud_cover&start_date="+dateLyouma+"&end_date="+dateLyouma

response=requests.get(url)
response=requests.get(url).content.decode('utf-8')
data = json.loads(response)

nomLyouma=datetime.today().strftime("%A")
jours={'Monday':'Lundi','Tuesday':'Mardi', 'Wednesday':'Mercredi',
'Thursday':'jeudi', 'Friday':'Vendredi', 'Sunday':'samedi' , 'Saturday':''}
lyouma1 = jours[nomLyouma]


def just3h(L) :
    L1 = []
    for i in range(0,len(L),3) :
        L1.append(L[i])
    return L1


DayTemperatures = data[0]["hourly"]["temperature_2m"]
DayWindspeed = data[0]["hourly"]["windspeed_10m"]
DayPrecipitation = data[0]["hourly"]["precipitation"]
Daycloud_cover = data[0]["hourly"]["cloud_cover"]

def getImages(Listecloud):
    images = []
    for c in Listecloud:
        if c < 20:
            images.append("sun.jpg")
        elif c < 60:
            images.append("sunetcloud.jpg")
        else:
            images.append("cloud.jpg")
    return images


ListeTemperature = just3h(DayTemperatures)
ListeWindspeed = just3h(DayWindspeed)
ListePrecipitation = just3h(DayPrecipitation)
ListeCloud_cover = just3h(Daycloud_cover)
listimages = getImages(ListeCloud_cover)

@app.route("/home")
def homepage():
    return render_template("home.html" , listimages =listimages ,ListeWindspeed =ListeWindspeed ,ListeCloud_cover=ListeCloud_cover)
@app.route("/")
def time():
    return render_template("meteo.html" ,date = dateLyouma , jour = lyouma1 ,ListeTemperatures = ListeTemperature , ListeWindspeed = ListeWindspeed , ListePrecipitation = ListePrecipitation , ListeCloud_cover = ListeCloud_cover , listimages = listimages )