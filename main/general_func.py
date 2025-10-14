import os
import time

monitor = None

def get_monitor(): # Function that delays import to avoid circular imports
    global monitor
    if monitor is None:
        from monitoring_and_alerts.monitoring_class import Monitor  # delayed import
        monitor = Monitor()
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
                        
        print("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Quit Program\n")
        return input("").strip() # Strip trims and ensures proper input
          
    
    @staticmethod
    def end_task(monitor): # Ends processes when called upon
       
        try: 
            confirm = input("Are you sure you wan to end all current running processes? (y/n): ").strip().lower()
            
            if confirm != 'y':
                print(f"{YELLOW}Ending all running processes...{RESET}")
                time.sleep(3)
                return
            
            for obj in monitor: # Ends all running threads by checking if they are active with '' flags in the method by use of a loop 
                if hasattr(obj, 'running') and obj.running:
                    obj.running = False
                if hasattr(obj, 'alerts_running') and obj.alerts_running:
                    obj.alerts_running = False
                    
        except Exception as e:
            print(f"{RED}Error ending tasks: {e}{RESET}")
            pass

        
# Colour codes for implementation 
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[34m"
RESET = "\033[0m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"