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
    
    @staticmethod   
    def print_menu():
        GeneralFunctions.clear_screen()
        
        print("------------------------------------") 
        print(f"{YELLOW}Hardware Monitor{RESET} | {YELLOW}Select an option{RESET}")
        print("------------------------------------\n")
                        
        print(f"[1] - Monitoring Process Options\n[2] - Show Current Monitoring Activity\n[3] - Configure Alerts\n[4] - Alert List\n[5] - Alert Process Options\n[6] - Quit Program\n")
        return input("").strip() # Strip trims and ensures proper input
    
    @staticmethod
    def default_case(): # For reusability in main()
        
        print("--------------------------------------------------------------------------")
        print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
        print("--------------------------------------------------------------------------\n")
        input("Press Enter to continue: ")
    
    @staticmethod
    def exit_sub_menu(): # Exits submenus to main menu
        print("-------------------------")
        print(f"{YELLOW}Exiting back to main menu{RESET}")
        print("-------------------------\n")
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