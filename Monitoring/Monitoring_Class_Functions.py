import psutil 
import threading
from datetime import datetime
from Main.General_Functions import General_Functions


class Monitor: # Functions for monitoring tasks
    
    def __init__(self):
        self.cpu_usage = 0
        self.ram_usage = 0
        self.disk_usage = 0
        self.timecheck = None
        self.running = False
        self.thread = None 
    
    def Initialise_Monitoring(self): # Starts monitoring by user in background
        
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.Monitor_Running, daemon=True)
            self.thread.start()
        pass
        
    def Monitor_Running(self):
        
        while self.running:
            self.cpu_usage = psutil.cpu_percent(interval=2) # CPU Check
            self.ram_usage = psutil.virtual_memory().percent # RAM Check
            self.disk_usage = psutil.disk_usage('/').percent # Disk Usage
            self.timecheck = datetime.now().strftime("%H:%M:%S") # Shows time 
            
    def Monitor_Print(self): # Prints latest value monitored 
        General_Functions.clear_screen(self)
        if self.timecheck is None:
            print("No monitoring has started as of yet")
            return
        
        print(f"CPU Usage: {self.cpu_usage}% | RAM Usage: {self.ram_usage}% | Disk Usage: {self.disk_usage}% | {self.timecheck}")
            
    
    def Monitoring_Mode(): # Automatic monitoring mode initialisation 
    
        pass
    
