import os
import time
import logging

monitor = None

def get_monitor(): # Function that delays import to avoid circular imports
    global monitor, alerts
    if monitor and alerts is None:
        from monitoring_and_alerts.monitoring_class import Monitoring, Alerts  # delayed import
        monitor = Monitoring()
        alerts = Alerts()
    return monitor

class GeneralFunctions: # General functions for menu and system
    
     
    @staticmethod
    def clear_screen(): # Clears screens at input
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_menu():
        GeneralFunctions.clear_screen()
        
        print("------------------------------------") 
        print(f"{YELLOW}Hardware Monitor{RESET} | {CYAN}Select an option{RESET}")
        print("------------------------------------\n")
                        
        print("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Stop Running Processes\n[7] Quit Program\n")
        return input("").strip() # Strip trims and ensures proper input
          
    
    @staticmethod
    def end_task(): # End process menu for main
       
        try:
            print("\nChoose one of the following processes :\n")
            print("[1] Stop Monitoring\n[2] Stop Alerts\n[3] Stop Both Processes\n[4] Exit to Main Menu\n")
            
            input_task = input("").strip()
            
            match input_task:
                
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass 
                case "4":
                    pass
        except ValueError: 
                   
            pass
        
    
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
CYAN = "\033[36m"