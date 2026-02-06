import requests
from tkinter import *
from tkinter import ttk

class WeatherApp:

    def __init__(self):
        self.root = Tk()
        self.root.title("Weather App") # Need to set proper griding to make app look nice.
        mainframe = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.city_entry = ttk.Entry(mainframe)
        self.city_entry.grid(column=20, row=10, sticky=W)
        self.get_weather_button = ttk.Button(mainframe, text="Would you like to view the wather?",command=self.get_weather)
        self.get_weather_button.grid(column=3, row=3, sticky=W)
        self.result_label = ttk.Label(mainframe, text="Resut")
        self.result_label.grid(column=50,row=2)
        self.root.mainloop()
        self.root = NoDefaultRoot()
        

    def get_weather(self):
        city_name = self.city_entry.get()
        self.result_label.config(text=city_name)
        print()



WeatherApp()