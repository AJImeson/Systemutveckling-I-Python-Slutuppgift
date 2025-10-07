
import time #prettytable, terminalmenu, tkinter 
from main.general_func import GeneralFunctions   
from monitoring_and_alerts.monitoring_class import Monitor

functions = GeneralFunctions() # Object for General_Functions Class
monitor = Monitor() # Object for Monitor Class 

try:
    
    while True: 
        
        # User Main Menu start up screen
        
        functions.clear_screen()
        print("------------------------------------") 
        print("Hardware Monitor | Select an option")
        print("------------------------------------\n")
        
        main_menu = input("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Quit Program\n").strip() # Strip trims and ensures proper input and "if not main_menu" can 
        
        if not main_menu:
            print("Input cannot be any other options than the ones provided, please try again")
            continue
        
        try:
        
            match main_menu:
                
                
                case "1": # Start Monitoring 
                    functions.clear_screen()
                    
                    if monitor.running:
                    
                        if monitor.thread and monitor.thread.is_alive():
                            print("Unexpected stop, restarting")
                            monitor.initialise_monitoring()
                        else:
                            print("Unexpected stop of monitor - Restarting...")
                            monitor.initialise_monitoring()
                        
                        
                    else:
                        monitor.initialise_monitoring()
                        print("Monitoring started.....\n")
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
                        
                        print("----------------------------")
                        print("Choose an Alert to configure")
                        print("----------------------------\n")
                        
                        try:
                            configure_menu = input("[1] CPU Usage\n[2] Memory Usage\n[3] Disk Usage\n[4] Exit to Main Menu\n").strip()
                            
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
                                print("Exiting back to main menu ")
                                is_configuring_alerts = False                

                            case _:

                                print("Please choose a valid option ")
                        
                
                case "4":
                    functions.clear_screen()
                    
                    monitor.print_alert_list()
                    input("\nPress Enter to return to main menu")
                    
                        
                
                case "5":
                    functions.clear_screen()
                    pass
                
                case "6": # Closes the program 
                    print("Terminating Program....\n")
                    time.sleep(2)
                    print("Thank you for using")
                    break
                
                case _:
                    
                    print("Invalid input - Choose between 1-6 ") # Default case 
                    continue
                    
        except ValueError: # Error handling 
            print("Unknown error occured ")
            continue
        
except KeyboardInterrupt: # For more 
    print("\nInteruppted by user...")
    time.sleep(2)
    print("\Exiting session...")