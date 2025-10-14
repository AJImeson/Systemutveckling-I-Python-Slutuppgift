import os
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
        print(f"{BLUE}Hardware Monitor{RESET} | {PINK}Select an option{RESET}")
        print("------------------------------------\n")
                        
        print(f"{YELLOW}[1] - Monitoring Processes Options\n[2] - Show Current Monitoring Activity\n[3] - Configure Alerts\n[4] - Alert List\n[5] - Alerts Processes Options\n[6] - Quit Program\n{RESET}")
        return input("").strip() # Strip trims and ensures proper input
    
    def default_case(): # For reusability in main()
        
        print("--------------------------------------------------------------------------")
        print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
        print("--------------------------------------------------------------------------\n")
        input("Press Enter to continue: ")
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
PINK = "\033[95m"