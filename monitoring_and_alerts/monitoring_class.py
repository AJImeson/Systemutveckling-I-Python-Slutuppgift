import psutil
import time
import threading
import logging
from datetime import datetime
from main.functions import GeneralFunctions

class Monitor: # Base Monitor class
    
    def __init__(self): # Initialisation of Constructor
         
        self.cpu_usage = 0
        self.ram_usage = 0
        self.disk_usage = 0
        self.timecheck = None
        self.monitoring_running = False
        self.monitoring_thread = None
        self.monitoring_stop = threading.Event() # Class for managing objects in threading, used to stop the monitoring process when called upon in the method
        self.alerts_running = False
        self.alerts_thread = None
        self.alerts_stop = threading.Event() # Class for managing objects in threading, used to stop the alerts process when called upon in the method
        self.alerts = {"CPU":[], "RAM":[], "Disk":[]}
        
class Monitoring(Monitor): # Inherits from Monitor class and it's parameters; responsible for monitoring system info and initialisation
    
    def initialise_monitoring(self): # Starts monitoring by user in the background with threading 
      
        try:
            self.monitoring_stop.clear()
            self.monitoring_running = True
            self.monitoring_thread = threading.Thread(target=self.monitor_running, daemon=True)
            self.monitoring_thread.start()
            
        except Exception as e:
            return f"{RED}Failed to start monitoring thread: {e}{RESET}"
            
    def monitor_running(self, interval=2): # Function fetches system info
        
        psutil.cpu_percent(interval=None) # Flag to set initial CPU percent reading to 0
        while self.monitoring_running and not self.monitoring_stop.is_set(): # While loop that runs the monitoring process in the background
            
            try:
                self.cpu_usage = psutil.cpu_percent(interval=interval) # CPU Check
                self.ram_usage = psutil.virtual_memory().percent # RAM Check
                self.disk_usage = psutil.disk_usage('/').percent # Disk Usage
                self.timecheck = datetime.now().strftime("%H:%M:%S") # Shows time
                
            except Exception as e:
                self.monitoring_running = False
                return f"{RED}Error during monitoring process: {e}{RESET}"
            
    def monitor_print(self): # Function prints current info 
        
        if self.timecheck is None:
            GeneralFunctions.clear_screen()
            return f"{RED}No monitoring active{RESET}\n\n{YELLOW}Press Ctrl + C to exit{RESET}"
        
        else:
            return f"{BLUE}CPU Usage:{RESET} {self.cpu_usage}% | {YELLOW}RAM Usage:{RESET} {self.ram_usage}% | {MAGENTA}Disk Usage:{RESET} {self.disk_usage}% | {self.timecheck}\n\n{YELLOW}Press CTRL + C To exit back to main menu{RESET}"
        
    def monitor_stop(self,clear_monitor=False): # Stops monitoring process when called upon in the main menu
        
        if self.monitoring_running:
            self.monitoring_stop.set() # Sets the event flag to stop the monitoring thread
            self.monitoring_running = False
            m_t = self.monitoring_thread
            if m_t and m_t.is_alive():
                m_t.join(timeout=3) # Waits for the monitoring thread to finish
            self.monitoring_thread = None
        if clear_monitor: # Clears data if specified when called
            self.timecheck = None 
            self.cpu_usage = self.ram_usage = self.disk_usage = 0  
          
        
