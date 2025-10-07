
import time #prettytable, terminalmenu, tkinter 
from main.general_func import GeneralFunctions   
from monitoring_and_alerts.monitoring_class import Monitor

functions = GeneralFunctions() # Object for General_Functions Class
monitor = Monitor() # Object for Monitor Class 

try:
    
    while True: 
        
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        BLUE = "\033[34m"
        RESET = "\033[0m"
        MAGENTA = "\033[35m"
        
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
                            print("------------------------------------------")
                            print("Unexpected stop of monitor - Restarting...")
                            print("------------------------------------------\n")
                            monitor.initialise_monitoring()
                        
                        
                    else:
                        monitor.initialise_monitoring()
                        print("-----------------------")
                        print("Monitoring started.....")
                        print("-----------------------\n")
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
                                
                                alert_level = input("Set CPU usage threshold in percentage\n")
                                monitor.configure_alerts("CPU", alert_level) # Calls configuring function
                                
                                    
                            case "2":
                                functions.clear_screen()
                                
                                alert_level = input("Set RAM usage threshold in percentage\n")
                                monitor.configure_alerts("RAM", alert_level) # Calls configuring function
                                
                                pass
                    
                            case "3":
                                functions.clear_screen()
                                
                                alert_level = input("Set Disk usage threshold in percentage\n")
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
                        
                
                case "4":
                    functions.clear_screen()
                    monitor.print_alert_list()
                    input("Press Enter to return to main menu ")
                
                case "5":
                    functions.clear_screen()
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
    
    
    
    
