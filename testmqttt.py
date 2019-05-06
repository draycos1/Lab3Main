import time
global pillv
import json
import paho.mqtt.client as mqtt
import requests
import wiringpi
import requests
import datetime
from tkinter import *
degree_sign= u'\N{DEGREE SIGN}'

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='57338a25ecef449188e43149423bbdd5')

hunt_top_headlines = newsapi.get_top_headlines(
                                         
                                          category='sports',
                                        language='en',
                                          country='us')
rick_top_headlines = newsapi.get_top_headlines(
                                         
                                          category='technology',
                                        language='en',
                                          country='us')
cart_top_headlines = newsapi.get_top_headlines(
                                         
                                          category='business',
                                        language='en',
                                          country='us')
khizar_top_headlines = newsapi.get_top_headlines(
                                         
                                          category='entertainment',
                                        language='en',
                                          country='us')
default_top_headlines = newsapi.get_top_headlines(
                                         
                                          category='general',
                                        language='en',
                                          country='us')
                                         
hzip="76073"
czip="79707"
rzip="79416"
kzip="79406"
dzip="79401"
hhi=''
hlo=''
hc=''
rhi=''
rlo=''
rc=''
chi=''
clo=''
cc=''
khi=''
klo=''
kc=''
dhi=''
dlo=''
dc=''

def getweath(profile):
    global hhi
    global hlo
    global hc
    global rhi
    global rlo
    global rc
    global chi
    global clo
    global cc
    global khi
    global klo
    global kc
    global dhi
    global dlo
    global dc
    if profile=="Hunter":
          topic3.config(text=(("Current Temp: "+str(round(hc,1))+degree_sign)))
    elif profile=="Khizar":
          topic3.config(text=(("Current Temp: "+str(round(kc,1))+degree_sign)))
    elif profile=="Rick":
             topic3.config(text=(("Current Temp: "+str(round(rc,1))+degree_sign)))
    elif profile=="Carter":
             topic3.config(text=(("Current Temp: "+str(round(cc,1))+degree_sign)))
    elif profile=="Default":
             topic3.config(text=(("Current Temp: "+str(round(dc,1))+degree_sign)))
    print("done")
def getnews():
    global khizar_top_headlines
    global hunt_top_headlines
    global rick_top_headlines
    global cart_top_headlines
    global hnews
    global cnews
    global knews
    global dnews
    global rnews
    i=0
    hnews=(hunt_top_headlines['articles'][0]['title'])
    knews=(khizar_top_headlines['articles'][0]['title'])
    rnews=(rick_top_headlines['articles'][0]['title'])
    cnews=(cart_top_headlines['articles'][0]['title'])
def setnews(profile):
    global khizar_top_headlines
    global hunt_top_headlines
    global rick_top_headlines
    global cart_top_headlines
    global hnews
    global cnews
    global knews
    global dnews
    global rnews
    if profile=="Hunter":
        topic4.config(text=hnews)
    elif profile=="Khizar":
           topic4.config(text=knews)
    elif profile=="Rick":
            topic4.config(text=rnews)
    elif profile=="Carter":
            topic4.config(text=cnews)
    elif profile=="Default":
            print(hi)
    print(Ctemp+Htemp+Ltemp)
    
hnews=''
cnews=''
knews=''
dnews=''
rnews=''
redv=1
bluev=1
greenv=1
weatherv=0
remindersv=0
musicv=0
doorv='0'
Ctemp='0'
Htemp='0'
Ltemp='0'
hpill=0
cpill=0
kpill=0
rpill=0
hsettings=['0','0','0','0','000','000','000']
ksettings=['0','0','0','0','000','000','000']
rsettings=['0','0','0','0','000','000','000']
csettings=['0','0','0','0','000','000','000']
dsettings=['0','0','0','0','000','000','000']
tempset='a'
profilev="Default"
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyS0',9600)
now =datetime.datetime.now()
#topic2.config(text=now.strftime())
date=(now.strftime("%m-%d-%Y %H:%M"))
client =mqtt.Client()

def temperature(profile,zipcode):
    global hhi
    global hlo
    global hc
    global rhi
    global rlo
    global rc
    global chi
    global clo
    global cc
    global khi
    global klo
    global kc
    global dhi
    global dlo
    global dc
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=fb991b0f7a98e5e252c194912c41d4d9')
    a = r.json()
    temp_k = float(a['main']['temp'])
    temp_low = float(a['main']['temp_min'])
    temp_hi = float(a['main']['temp_max'])
    temp_f = (temp_k-273.15)*1.8+32
    temp_hif = (temp_hi-273.15)*1.8+32
    temp_lof = (temp_low-273.15)*1.8+32
    Ctemp=temp_f
    Htemp=temp_hif
    Ltemp=temp_lof
    if profile=="Hunter":
            hhi=Htemp
            hlo=Ltemp
            hc=Ctemp
    elif profile=="Khizar":
            khi=Htemp
            klo=Ltemp
            kc=Ctemp
    elif profile=="Rick":
            rhi=Htemp
            rlo=Ltemp
            rc=Ctemp
    elif profile=="Carter":
            chi=Htemp
            clo=Ltemp
            cc=Ctemp
    elif profile=="Default":
            dhi=Htemp
            dlo=Ltemp
            dc=Ctemp
    print(Ctemp+Htemp+Ltemp)
    
