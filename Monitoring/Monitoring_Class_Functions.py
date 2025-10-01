import psutil 
import time
from datetime import datetime
from Main.General_Functions import General_Functions


class Monitor: # Functions for monitoring tasks 
    
    def Initialise_Monitoring(self): # Starts monitoring by user 
    
        while True:
        
            cpu_usage = psutil.cpu_percent(interval=2) # CPU Check
            ram_usage = psutil.virtual_memory().percent # RAM Check
            disk_usage = psutil.disk_usage('/').percent # Disk Usage
            timecheck = datetime.now().strftime("%H:%M:%S")
            
            General_Functions.clear_screen()
            print(f"CPU Usage: {cpu_usage}% | RAM Usage: {ram_usage}% | Disk Usage: {disk_usage}% | {timecheck}")
            
    
    def Monitoring_Mode(): # Automatic monitoring mode initialisation 
    
        pass
    
