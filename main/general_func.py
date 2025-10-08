import os
from monitoring_and_alerts.monitoring_class import Monitor

monitor = Monitor()

class GeneralFunctions: # General functions for menu and system
    
     
    @staticmethod
    def clear_screen(): # Clears screens at input
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def end_task(monitor): # Ends processes when called upon
        
        monitor.running = False
        monitor.alerts_running = False
        print(f"{RED}Process terminated...{RESET}")
        
        
# Colour codes for implementation 
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[34m"
RESET = "\033[0m"
MAGENTA = "\033[35m"