class Alerts(Monitor): # Inherits from Monitor class and it's parameters; responsible for alert configuration, initialisation and update         
           
    def alert_colour(self, alert_type): # Colour coding for reuse, looks for keys in the dictionary
        
        if alert_type == "CPU":
            return BLUE
        elif alert_type == "RAM":
            return YELLOW
        elif alert_type == "Disk":
            return MAGENTA
        else:
            return RESET
            
    def initialise_alerts(self): # Initialises alerts monitoring by user in the background with threading
        
        try:
            if not self.alerts_running:
                self.alerts_running = True
                self.alerts_stop.clear()
                self.alerts_thread = threading.Thread(target=self.alerts_inspector, daemon=True)
                self.alerts_thread.start()
                
                
        except Exception as e:
            print(f"{RED}Failure during alerts process: {e}{RESET}")
            self.alerts_running = False
                
    
    def alerts_inspector(self): # Checks alerts automatically in the background
        
        while self.alerts_running and not self.alerts_stop.is_set(): # Confirms flag is not set to stop the alerts thread
      
            try: 
                
                if not self.monitoring_running: # Automatically stops alerts if monitoring is not active or running 
                    print(f"{RED}Monitoring not active{RESET}\n")
                    if self.alerts_stop.wait(timeout=3):
                        continue
                
            except Exception as e:
                self.alerts_running = False
                return f"{RED}Error in alerts {e}{RESET}"
            
            
    def stop_alerts(self): # Stops alerts process when called upon in the main menu
        
        if self.alerts_running:
            self.alerts_stop.set() # Sets the event flag to stop the alerts thread
            self.alerts_running = False
            a_t = self.alerts_thread
            if a_t and a_t.is_alive():
                a_t.join() 
            self.alerts_thread = None
            self.alerts_running = False 
    
    def print_alerts(self): # Function to print alerts when called from main menu
        
        status = (
        f"{GREEN}Active{RESET}" 
        if (self.alerts_thread and self.alerts_thread.is_alive()) 
        else f"{RED}Inactive{RESET}"
        )
        print(f"Current Status: {status}\n")
        
        if not any (self.alerts.values()):
            GeneralFunctions.clear_screen()
            print(f"{RED}No alerts configured{RESET}\n")
        
        for key, thresholds in self.alerts.items(): # Loops through the dictionary keys and their relevant lists
            if not thresholds:
                continue
            
            colour = self.alert_colour(key) 
            attr_name = f"{key.lower()}_usage"
            current = getattr(self, attr_name, None) # Retrieves current usage value depending on which key is looped through 
            if current is None: 
                continue
            
            exceeded = [t for t in thresholds if current >= t] # List with a for loop that controls if usage exceeds any of the thresholds set in configured alerts 
            if exceeded:
                lowest_exceeded = min(exceeded)
                print(f"{RED}[ALERT]{RESET} | {colour}{key}: usage is at {RED}{current:.1f}%{RESET} which exceeds {CYAN}{lowest_exceeded}%{RESET}\n")
                
    def configure_alerts(self, alert_type, alert_threshold): # Configure alerts function called to main menu
                
        try:
            alert_threshold = float(alert_threshold) # Float converter/declaration 
        except ValueError:
            print(f"{RED}\nValue must be a valid number, press Enter to continue{RESET}")
            input() 
            return
            
        if not ( 1 < alert_threshold <= 100): # Range limiter
            
            print(f"{RED}------------------------------------{RESET}")
            print(f"{RED}Threshold must be set between 1-100%{RESET}")
            print(f"{RED}------------------------------------{RESET}\n")
            input("Press Enter to continue ")
            return
            
        if alert_type in self.alerts:
            self.alerts[alert_type].append(alert_threshold) # Adds alert configuring to it's relevant key and list
            GeneralFunctions.clear_screen() 
            print(f"{GREEN}Added Configured alert{RESET}: {alert_type} at {alert_threshold}")
            input(f"{YELLOW}\nPress Enter to return to alert configuration menu{RESET} ")
            return
            
        else:
            return f"Error adding alert: {alert_type}"
            
    def print_configured_alerts(self): # Alert printing
    
        try:
            
            print(f"{YELLOW}----------------------------------{RESET}")
            print(f"{YELLOW}Currently added/configured alerts:{RESET}")
            print(f"{YELLOW}----------------------------------{RESET}\n")
            
            if not any (self.alerts.values()): # Checks if any alerts are configured in a dictionary 
                print(f"{RED}--------------------{RESET}")
                print(f"{RED}No alerts configured{RESET}")
                print(f"{RED}--------------------{RESET}\n")
                return
            
            for alert_type, thresholds in self.alerts.items(): # Looks for relevant keys within the dictionary and prints type of alert
                
                colour = self.alert_colour(alert_type)
                    
                print(f"\n{colour}{BOLD}{alert_type.upper()}{RESET}: ") # Printing in uppercase for more emphasis in the terminal
                    
                if thresholds:
                    sorted_thresholds = sorted(thresholds) # Sorts thresholds in ascending order
                    lowest = sorted_thresholds[0] # Finds lowest alert configured for each type
                    for i, threshold in enumerate(sorted_thresholds, start=1): # Lists alerts within its proper type/key
                        if threshold == lowest:
                            print(f"\n\t{colour}[{i}] {threshold}%")
                        else:
                            print(f"\n\t{colour}[{i}] {threshold}%")
                else:
                    
                    print(f"\n{RED}No alerts set\n{RESET}")
                    
        except Exception as e:
            return f"\nError printing alerts: {e}"
   
        
class SystemLog(Monitor):
    
    def system_log():
        
        logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('System Monitor started')
    pass     
    
class MonitorSystem(Monitoring, Alerts): # Inherits from both Monitoring and Alerts class: Used as a bridge/flag for easier object managemnet in main 
    pass   

# Colour codes for implementation
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[34m"
RESET = "\033[0m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
CYAN = "\033[36m"