import requests
from customtkinter import *



# from tkinter import *
# from tkinter import ttk

class WeatherApp:

    def __init__(self):
        app = CTk()
        app.geometry("500x400")
        set_appearance_mode("dark")
        self.btn = CTkButton(master=app, text="Check the weather", corner_radius=32,)
        self.btn.place(relx=0.5, rely=0.5, anchor="center")
        self.result_label = CTkLabel(master=app,text="Weather", font=("Arial", 20) )
        self.result_label.place(relx=0.4, rely=0.3, anchor="nw")
        self.entry = CTkEntry(master=app, placeholder_text="Type the place to check weather",width=300)
        self.entry.place(relx=.2, rely=.7, anchor="sw")
        app.mainloop()
    
    
    
    # def __init__(self):
    #     self.root = Tk()
    #     self.root.title("Weather App") # Need to set proper griding to make app look nice.
    #     mainframe = ttk.Frame(self.root, padding=(3, 3, 12, 12))
    #     mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    #     self.city_entry = ttk.Entry(mainframe)
    #     self.city_entry.grid(column=0, row=0, sticky=W)
    #     self.get_weather_button = ttk.Button(mainframe, text="Would you like to view the wather?",command=self.get_weather)
    #     self.get_weather_button.grid(column=0, row=1, sticky=W)
    #     self.result_label = ttk.Label(mainframe, text="Resut")
    #     self.result_label.grid(column=0, row=2, sticky=W)
    #     self.root.mainloop()
        
    # def get_weather(self):
    #     # city_name = self.city_entry.get()

    #     api_key = "9bc2274e2ab8379ec64b7e2d9adb233e"
    #     url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"

    #     response = requests.get(url)
    #     data = response.json()

    #     temperature = data["main"]["temp"]
    #     description = data["weather"][0]["description"]

    #     self.result_label.config(
    #         text=f"{city_name}: {temperature}°F, {description}"
    #     )

WeatherApp()
