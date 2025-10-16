import os
import time 

class GeneralFunctions: # General functions for menu and system
    
     
    @staticmethod
    def clear_screen(): # Clears screens at input
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod   
    def print_menu():
        GeneralFunctions.clear_screen()
        
        print("-"*40) 
        print(f"{YELLOW}Hardware Monitor{RESET} | {YELLOW}Select an option{RESET}".center(40))
        print("-"*40)
                        
        print(f"[1] - Monitoring Process Options\n[2] - Show Current Monitoring Activity\n[3] - Configure Alerts\n[4] - Alert List\n[5] - Alert Process Options\n[6] - Quit Program\n")
        return input("").strip() # Strip trims and ensures proper input
    
    @staticmethod
    def default_case(): # Print message for main and sub menus in main()
        
        print("--------------------------------------------------------------------------")
        print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
        print("--------------------------------------------------------------------------\n")
        input("Press Enter to continue: ")
    
    @staticmethod
    def exit_sub_menu(): # Exits submenus to main menu print message
        print("-------------------------")
        print(f"{YELLOW}Exiting back to main menu{RESET}")
        print("-------------------------\n")
       
        
# Colour codes for implementation 

YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
