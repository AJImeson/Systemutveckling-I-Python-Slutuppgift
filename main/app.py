
import time
from monitoring_and_alerts.monitoring_class import MonitorSystem 
from main.functions import GeneralFunctions

functions = GeneralFunctions() # Object for General_Functions Class
monitor = MonitorSystem() # Object for Monitor Class and inheriting classes
alerts = monitor # Defining alerts as the same object, cleaner in main menu
 
def main():
    
    try:
        
        # Colour codes for implementation
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        BLUE = "\033[34m"
        RESET = "\033[0m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        
        while True: # Keeps loop alive until user inputs any exit command 
            
            # User Main Menu start up screen
            
            main_menu = GeneralFunctions.print_menu()
            
            try:
            
                match main_menu:
                    
                    
                    case "1": # Monitoring options 
                        
                        is_choosing_monitoring_option = True
                        while is_choosing_monitoring_option:
                            functions.clear_screen()
                            
                            print("----------------")
                            print(f"{YELLOW}Choose An Option{RESET}")
                            print("----------------")
                            
                            try:
                                monitoring_menu = input(f"[1] - {GREEN}Start Monitoring Process{RESET}\n[2] - {RED}End Monitoring Process{RESET}\n[3] - {YELLOW}Exit to Main menu{RESET}\n").strip()
                            
                            except ValueError:
                                print("Unknown error occured")
                                input("Press Enter to continue")
                                continue
                             
                            match monitoring_menu:
                                
                                case "1": # Start Monitoring
                                    
                                    if monitor.monitoring_running:
                                    
                                        if monitor.monitoring_thread and monitor.monitoring_thread.is_alive():
                                            functions.clear_screen()
                                            print(f"\n{CYAN}Monitor already running\n{RESET}")
                                            monitor.initialise_monitoring()
                                        else:
                                            print(f"{RED}------------------------------------------{RESET}")
                                            print(f"{RED}Unexpected stop of monitor{RESET} - {YELLOW}Restarting...{RESET}")
                                            print(f"{RED}------------------------------------------{RESET}\n")
                                            monitor.initialise_monitoring()
                                        
                                        
                                    else:
                                        monitor.initialise_monitoring()
                                        functions.clear_screen()
                                        print(f"-------------------------")
                                        print(f"{GREEN}Monitoring started.....{RESET}")
                                        print(f"-------------------------\n")
                                        time.sleep(1)
                                        
                                    input("Press enter to return to menu ")
                                        
                                case "2": # End monitoring 
                                    
                                    if monitor.monitoring_running:
                                        functions.clear_screen()
                                        monitor.monitoring_running = False
                                        if monitor.monitoring_thread and monitor.monitoring_thread.is_alive():
                                            monitor.monitoring_thread.join(timeout=2)
                                            monitor.monitoring_thread = None
                                            
                                        print("------------------------------")
                                        print(f"{RED}Monitoring Process Ended{RESET}")
                                        print("------------------------------\n")
                                        time.sleep(2)
                                        
                                    else:
                                        functions.clear_screen()
                                        print(f"{YELLOW}Monitor Process not Running\n{RESET}")
                                    
                                    input(f"\n{YELLOW}Press Enter to return to Monitoring Options{RESET}")
                                    
                                    
                                case "3":
                                    functions.clear_screen()
                                    print("-------------------------")
                                    print(f"{YELLOW}Exiting back to main menu{RESET}")
                                    print("-------------------------\n")
                                    is_choosing_monitoring_option = False
                                    time.sleep(1)
                                    
                                case _:
                                    functions.clear_screen()
                                    print("--------------------------------------------------------------------------")
                                    print(f"{RED}Input cannot be any other options than the ones provided, please try again{RESET}")
                                    print("--------------------------------------------------------------------------\n")
                                    continue
                                    
                        
                    case "2": # Monitoring Activity
                        
                        if monitor.timecheck is None:
                            time.sleep(1)
                        
                        try:
                            while True:
                                functions.clear_screen()
                                print(monitor.monitor_print())
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
                                configure_menu = input(f"[1] - {BLUE}CPU Usage{RESET}\n[2] - {YELLOW}Memory Usage{RESET}\n[3] - {MAGENTA}Disk Usage{RESET}\n[4] - {RED}Exit to Main Menu{RESET}\n").strip()
                                
                                
                            except ValueError:
                                print("Uknown error occured ")
                                input("Press Enter to continue")
                                continue
                            
                            match configure_menu:
                                    
                                
                                case "1": # All options except exit to main menu calls configure method
                                    functions.clear_screen()
                                    
                                    alert_level = input(f"Set {BLUE}CPU{RESET} usage threshold in percentage\n")
                                    alerts.configure_alerts("CPU", alert_level) 
                                    
                                        
                                case "2":
                                    functions.clear_screen()
                                    
                                    alert_level = input(f"Set {YELLOW}RAM{RESET} usage threshold in percentage\n")
                                    alerts.configure_alerts("RAM", alert_level)
                                    
                                    pass
                        
                                case "3":
                                    functions.clear_screen()
                                    
                                    alert_level = input(f"Set {MAGENTA}Disk{RESET} usage threshold in percentage\n")
                                    alerts.configure_alerts("Disk", alert_level) 
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
                        
                        alerts.print_configured_alerts()
                        input(f"{YELLOW}\nPress Enter to return to main menu{RESET} ")
                    
                    case "5":# Starts monitoring mode that runs alerts in the background
                       
                        if not monitor.monitoring_running:
                            functions.clear_screen()
                            print(f"{RED}Monitoring not active{RESET}\n")
                            input(f"{CYAN}Press Enter to return to main menu: {RESET}")
                            continue

                        try:
                            while True:
                                functions.clear_screen()
                                alerts.print_alerts()
                                print(f"\n{YELLOW}Press CTRL + C To exit back to main menu{RESET}")
                                time.sleep(2)
                        except KeyboardInterrupt:
                            print("\n")
                            
                    
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
          
          
            
        
    except KeyboardInterrupt: # If user types ctrl + c during main menu loop the monitor thread is closed properly before exiting program
        functions.clear_screen()
        print(f"\n{RED}Interuppted by user...{RESET}")
        if monitor.monitoring_running:
            monitor.monitoring_running = False
            if monitor.monitoring_thread and monitor.monitoring_thread.is_alive():
                monitor.monitoring_thread.join(timeout=2)
        time.sleep(1)
        print(f"\n{YELLOW}Exiting session...{RESET}")
    
main()    
    