def on_connect(client, userdata, flags, rc):
    print ("Connected with result code "+ str(rc))
    client.subscribe("LEDCp")
    client.subscribe("Weatherp")
    client.subscribe("Remindersp")
    client.subscribe("Musicp")
    client.subscribe("Doorp")
    client.subscribe("profiles")
    client.subscribe("Settings")
    client.subscribe("Redp")
    client.subscribe("Greenp")
    client.subscribe("Bluep")
    client.subscribe("Pill")
    
def settingsdecode(setarray):
     global profilev
     global doorv
     global musicv
     global remindersv
     global weatherv
     global redv
     global bluev
     global greenb
     printsettings(profilev)
     doorv=setarray[0]
     weatherv=setarray[1]
     musicv=setarray[2]
     remindersv=setarray[3]
     redv=setarray[4]
     bluev=setarray[5]
     greenv=setarray[6]
     print(remindersv)
     if doorv=='1':
         topic5.config(text=("The Door is: Locked"))
         client.publish("Doorp","Locked")
     elif doorv=='0':
         topic5.config(text="The Door is: Unlocked")
         client.publish("Doorp","Unlocked")

     if weatherv=='1':
         print(weatherv)
         getweath(profilev)
         print('done')
     elif weatherv=='0':
         print(weatherv)
         topic3.config(text='')
         print('done')    
     if remindersv=='1':
         print(weatherv)
         setnews(profilev)
     elif remindersv=='0':
          topic4.config(text="")
     if profilev != "Default":
         topic6.config(text="Take Pills")
     if profilev=="Default":
         topic6.config(text="")
     #outputleds(redv,greenv,bluev)
     
def outputleds(R,G,B):
    print('hello')
    print(chr(int(R)))
    print(chr(int(G)))
    print(chr(int(B)))
    #Rq=R.endcode()
    print(((R)))
    print((G))
    print((B))
    wiringpi.serialPuts(serial,(chr(int(R))))
    wiringpi.serialPuts(serial,(chr(int(G))))
    wiringpi.serialPuts(serial,(chr(int(B))))
    print(R+G+B)
def printsettings(profile):
    global hsettings,csettings,ksettings,rsettings
    print(profile+"'s settings\n")
    if profile=="Hunter":
        print("Door Setting: ",hsettings[0])
        print("Weather Setting: ",hsettings[1])
        print("Music Setting: ",hsettings[2])
        print("Reminder Setting: ",hsettings[3])
        print("Red Setting: ",hsettings[4])
        print("Blue Setting: ",hsettings[5])
        print("Green Setting: ",hsettings[6])
            
    elif profile=="Khazir":
        print("Door Setting: ",ksettings[0])
        print("Weather Setting: ",ksettings[1])
        print("Music Setting: ",ksettings[2])
        print("Reminder Setting: ",ksettings[3])
        print("Red Setting: ",ksettings[4])
        print("Blue Setting: ",ksettings[5])
        print("Green Setting: ",ksettings[6])
           
    elif profile=="Rick":
        print("Door Setting: ",rsettings[0])
        print("Weather Setting: ",rsettings[1])
        print("Music Setting: ",rsettings[2])
        print("Reminder Setting: ",rsettings[3])
        print("Red Setting: ",rsettings[4])
        print("Blue Setting: ",rsettings[5])
        print("Green Setting: ",rsettings[6])    
    elif profile=="Carter":
        print("Door Setting: ",csettings[0])
        print("Weather Setting: ",csettings[1])
        print("Music Setting: ",csettings[2])
        print("Reminder Setting: ",csettings[3])
        print("Red Setting: ",csettings[4])
        print("Blue Setting: ",csettings[5])
        print("Green Setting: ",csettings[6])    
def settingupdate(profile,setstring):
    global hsettings,ksettings,csettings,rsettings
    print(profile)
    print(setstring)
    print(setstring[1])
    temparray=['0','0','0','0','000','000','000']
    temparray[0]=setstring[0]
    temparray[1]=setstring[1]
    temparray[2]=setstring[2]
    temparray[3]=setstring[3]
    temparray[4]=setstring[4:7]
    temparray[5]=setstring[7:10]
    temparray[6]=setstring[10:13]
    
    if profile=="Hunter":
            hsettings=temparray
            settingsdecode(hsettings)
    elif profile=="Khizar":
            ksettings=temparray
            settingsdecode(ksettings)
    elif profile=="Rick":
            rsettings=temparray
            settingsdecode(rsettings)
    elif profile=="Carter":
            csettings=temparray
            settingsdecode(csettings)
    print("done")
