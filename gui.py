import tkinter as tk
from tkinter import messagebox, filedialog, ttk, simpledialog, Toplevel
from weather_station import WeatherStation
from database import WeatherDatabase
from plot import plot_data
from datetime import datetime  # Removed `import datetime`
import requests

# Sponsor Class
class Sponsor:
    def show_sponsor_window(self):
        sponsor_root = Toplevel()
        sponsor_root.geometry("300x200")
        sponsor_root.title("Sponsor")

        title_label = tk.Label(sponsor_root, text="Support Us", font=("Arial", 16))
        title_label.pack(pady=10)

        def open_patreon():
            import webbrowser
            webbrowser.open("https://www.patreon.com/Nsfr750")

        def open_github():
            import webbrowser
            webbrowser.open("https://github.com/Nsfr750")

        def open_discord():
            import webbrowser
            webbrowser.open("https://discord.gg/q5Pcgrju")

        # Create and place buttons
        patreon_button = tk.Button(sponsor_root, text="Join the Patreon!", command=open_patreon)
        patreon_button.pack(pady=10)

        github_button = tk.Button(sponsor_root, text="GitHub", command=open_github)
        github_button.pack(pady=10)

        discord_button = tk.Button(sponsor_root, text="Discord", command=open_discord)
        discord_button.pack(pady=10)

        sponsor_root.mainloop()

class WeatherStationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Station Controller")
        self.root.geometry("300x400")

        self.weather_station = WeatherStation()
        self.database = WeatherDatabase()

        # Menus
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Data", command=self.load_data)
        file_menu.add_command(label="Save Data", command=self.save_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        sponsor_menu = tk.Menu(menu, tearoff=0)
        sponsor = Sponsor()
        sponsor_menu.add_command(label="Sponsor Us", command=sponsor.show_sponsor_window)
        help_menu.add_cascade(label="Sponsor", menu=sponsor_menu)

        # Controls
        self.mode_var = tk.StringVar(value="usb")
        tk.Label(root, text="Connection Mode:").pack()
        tk.Radiobutton(root, text="USB", variable=self.mode_var, value="usb").pack(anchor=tk.W)
        tk.Radiobutton(root, text="WiFi", variable=self.mode_var, value="wifi").pack(anchor=tk.W)
        tk.Radiobutton(root, text="Demo", variable=self.mode_var, value="demo").pack(anchor=tk.W)

        tk.Button(root, text="Connect", command=self.connect).pack()
        tk.Button(root, text="Get Data", command=self.get_data).pack()

        # Plot Format Dropdown
        tk.Label(root, text="Select Plot Format:").pack()
        self.plot_format_var = tk.StringVar(value="Line")
        plot_formats = ["Line", "Bar", "Scatter"]
        tk.OptionMenu(root, self.plot_format_var, *plot_formats).pack()

        tk.Button(root, text="Plot Data", command=self.plot_data).pack()

        self.status_label = tk.Label(root, text="Status: Disconnected", fg="red")
        self.status_label.pack()

    def connect(self):
        mode = self.mode_var.get()
        self.weather_station = WeatherStation(mode)
        status = self.weather_station.connect()
        self.status_label.config(text=f"Status: {status}", fg="green")

    def get_data(self):
        data = self.weather_station.get_data()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fixed the datetime usage
        self.database.save_data(
            timestamp,
            data["temperature"],
            data["humidity"],
            data["wind_speed"],
            data["wind_direction"],
            data["rain_level"],
            data["solar_radiation"],
        )
        messagebox.showinfo(
            "Data Retrieved",
            f"Temperature: {data['temperature']} °C\n"
            f"Humidity: {data['humidity']} %\n"
            f"Wind Speed: {data['wind_speed']} m/s\n"
            f"Wind Direction: {data['wind_direction']}\n"
            f"Rain Level: {data['rain_level']} mm\n"
            f"Solar Radiation: {data['solar_radiation']} W/m²",
        )

    def plot_data(self):
        data = self.database.retrieve_data()
        if data:
            plot_format = self.plot_format_var.get().lower()
            plot_data(data, plot_format)
        else:
            messagebox.showwarning("No Data", "No data available to plot.")

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Database Files", "*.db")])
        if file_path:
            self.database = WeatherDatabase(file_path)
            messagebox.showinfo("Load Data", "Data loaded successfully.")

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("Database Files", "*.db")])
        if file_path:
            with open(file_path, "wb") as f:
                f.write(self.database.connection.iterdump())
            messagebox.showinfo("Save Data", "Data saved successfully.")

    def show_about(self):
        messagebox.showinfo("About", "Weather Station Controller\nVersion 1.0.2")