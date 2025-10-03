import psutil, time, threading
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
        self.alerts = {"CPU":[], "RAM":[], "Disk":[]}
        
    
    def initialise_monitoring(self): # Starts monitoring by user in background
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self.monitor_running, daemon=True)
        self.thread.start()
        
    def monitor_running(self, interval=2): # Function fetches system info 
        
        while self.running:
            self.cpu_usage = psutil.cpu_percent(interval=None) # CPU Check
            self.ram_usage = psutil.virtual_memory().percent # RAM Check
            self.disk_usage = psutil.disk_usage('/').percent # Disk Usage
            self.timecheck = datetime.now().strftime("%H:%M:%S") # Shows time
            time.sleep(interval)
            
    def monitor_print(self): # Function prints current info 
        
        if self.timecheck is None:
            GeneralFunctions.clear_screen()
            print("No monitoring history documented\nPress Ctrl + C to exit ")
            return
        
        else:
            print(f"CPU Usage: {self.cpu_usage}% | RAM Usage: {self.ram_usage}% | Disk Usage: {self.disk_usage}% | {self.timecheck}\n\nPress CTRL + C To exit")
        
    def configure_alerts(self, alert_type, alert_threshold): # Configure alerts function called to main menu
        
        try:
            alert_threshold = int(alert_threshold) # Int converter 
        except ValueError:
            print("Value must be a number")
            
        if not (0 <= alert_threshold <= 100):
            print("Threshold must be set between 1-100% ")
            
        if alert_type in self.alerts:
            self.alerts[alert_type].append(alert_threshold)
            print(f"Added Configured alert: {alert_type} at {alert_threshold}")
            
        else:
            print(f"Error adding alert: {alert_type}")
            
    def print_alert_list(self):
        
        print("Currently added/configured alerts: \n")
        for alert_type, thresholds in self.alerts.items():
            if thresholds:
                for i, t in enumerate(thresholds, start=1):
                    print(f"{alert_type} Alert {i}: {t}%")
                
                else:
                    print("No alerts set")
                    
                    pass 
    
    def alert_types():
        pass
    
    def monitoring_mode(): # Automatic monitoring mode initialisation 
        pass
    
