
import time #prettytable, terminalmenu, tkinter 
from main.general_func import GeneralFunctions   
from monitoring_and_alerts.monitoring_class import Monitor

functions = GeneralFunctions() # Object for General_Functions Class
monitor = Monitor() # Object for Monitor Class 

try:
    
    # Colour codes for implementation
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    MAGENTA = "\033[35m"
     
    while True: # Keeps loop alive until user inputs any exit command 
        
        # User Main Menu start up screen
        
        functions.clear_screen()
        print("------------------------------------") 
        print("Hardware Monitor | Select an option")
        print("------------------------------------\n")
        
        main_menu = input("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Quit Program\n").strip() # Strip trims and ensures proper input and "if not main_menu" can 
        
        if not main_menu:
            functions.clear_screen()
            print("--------------------------------------------------------------------------")
            print("Input cannot be any other options than the ones provided, please try again")
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
                        print(f"{GREEN}-----------------------{RESET}")
                        print(f"{GREEN}Monitoring started.....{RESET}")
                        print(f"{GREEN}-----------------------{RESET}\n")
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
                        
                        print(f"{YELLOW}----------------------------{RESET}")
                        print(f"{YELLOW}Choose an Alert to configure{RESET}")
                        print(f"{YELLOW}----------------------------{RESET}\n")
                        
                        try:
                            configure_menu = input(f"[1]{BLUE} CPU Usage{RESET}\n[2]{YELLOW} Memory Usage{RESET}\n[3] {MAGENTA}Disk Usage{RESET}\n[4] {RED}Exit to Main Menu{RESET}\n").strip()
                            
                            if not configure_menu:
                                print("Input cannot be any other options than the ones provided, please try again")
                                continue
                            
                            if configure_menu not in ("1", "2", "3", "4"):
                                print("Input must be between 1-4")
                                continue
                            
                        except ValueError:
                            print("Uknown error occured ")
                            input("Press Enter to continue")
                            continue
                        
                        match configure_menu:
                                
                            
                            case "1":
                                functions.clear_screen()
                                
                                alert_level = input(f"Set {BLUE}CPU{RESET} usage threshold in percentage\n")
                                monitor.configure_alerts("CPU", alert_level) # Calls configuring function
                                
                                    
                            case "2":
                                functions.clear_screen()
                                
                                alert_level = input(f"Set {YELLOW}RAM{RESET} usage threshold in percentage\n")
                                monitor.configure_alerts("RAM", alert_level) # Calls configuring function
                                
                                pass
                    
                            case "3":
                                functions.clear_screen()
                                
                                alert_level = input(f"Set {MAGENTA}Disk{RESET} usage threshold in percentage\n")
                                monitor.configure_alerts("Disk", alert_level) # Calls configuring function
                                pass 
                            
                            case "4": # End loop and return to Main Menu 
                                
                                functions.clear_screen()
                                print("-------------------------")
                                print("Exiting back to main menu")
                                print("-------------------------\n")
                                is_configuring_alerts = False                

                            case _:

                                print("Please choose a valid option ")
                        
                
                case "4": # Prints all configured alerts
                    functions.clear_screen()
                    
                    monitor.print_alert_list()
                    input("Press Enter to return to main menu ")
                
                case "5":# Starts monitoring mode that runs alerts in the background
                    functions.clear_screen()
                    
                    if monitor.alerts_running and monitor.running:
                        
                        if monitor.thread and monitor.thread.is_alive() and monitor.alerts_thread and monitor.alerts_thread.is_alive(): # Checks if both threads are alive and running before trying to start alerts process 
                            print(f"{YELLOW}----------------------------------{RESET}")
                            print(f"{YELLOW}Alerts and Monitoring already active{RESET}")
                            print(f"{YELLOW}----------------------------------{RESET}\n")
                            input("Press Enter to return to main menu ")
                    
                        else:
                            print(f"{RED}------------------------------------------{RESET}")
                            print(f"{RED}Unexpected stop of monitor/alerts{RESET} - {YELLOW}Restarting...{RESET}")
                            print(f"{RED}------------------------------------------{RESET}\n")
                            monitor.initialise_alerts()
                            input("Press Enter to return to main menu ")
                    
                    else:
                        monitor.initialise_alerts()
                        
                        input("Press Enter to return to main menu ")
                        pass
                
                case "6": # Closes the program 
                    print("Terminating Program....\n")
                    time.sleep(2)
                    print("Thank you for using")
                    break
                
                case _:
                    functions.clear_screen()
                    print("----------------------------------")
                    print("Invalid input - Choose between 1-6") # Default case
                    print("----------------------------------\n")
                    input("Press Enter to continue")
                    continue
                    
        except ValueError: # Error handling 
            print("Unknown error occured ")
            continue
        
except KeyboardInterrupt: # If user types ctrl + c during main menu loop the monitor thread is closed properly before exiting program 
    print("\nInteruppted by user...")
    if monitor.running:
        monitor.running = False
        if monitor.thread and monitor.thread.is_alive():
            monitor.thread.join(timeout=2)
    time.sleep(1)
    print("\nExiting session...")
    
    
    

# Colour codes for implementation
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[34m"
RESET = "\033[0m"
MAGENTA = "\033[35m"    
