
import time
from monitoring_and_alerts.monitoring_class import Monitor
from main.general_func import GeneralFunctions

functions = GeneralFunctions() # Object for General_Functions Class
monitor = Monitor() # Object for Monitor Class 

def main():
    
    try:
        
        
        while True: # Keeps loop alive until user inputs any exit command 
            
            # User Main Menu start up screen
            
            functions.clear_screen()
            print("------------------------------------") 
            print(f"{YELLOW}Hardware Monitor{RESET} | {CYAN}Select an option{RESET}")
            print("------------------------------------\n")
            
            main_menu = input("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Quit Program\n").strip() # Strip trims and ensures proper input and "if not main_menu" can 
            
            if not main_menu:
                functions.clear_screen()
                print("--------------------------------------------------------------------------")
                print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
                print("--------------------------------------------------------------------------\n")
                input("Press Enter to continue")
                continue
            
            try:
            
                match main_menu:
                    
                    
                    case "1": # Start Monitoring 
                        functions.clear_screen()
                        
                        if monitor.running:
                        
                            if monitor.thread and monitor.thread.is_alive():
                                print("Monitor already running\n")
                                monitor.initialise_monitoring()
                            else:
                                print(f"{RED}------------------------------------------{RESET}")
                                print(f"{RED}Unexpected stop of monitor{RESET} - {YELLOW}Restarting...{RESET}")
                                print(f"{RED}------------------------------------------{RESET}\n")
                                monitor.initialise_monitoring()
                            
                            
                        else:
                            monitor.initialise_monitoring()
                            print(f"-------------------------")
                            print(f"{GREEN}Monitoring started.....{RESET}")
                            print(f"-------------------------\n")
                            time.sleep(1)
                            
                        input("Press enter to return to menu ")
                        
                    case "2": # Monitoring Activity
                        
                        try:
                            while True:
                                functions.clear_screen()
                                monitor.monitor_print()
                                time.sleep(2)
                        except KeyboardInterrupt:
                            print("\n")
                            
                    case "3": # Configure/add different alerts 
                    
                        is_configuring_alerts = True
                        while is_configuring_alerts:
                            functions.clear_screen()
                            
                            print(f"----------------------------")
                            print(f"{CYAN}Choose an Alert to configure{RESET}")
                            print(f"----------------------------\n")
                            
                            try:
                                configure_menu = input(f"[1]{BLUE} CPU Usage{RESET}\n[2]{YELLOW} Memory Usage{RESET}\n[3] {MAGENTA}Disk Usage{RESET}\n[4] {RED}Exit to Main Menu{RESET}\n").strip()
                                
                                if not configure_menu:
                                    print("--------------------------------------------------------------------------")
                                    print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
                                    print("--------------------------------------------------------------------------\n")
                                    continue
                                
                                if configure_menu not in ("1", "2", "3", "4"):
                                    print("Input must be between 1-4")
                                    continue
                                
                            except ValueError:
                                print("Uknown error occured ")
                                input("Press Enter to continue")
                                continue
                            
                            match configure_menu:
                                    
                                
                                case "1": # All options except exit to main menu calls configure method
                                    functions.clear_screen()
                                    
                                    alert_level = input(f"Set {BLUE}CPU{RESET} usage threshold in percentage\n")
                                    monitor.configure_alerts("CPU", alert_level) 
                                    
                                        
                                case "2":
                                    functions.clear_screen()
                                    
                                    alert_level = input(f"Set {YELLOW}RAM{RESET} usage threshold in percentage\n")
                                    monitor.configure_alerts("RAM", alert_level)
                                    
                                    pass
                        
                                case "3":
                                    functions.clear_screen()
                                    
                                    alert_level = input(f"Set {MAGENTA}Disk{RESET} usage threshold in percentage\n")
                                    monitor.configure_alerts("Disk", alert_level) 
                                    pass 
                                
                                case "4": # End loop and return to Main Menu 
                                    
                                    functions.clear_screen()
                                    print("-------------------------")
                                    print(f"{YELLOW}Exiting back to main menu{RESET}")
                                    print("-------------------------\n")
                                    is_configuring_alerts = False 
                                    time.sleep(1)               

                                case _: # Default case for invalid input
                                    functions.clear_screen()
                                    print("--------------------------------------------------------------------------")
                                    print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
                                    print("--------------------------------------------------------------------------\n")
                                    continue
                            
                    
                    case "4": # Prints all configured alerts
                        functions.clear_screen()
                        
                        monitor.print_configured_alerts()
                        input(f"{YELLOW}\nPress Enter to return to main menu{RESET} ")
                    
                    case "5":# Starts monitoring mode that runs alerts in the background
                        functions.clear_screen()
                        
                        if not monitor.running:
                            monitor.running = True
                            print(f"{GREEN}Starting monitoring process...{RESET}\n")

                        else:
                            print(f"{YELLOW}Monitoring already active...{RESET}\n")
                        
                        if not monitor.alerts_running:
                            monitor.initialise_alerts()
                            
                        else:
                            print(f"{YELLOW}Alerts already active...{RESET}\n")
                            
                            
                        input("Press Enter to return to main menu: ")
                    
                    case "6": # Closes the program 
                        functions.clear_screen()
                        print(f"\n{RED}Terminating Program....\n{RESET}")
                        time.sleep(2)
                        print(f"{YELLOW}Thank you for using{RESET}")
                        break
                    
                    case _: # Default case for invalid input
                        functions.clear_screen()
                        print("--------------------------------------------------------------------------")
                        print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
                        print("--------------------------------------------------------------------------\n")
                        input("Press Enter to continue: ")
                        continue
                        
            except ValueError: # Error handling 
                print("Unknown error occured ")
                continue
          
          
            # Colour codes for implementation
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        BLUE = "\033[34m"
        RESET = "\033[0m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        
    except KeyboardInterrupt: # If user types ctrl + c during main menu loop the monitor thread is closed properly before exiting program
        functions.clear_screen()
        print(f"\n{RED}Interuppted by user...{RESET}")
        if monitor.running:
            monitor.running = False
            if monitor.thread and monitor.thread.is_alive():
                monitor.thread.join(timeout=2)
        time.sleep(1)
        print(f"\n{YELLOW}Exiting session...{RESET}")
    
main()    
    

