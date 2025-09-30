import psutil 
import time 


class Monitor:
    
    def Initialise_Monitoring(): # Starts monitoring by user 
    
        while True:
        
            cpu_usage = psutil.cpu_percent(interval=2) # CPU Check
            ram_usage = psutil.virtual_memory().percent # RAM Check
            disk_usage = psutil.disk_usage('/').percent # Disk Usage 
    
            print(f"CPU Usage: {cpu_usage}% | RAM Usage: {ram_usage}% | Disk Usage: {disk_usage}%")
    
            time.sleep(2) # Interval check for total monitor 
            
    
    def Monitoring_Mode(): # Automatic monitoring mode initialisation 
    
        pass
    