#client.publish("Doorp","Locked")
def on_message(client,userdata,msg):
    global ksettings
    global hsettings  
    global dsettings  
    global profilev
    global tempset
    global redv
    global bluev
    global greenv
    global weatherv
    global remindersv
    global musicv
    global doorv
    global pillv
    global date
    global now
    now =datetime.datetime.now()
    date=(now.strftime("%m-%d-%Y %H:%M"))
    topic2.config(text=date)
    msg.payload=msg.payload.decode('utf-8')
    print(msg.topic+" " +str(msg.payload))
    if msg.topic=='Doorp':
        doorv=msg.payload
        print(doorv)
        if msg.payload =='Locked':
            print('Door is currently Locked')
        elif msg.payload=='Unlocked':
            print('Door is unlocked')
        topic5.config(text=("The Door is: "+doorv))
    if msg.topic=='Musicp':
        if msg.payload =='On':
            print('Music is on')
        elif msg.payload=='Off':
            print('Music is off')
    if msg.topic=='Weatherp':
        weatherv=msg.payload
        if msg.payload =='On':
            print('Weather is on')
            getweath(profilev)
            print('it is workin')
            #topic3.config(text=('weather is '+weatherv))
        elif msg.payload=='Off':
            print('Weather is off')
            topic3.config(text=(''))
    if msg.topic=='Remindersp':
        remindersv=msg.payload
        if msg.payload =='On':
            setnews(profilev)
        else:
            print('Reminders is off')
            topic4.config(text=(''))
    if msg.topic=='profiles':
        profilev=msg.payload
        print(profilev+' has logged in')
        if profilev =='Default':
           topic1.config(text=("Please Log in"))
           topic6.config(text="")
        else:
            topic1.config(text=("Hello, " +profilev))
        if profilev=='Hunter':
            print(hsettings)
            settingsdecode(hsettings)
        elif profilev=="Khizar":
         settingsdecode(ksettings)
        elif profilev=="Default":
            settingsdecode(dsettings)
    if msg.topic=='Settings':
        tempset=msg.payload
        #print('current settings are-> '+tempset)
        settingupdate(profilev,tempset)
    if msg.topic=='Redp':
        redv=msg.payload
        print('Redl light value-> '+redv) 
        outputleds(redv,greenv,bluev)   
    if msg.topic=='Bluep':
        bluev=msg.payload
        print(' Blue light value-> '+bluev)
        outputleds(redv,greenv,bluev)
    if msg.topic=='Greenp':
        greenv=msg.payload
        print('Green light value-> '+greenv) 
        outputleds(redv,greenv,bluev)    
    if msg.topic=='Pill':
        pillv=msg.payload
        print(profilev+'s Pill is dispensing'+pillv)
        topic6.config(text="Pill Taken")
temperature('Hunter',hzip)
temperature('Khizar',kzip)
temperature('Carter',czip)
temperature('Default',dzip)
getnews()
print(hunt_top_headlines['articles'][0]['title'])
print('news done')
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost',1883,60)
client.loop_start()
print('Script is running, press Ctrl-c to quit...')





rootWindow = Tk()
rootWindow.title('MQTT monitor')
rootWindow.configure(background='black')
topic1 = Label(rootWindow, font = ('fixed', 13),fg="white",background="black")
topic1.grid( row = 2, column = 1, padx =75 , pady = 200)
topic2 = Label(rootWindow, font = ('fixed', 13),fg="white",background="black")
topic2.grid( row = 3, column = 1, padx = 75, pady = 200)
topic3 = Label(rootWindow, font = ('fixed', 13),fg="white",background="black")
topic3.grid( row = 1, column = 1, padx = 75, pady = 200)
topic4 = Label(rootWindow, font = ('fixed', 8),fg="white",background="black")
topic4.grid( row = 2, column = 2, padx = 75, pady = 200)
topic5 = Label(rootWindow, font = ('fixed', 13),fg="white",background="black")
topic5.grid( row = 3, column = 2, padx = 75, ipady = 200)
topic6 = Label(rootWindow, font = ('fixed', 13),fg="white",background="black")
topic6.grid( row = 1, column = 2, padx = 75, pady = 200)

print(hc)
#topic3.config(text=hc)
rootWindow.mainloop()
while True:
    print(hunt_top_headlines[0]['title'])
    #print(Ctemp+Htemp+Ltemp)
    dummy=input()
    
   
   
   
   
