import requests
from customtkinter import *



# from tkinter import *
# from tkinter import ttk

class WeatherApp:

    def __init__(self):
        self.app = CTk()
        self.app.geometry("500x400")
        self.app.title("Weather App")

        set_appearance_mode("dark")

        # Makes the window resizable
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

        # Main frame
        self.frame = CTkFrame(master=self.app, fg_color="#423A8D")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Center contents inside frame
        self.frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Label
        self.result_label = CTkLabel(
            master=self.frame,
            text="Forecast",
            font=("Arial", 45)
        )
        self.result_label.grid(row=0, column=0, pady=20)

        # Entry
        self.city_entry = CTkEntry(
            master=self.frame,
            placeholder_text="Type the place to check weather",
            width=300
        )
        self.city_entry.grid(row=1, column=0, pady=10)

        # Button
        self.btn = CTkButton(
            master=self.frame,
            text="Check the weather",
            corner_radius=90,
            command=self.get_weather   
        )
        self.btn.grid(row=2, column=0, pady=20)

        self.app.mainloop()
        
    def get_weather(self):
        city_name = self.city_entry.get()

        api_key = "9bc2274e2ab8379ec64b7e2d9adb233e"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"

        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            self.result_label.configure(text="City not found, please try again")
            return
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        
        self.result_label.configure(
            text=f"The forecast for {city_name}: {temperature}°F, {description}"
        )

WeatherApp()


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
