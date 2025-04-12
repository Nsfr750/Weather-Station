import tkinter as tk
from gui import WeatherStationApp

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")  # Set the window size to 300x400
    app = WeatherStationApp(root)
    root.mainloop()