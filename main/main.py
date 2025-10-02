
import time
from main.general_func import GeneralFunctions   
from monitoring_and_alerts.monitoring_class import Monitor

functions = GeneralFunctions() # Object for General_Functions Class
monitor = Monitor() # Object for Monitor Class 

while True: 
    
    # User Main Menu start up screen
     
    functions.clear_screen()
    print("---------------------------------") 
    print("Program menu | Select and option")
    print("---------------------------------\n")
    
    main_system_menu = input("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Quit Program\n")
    
    try:
    
        match main_system_menu:
            
            case "1": # Start Monitoring 
                functions.clear_screen()
                monitor.initialise_monitoring()
                print("Monitoring started...")
                input("Press enter to return to menu")
                            
            case "2": # Monitoring Activity 
                functions.clear_screen()
                
                while True:
                    functions.clear_screen()
                    monitor.monitor_print()
                        
                    choice = input("\nPress E to Return to menu").lower()
                    if choice == "E":
                        break
                    else:
                        print("Unknown command")
                        continue  
                    
            case "3": # Configure different alerts 
               
                is_configuring_alerts = True
                while is_configuring_alerts:
                    
                    functions.clear_screen()
                    print("----------------------------")
                    print("Choose an Alert to configure")
                    print("----------------------------\n")
                    
                    try:
                        configure_menu = input("[1] CPU Usage\n[2] Memory Usage\n[3] Disk Usage\n[4] Exit to Main Menu\n")
                    except ValueError:
                        print("Choose a valid option")
                        continue
                    
                    match configure_menu:
                            
                        
                        case "1":
                            
                            alert_level = input("Set CPU usge threshold percentage\n")
                            monitor.configure_alerts("CPU", alert_level)
                            
                                
                        case "2":
                            
                            alert_level = input("Set RAM usage threshold percentage\n")
                            monitor.configure_alerts("RAM", alert_level)
                            
                            pass
                
                        case "3":
                            
                            alert_level = input("Set Disk usage threshld\n")
                            monitor.configure_alerts("Disk", alert_level)
                            pass 
                        
                        case "4": # End loop and return to Main Menu 
                            
                            functions.clear_screen()
                            print("Exiting back to main menu")
                            configure_menu_bool = False                

                        case _:

                            print("Please choose a valid option")
                    
            
            case "4":
                functions.clear_screen()
                pass 
                    
            
            case "5":
                functions.clear_screen()
                pass
            
            case "6": # Closes the program 
                print("Terminating Program....")
                print("Thank you for using")
                break
            
            case _:
                
                print("Invalid input - Choose between 1-6") # Default case 
                continue
                
    except ValueError: # Error handling 
        print("Unknown error occured")
        continue 