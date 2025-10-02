import psutil 
import threading
from datetime import datetime
from main.general_func import GeneralFunctions


class Monitor: # Functions for monitoring tasks
    
    def __init__(self):
        self.cpu_usage = 0
        self.ram_usage = 0
        self.disk_usage = 0
        self.timecheck = None
        self.running = False
        self.thread = None
        self.alerts = {"CPU":[5], "RAM":[5], "Disk":[5]}
    
    def initialise_monitoring(self): # Starts monitoring by user in background
        
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.monitor_running, daemon=True)
            self.thread.start()
        
    def monitor_running(self): # Function fetches system info 
        
        while self.running:
            self.cpu_usage = psutil.cpu_percent(interval=2) # CPU Check
            self.ram_usage = psutil.virtual_memory().percent # RAM Check
            self.disk_usage = psutil.disk_usage('/').percent # Disk Usage
            self.timecheck = datetime.now().strftime("%H:%M:%S") # Shows time 
            
    def monitor_print(self): # Prints latest value monitored 
        GeneralFunctions.clear_screen()
        if self.timecheck is None:
            print("No monitoring history documented\n")
            return
        
        print(f"CPU Usage: {self.cpu_usage}% | RAM Usage: {self.ram_usage}% | Disk Usage: {self.disk_usage}% | {self.timecheck}")
    
    def configure_alerts(self, alert_type, alert_threshold): # Configure alerts function 
        
        
        pass
    
    def alert_types():
        pass
    
    def monitoring_mode(): # Automatic monitoring mode initialisation 
        pass
    
