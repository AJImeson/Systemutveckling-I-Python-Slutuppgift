import psutil, time, threading
from datetime import datetime
from main.general_func import GeneralFunctions



class Monitor: # Functions for monitoring tasks
    
    def __init__(self): # Initialisation of Constructor 
        self.cpu_usage = 0
        self.ram_usage = 0
        self.disk_usage = 0
        self.timecheck = None
        self.running = False
        self.alerts_running = False
        self.alerts_thread = None
        self.thread = None
        self.alerts = {"CPU":[], "RAM":[], "Disk":[]}
        
    
    def initialise_monitoring(self): # Starts monitoring by user in background
      
        try:
            self.running = True
            self.thread = threading.Thread(target=self.monitor_running, daemon=True)
            self.thread.start()
            print(f"{GREEN}Monitoring thread started{RESET}\n")
            
        except Exception as e:
            print(f"{RED}Failed to start monitoring thread: {e}{RESET}")
            
    def monitor_running(self, interval=2): # Function fetches system info 
        
        while self.running:
            
            try:
                self.cpu_usage = psutil.cpu_percent(interval=None) # CPU Check
                self.ram_usage = psutil.virtual_memory().percent # RAM Check
                self.disk_usage = psutil.disk_usage('/').percent # Disk Usage
                self.timecheck = datetime.now().strftime("%H:%M:%S") # Shows time
                
            except Exception as e:
                print(f"{RED}Error during monitoring process{RESET}")
                self.running = False 
            
    def monitor_print(self): # Function prints current info 
        
        if self.timecheck is None:
            GeneralFunctions.clear_screen()
            print(f"{RED}No monitoring history documented{RESET}\n{YELLOW}Press Ctrl + C to exit{RESET} ")
            return
        
        else:
            print(f"{BLUE}CPU Usage:{RESET} {self.cpu_usage}% | {YELLOW}RAM Usage:{RESET} {self.ram_usage}% | {MAGENTA}Disk Usage:{RESET} {self.disk_usage}% | {self.timecheck}\n\nPress CTRL + C To exit back to main menu")
            
            
    def initialise_alerts(self): # Initialises alerts monitoring in background
        
        try:
            if not self.alerts_running:
                self.alerts_running = True
                self.alerts_thread = threading.Thread(target=self.alerts_inspector, daemon=True)
                self.alerts_thread.start()
                
                print(f"{GREEN}--------------{RESET}")
                print(f"{GREEN}Alerts started{RESET}")
                print(f"{GREEN}--------------{RESET}\n")
                
            else:
                print(f"{YELLOW}------------------{RESET}")
                print(f"{YELLOW}Alerts already active{RESET}")
                print(f"{YELLOW}------------------{RESET}\n")
                
        except Exception as e:
            print(f"{RED}Failure during alerts process: {e}{RESET}")
            self.alerts_running = False
                
            
    
    def alerts_inspector(self): # Checks alerts configured and compares with current usage
        
        if not self.alerts_running:
            return
        
        while self.alerts_running:
      
            try: 
                
                if not self.running: # Automatically stops alerts if monitoring is not active or running 
                    print(f"{RED}Monitoring not active{RESET}\n")
                    return
                
                for levels, thresholds in self.alerts.items(): # Loops each key in dictionary 
                    
                    if not thresholds: # Passes if no alerts are configured
                        print(f"{YELLOW}No {levels} alerts configured{RESET}\n")
                        continue
                    
                attr_name = f"{levels.lower()}_usage"
                current = getattr(self, attr_name, None)
                
                if current is None: # Extra handling/error checking
                    print(f"{RED}Error retrieving {levels} usage{RESET}\n")
                    continue
                
                for threshold in thresholds:# Checks each threshold within the list of configured alerts
                    if current >= threshold:
                        print(f"{RED}ALERT! {levels} usage is at {current}% which exceeds the threshold of {threshold}%{RESET}\n")
                
                time.sleep(2) # Interval for checking alerts
                
            except Exception as e:
                print(f"{RED}Error in alerts {e}{RESET}")
                self.alerts_running = False
    
    def configure_alerts(self, alert_type, alert_threshold): # Configure alerts function called to main menu
        
        try:
            alert_threshold = float(alert_threshold) # Float converter/declaration 
        except ValueError:
            print("Value must be a number")
            
        if not (0 <= alert_threshold <= 100): # Range limiter
            
            print(f"{RED}------------------------------------{RESET}")
            print(f"{RED}Threshold must be set between 1-100%{RESET}")
            print(f"{RED}------------------------------------{RESET}\n")
            input("Press Enter to continue ")
            return
            
        if alert_type in self.alerts:
            self.alerts[alert_type].append(alert_threshold) # Adds alert configuring to it's relevant key and list 
            print(f"Added Configured alert: {alert_type} at {alert_threshold}")
            
        else:
            print(f"Error adding alert: {alert_type}")
            
    def print_configured_alerts(self): # Alert printing
    
        try:
            
            print(f"{YELLOW}----------------------------------{RESET}")
            print(f"{YELLOW}Currently added/configured alerts:{RESET}")
            print(f"{YELLOW}----------------------------------{RESET}\n")
            
            if not any (self.alerts.values()): # Checks if any alerts are configured
                print(f"{RED}--------------------{RESET}")
                print(f"{RED}No alerts configured{RESET}")
                print(f"{RED}--------------------{RESET}\n")
                input("Press Enter to continue ")
                return
            
            for alert_type, thresholds in self.alerts.items(): # Looks for relevant keys within the dictionary and prints type of alert
                print(f"{alert_type}: ")
                if thresholds:
                    for i, threshold in enumerate(thresholds, start=1): # Lists alerts within it's proper type/key 
                        print(f"   [{i}] {threshold}%")
                    
                else:
                    print(f"{RED}--------------------------------------{RESET}")
                    print(f"{RED}No alerts set\nPress Enter to continue{RESET}")
                    print(f"{RED}--------------------------------------{RESET}\n")
                    input("Press Enter to continue ")
                    
        except Exception as e:
            print(f"\nError printing alerts: {e}")
    
    




# Colour codes for implementation
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[34m"
RESET = "\033[0m"
MAGENTA = "\033[35m"