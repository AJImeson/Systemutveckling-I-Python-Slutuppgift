import psutil
import time
import threading
import logging 
from datetime import datetime
from main.general_func import GeneralFunctions
from pathlib import Path


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
    
    def initialise_monitoring(self): # Starts monitoring by user in the background with threading 
      
        try:
            self.running = True
            self.thread = threading.Thread(target=self.monitor_running, daemon=True)
            self.thread.start()
            
        except Exception as e:
            return f"{RED}Failed to start monitoring thread: {e}{RESET}"
            
    def monitor_running(self, interval=2): # Function fetches system info 
        
        psutil.cpu_percent(interval=None) # Flag to set initial CPU percent reading to 0
        while self.running:
            
            try:
                self.cpu_usage = psutil.cpu_percent(interval=interval) # CPU Check
                self.ram_usage = psutil.virtual_memory().percent # RAM Check
                self.disk_usage = psutil.disk_usage('/').percent # Disk Usage
                self.timecheck = datetime.now().strftime("%H:%M:%S") # Shows time
                
            except Exception as e:
                self.running = False
                return f"{RED}Error during monitoring process: {e}{RESET}"
            
    def monitor_print(self): # Function prints current info 
        
        if self.timecheck is None:
            GeneralFunctions.clear_screen()
            return f"{RED}No monitoring history documented{RESET}\n{YELLOW}Press Ctrl + C to exit{RESET}"
        
        else:
            return f"{BLUE}CPU Usage:{RESET} {self.cpu_usage}% | {YELLOW}RAM Usage:{RESET} {self.ram_usage}% | {MAGENTA}Disk Usage:{RESET} {self.disk_usage}% | {self.timecheck}\n\nPress CTRL + C To exit back to main menu"
            
            
    def initialise_alerts(self): # Initialises alerts monitoring by user in the background with thread
        
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
        
        while self.alerts_running:
      
            try: 
                
                if not self.running: # Automatically stops alerts if monitoring is not active or running 
                    print(f"{RED}Monitoring not active{RESET}\n")
                    time.sleep(2)
                    continue
                
                self.print.alerts()
                time.sleep(2)
                
            except Exception as e:
                self.alerts_running = False
                return f"{RED}Error in alerts {e}{RESET}"
    
    def print_alerts(self): # Function to print alerts when called from main menu
        
        for levels, thresholds in self.alert.items():
            if not thresholds:
                continue
            attr_name = f"{levels.lower()}_usage"
            current = getattr(self, attr_name, None)
            if current is None:  
                continue
            exceeded = [t for t in thresholds if current >= t]
            if exceeded:
                lowest_exceeded = min(exceeded)
                print(f"{RED}[ALERT]{RESET} {levels} usage is at {current:.1f}% which exceeds {lowest_exceeded}%\n")
                print("Press CTRL + C to return to main menu ")
                
    def configure_alerts(self, alert_type, alert_threshold): # Configure alerts function called to main menu
                
        try:
            alert_threshold = float(alert_threshold) # Float converter/declaration 
        except ValueError:
            print(f"{RED}\nValue must be a number, press Enter to continue{RESET}")
            input() 
            return
            
        if not (0 <= alert_threshold <= 100): # Range limiter
            
            print(f"{RED}------------------------------------{RESET}")
            print(f"{RED}Threshold must be set between 1-100%{RESET}")
            print(f"{RED}------------------------------------{RESET}\n")
            input("Press Enter to continue ")
            return
            
        if alert_type in self.alerts:
            self.alerts[alert_type].append(alert_threshold) # Adds alert configuring to it's relevant key and list 
            print(f"Added Configured alert: {alert_type} at {alert_threshold}")
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
                
                # Colour coding for each alert type, as long as the key names are correct
                
                if alert_type == "CPU":
                    color = BLUE
                elif alert_type == "RAM":
                    color = YELLOW
                elif alert_type == "Disk":
                    color = MAGENTA
                else:
                    color = RESET
                    
                print(f"{color}{BOLD}{alert_type.upper()}{RESET}: ")
                    
                if thresholds:
                    lowest = min(thresholds) # Finds lowest alert configured for each type
                    for i, threshold in enumerate(thresholds, start=1): # Lists alerts within it's proper type/key
                        if threshold == lowest:
                            print(f"   [{i}] {threshold}%")
                        else:
                            print(f"   [{i}] {threshold}%")
                    
                else:
                    print(f"\n{RED}--------------------------------------{RESET}")
                    print(f"{RED}No alerts set\nPress Enter to continue{RESET}")
                    print(f"{RED}--------------------------------------{RESET}\n")
                    
        except Exception as e:
            return f"\nError printing alerts: {e}"
    
    
    def action_logger():
        
        logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('System Monitor started')
    pass 



# Colour codes for implementation
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[34m"
RESET = "\033[0m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"