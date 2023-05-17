'''you can vist 'python made easy' on to get the code break down'''


#download and install all this libraries before importing
from tkinter import *
from tkinter import ttk
import phonenumbers
import opencage
import folium
from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import Nominatim
import tkintermapview

#set the tkinter interface and configure it
root = Tk()
root.overrideredirect(False)
root.resizable(False, False)

root.geometry("350x500")
root.config(bg="black")
#this label is not in use
lb_hb1 = Label(root, background="white")
lb_hb1.config(width="350", height="1")
#lb_hb1.place(x="1.8", y="")


#for the frame, down to lb1
board = Frame(root, background="lime", height="420", width="300")
board.place(x="25",y="50")

board = Frame(root, background="black", height="418", width="298")
board.place(x="26",y="51")

lb1 = Label(root, background="black",foreground= "lime", text="phone number->", height= 1)
lb1.place(x="4", y="20")

lb2 = Label(root, background="black",foreground= "lime", text="number should start with +", height= 1)
lb2.place(x="100", y="2")

#this is the entry point were you put your number and declare if its a string or integal
number = StringVar()
input_number = Entry(root, background="black",fg="lime", textvariable= number)
input_number.place(x="100", y="20", height="24", width="200")

#function consists of all the taxt and output labels and placing
def enter():
    from phonenumbers import geocoder

    number1 = number.get()
    print(number1)

    pepnumber = phonenumbers.parse(number1)
    location = geocoder.description_for_number(pepnumber, 'en')
    locate.config(text = location)

    #getting carrier name and label config
    from phonenumbers import carrier
    service_pro = phonenumbers.parse(number1)
    p = (carrier.name_for_number(service_pro, "en"))
    carrier = Label(root, background="black", foreground= "lime", text = p, width="12")
    carrier.place(x="180", y = "90")

    key = '29b635b61ce74406af220623f40af05f'

    geocoder = OpenCageGeocode(key) 
    query = str(location)
    results = geocoder.geocode(query)
    #print(results)

    #getting latitude and it label placement configuration
    lat = results[0]['geometry']['lat']
    print(lat)
    latl = Label(root, background="black", foreground= "lime", text = lat)
    latl.place(x="63", y = "120")

    #getting longitude and it label placement configuration
    lng = results[0]['geometry']['lng']
    print(lng)
    lngl = Label(root, background="black", foreground= "lime", text = lng)
    lngl.place(x="210", y = "120")
    

    #this part gets the map from lat and lng and saves it in your project file
    myMap = folium.Map(location = [lat, lng], zoom_start = 15)
    folium.Marker([lat, lng], popup = location).add_to(myMap)
    myMap.save("C:/Users/DAIRO/Documents/work/code/number_tracking/mylocation.html")

    #configuration for in app map view
    mapW = tkintermapview.TkinterMapView(root, width=280, height=250)
    mapW.set_position(lat, lng, marker=True)
    mapW.set_zoom(10)
    mapW.place(x="35", y="180")



#config for the enter button and it configuration
btn = Button(root,command=enter , background="black", foreground="lime", text= "enter", height="1", width="5")
btn.place(x="300", y="20")  


locate = Label(root, background="black", foreground= "lime", width="12")
locate.place(x="40", y = "90")


#not in use
def close():
    root.destroy()
    root.quit()
btnx = Button(root, text = 'x', command = close, height=1)
#btnx.place(x="335", y="")

root.mainloop()