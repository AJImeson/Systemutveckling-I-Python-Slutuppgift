
import time
import logging
from monitoring_and_alerts.monitoring_class import MonitorSystem 
from main.functions import GeneralFunctions

functions = GeneralFunctions() # Object for General_Functions Class import 
monitor = MonitorSystem() # Object for Monitor Class and inheriting classes import 
alerts = monitor # Defining alerts as the same object, cleaner in main menu
 
def main():
    
    GeneralFunctions.system_log() # Initialises system log at program start up for documentation 
    logging.info('Program started')
    
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
            logging.info(f'User selected main menu option: {main_menu}')
            
            try:
            
                match main_menu:
                    
                    case "1": # Monitoring options
                        logging.info('User selected monitoring process options')
                        
                        is_choosing_monitoring_option = True
                        while is_choosing_monitoring_option:
                            functions.clear_screen()
                            
                            print("----------------")
                            print(f"{YELLOW}Choose An Option{RESET}")
                            print("----------------")
                            
                            try:
                                monitoring_menu = input(f"[1] - {GREEN}Start Monitoring Activity{RESET}\n[2] - {RED}End Monitoring Process{RESET}\n[3] - {YELLOW}Exit to Main menu{RESET}\n\n").strip()
                                logging.info(f'User selected monitoring menu option: {monitoring_menu}')
                                
                            except ValueError:
                                logging.error('ValueError occurred in monitoring menu selection')
                                print("Unknown error occured")
                                input("Press Enter to continue")
                                continue
                             
                            match monitoring_menu:
                                
                                case "1": # Start Monitoring
                                    
                                    logging.info('User selected to start monitoring activity')
                                    if monitor.monitoring_running:
                                        
                                        logging.warning('Attempted to start monitoring, but it is already running')
                                        if monitor.monitoring_thread and monitor.monitoring_thread.is_alive():
                                            functions.clear_screen()
                                            print(f"\n{CYAN}Monitor already running\n{RESET}")
                                            monitor.initialise_monitoring()
                                            
                                        else: # Remove or keep? 
                                            print(f"{RED}------------------------------------------{RESET}")
                                            print(f"{RED}Unexpected stop of Monitor{RESET} - {YELLOW}Restarting...{RESET}")
                                            print(f"{RED}------------------------------------------{RESET}\n")
                                            monitor.initialise_monitoring()
                                        
                                    else:
                                        logging.info('Starting monitoring activity')
                                        monitor.initialise_monitoring()
                                        functions.clear_screen()
                                        print(f"-------------------------")
                                        print(f"{GREEN}Monitoring started.....{RESET}")
                                        print(f"-------------------------\n")
                                        time.sleep(1)
                                        
                                    input(f"{YELLOW}Press enter to return to menu{RESET} ")
                                        
                                case "2": # End monitoring 
                                    functions.clear_screen()
                                    monitor_active = bool(monitor.monitoring_thread and monitor.monitoring_thread.is_alive()) # Checks monitoring thread status by first self(False) then if it's active for thread safety
                                    logging.info('User selected to end monitoring activity')
                                  
                                    if monitor_active or monitor.monitoring_running:
                                        monitor.monitor_stop(clear_monitor=True) # Calls the stop method from the monitoring class, 
                                        print("------------------------------")
                                        print(f"{GREEN}Monitoring Process Ended{RESET}")
                                        print("------------------------------\n")
                                        time.sleep(1)
                                        
                                    else:
                                        logging.error('Attempted to stop monitoring, process not running')
                                        functions.clear_screen()
                                        print(f"{RED}Monitoring Process not Running\n{RESET}")
                                    
                                    input(f"{YELLOW}Press Enter to return to Monitoring Options\n{RESET}")
                                    
                                case "3":
                                    logging.info('User exited monitoring menu to main menu')
                                    functions.clear_screen()
                                    functions.exit_sub_menu()
                                    is_choosing_monitoring_option = False
                                    time.sleep(1)
                                    
                                case _:
                                    logging.error('Invalid input in monitoring menu selection')
                                    functions.clear_screen()
                                    functions.default_case()
                                    continue
                                    
                    case "2": # Monitoring Activity
                        logging.info('User selected to view current monitoring activity')
                        if monitor.timecheck is None:
                            time.sleep(1)
                        
                        try:
                            while True:
                                functions.clear_screen()
                                print(monitor.monitor_print())
                                time.sleep(2)
                        except KeyboardInterrupt:
                            logging.info('User exited current monitoring activity view to main menu')
                            print("\n")
                            
                    case "3": # Configure/add different alerts 
                        logging.info('User selected to configure alerts')
                        is_configuring_alerts = True
                        while is_configuring_alerts:
                            functions.clear_screen()
                            
                            print(f"----------------------------")
                            print(f"{CYAN}Choose an Alert to configure{RESET}")
                            print(f"----------------------------\n")
                            
                            try:
                                alerts_configure_menu = input(f"[1] - {BLUE}CPU Usage{RESET}\n[2] - {YELLOW}Memory Usage{RESET}\n[3] - {MAGENTA}Disk Usage{RESET}\n[4] - {RED}Exit to Main Menu{RESET}\n\n").strip()
                                
                            except ValueError:
                                logging.error('ValueError occurred in configure alerts menu selection')
                                functions.value_error_print()
                                continue
                            
                            match alerts_configure_menu:
                                    
                                
                                case "1": # All options except exit to main menu calls configure method
                                    functions.clear_screen()
                                    logging.info('User selected to configure CPU alert')
                                    alert_level = input(f"Set {BLUE}CPU{RESET} usage threshold in percentage\n")
                                    alerts.configure_alerts("CPU", alert_level) 
                                    
                                case "2":
                                    functions.clear_screen()
                                    logging.info('User selected to configure RAM alert')
                                    alert_level = input(f"Set {YELLOW}RAM{RESET} usage threshold in percentage\n")
                                    alerts.configure_alerts("RAM", alert_level)
                                    
                                    pass
                        
                                case "3":
                                    functions.clear_screen()
                                    logging.info('User selected to configure Disk alert')
                                    alert_level = input(f"Set {MAGENTA}Disk{RESET} usage threshold in percentage\n")
                                    alerts.configure_alerts("Disk", alert_level) 
                                    pass 
                                
                                case "4": # End loop and return to Main Menu 
                                    logging.info('User exited configure alerts menu to main menu')
                                    functions.clear_screen()
                                    functions.exit_sub_menu()
                                    is_configuring_alerts = False 
                                    time.sleep(1)               

                                case _: # Default case for invalid input
                                    logging.error('Invalid input in configure alerts menu selection')
                                    functions.clear_screen()
                                    functions.default_case()
                                    continue
                            
                    case "4": # Prints all configured alerts by method call 
                        functions.clear_screen()
                        logging.info('User selected to view configured alerts')
                        
                        alerts.print_configured_alerts()
                        input(f"{YELLOW}\nPress Enter to return to main menu{RESET} ")
                    
                    case "5": # Alerts option for starting or ending processes 
                        
                        is_executing_alerts = True 
                        while is_executing_alerts:
                            functions.clear_screen()
                        
                            print(f"----------------------------")
                            print(f"{YELLOW}Choose an Alert Option{RESET}")
                            print(f"----------------------------\n")
                        
                            try:
                        
                                alerts_process_menu = input(f"[1] - {GREEN}Start Alerts Activity{RESET}\n[2] - {RED}End Alert Process{RESET}\n[3] - {YELLOW}Exit to Main menu{RESET}\n\n").strip()
                        
                            except ValueError:
                                logging.error('ValueError occurred in alerts process menu selection')
                                functions.value_error_print()
                                continue 
                        
                            match alerts_process_menu:
                        
                                case "1": # Start Alerts activity 
                                    functions.clear_screen()
                                    logging.info('User selected to start alerts activity')
                        
                                    if not monitor.monitoring_running: # Inspect if monitoring is active
                                        logging.warning('Attempted to start alerts without active monitoring process')
                                        functions.clear_screen()
                                        print(f"{RED}Monitoring not active{RESET}\n")
                                        input(f"{CYAN}Press Enter to return to main menu: {RESET}")
                                        continue
                                    
                                    if monitor.alerts_running and monitor.alerts_thread and monitor.alerts_thread.is_alive(): # Inspects if the alert thread is already running 
                                        functions.clear_screen()
                                        logging.info('Attempted to start alerts process although it is already running')
                                        print("-"*30)
                                        print(f"{YELLOW}Alerts activity already running{RESET}")
                                        print("-"*30)
                                        
                                    else:
                                        logging.info('Starting alerts activity')
                                        alerts.initialise_alerts() # Calls the initialise alerts method from Alerts sub class  
                                        time.sleep(1)
                                        print("-"*30)
                                        print(f"{GREEN}Alerts process started{RESET}")
                                        print(f"-"*30)
                                        time.sleep(2)
                                        
                                    input(f"\n{YELLOW}Press Enter to return to Alerts Options menu{RESET} ")
                                
                                case "2": # End Alerts process
                                    functions.clear_screen()
                                    logging.info('User selected to end alerts activity')
                                    alerts_active = bool(monitor.alerts_thread and monitor.alerts_thread.is_alive()) # Checks alerts thread status (False) then if it's active
                        
                                    if alerts_active and monitor.alerts_running:
                                        logging.info('Ending alerts activity')
                                        alerts.stop_alerts()
                                        print("-"*30)
                                        print(f"{GREEN}Alerts activity ended{RESET}")
                                        print("-"*30)
                                        time.sleep(2)
                        
                                    else:
                                        functions.clear_screen()
                                        logging.info('Attempted to stop alerts process although it is not running')
                                        print(f"{RED}Alerts activity not running{RESET}")
                                       
                                    input(f"\n{YELLOW}Press Enter to return to Alerts process menu{RESET} ")
                        
                                case "3": # Return to main menu
                                    logging.info('User exited alerts process menu to main menu')
                                    functions.clear_screen()
                                    functions.exit_sub_menu()
                                    is_executing_alerts = False
                                    time.sleep(1)
                                       
                                case _: # Default case for invalid input
                                    logging.error('Invalid input in alerts process menu selection')
                                    functions.clear_screen()
                                    functions.default_case()
                                    continue 
                        
                    case "6":
                        logging.info('User selected to view current alerts activity')
                        try:
                            while True:
                                functions.clear_screen()
                                alerts.print_alerts()
                                print(f"\n{YELLOW}Press CTRL + C To exit back to main menu{RESET}")
                                time.sleep(2)
                                 
                        except KeyboardInterrupt:
                            logging.info('User exited current alerts activity view to main menu')
                            print("\n")
                            
                    
                    case "7": # Closes the program
                        logging.info('User selected to quit program')
                        functions.clear_screen()
                        print(f"\n{RED}Terminating Program....\n{RESET}")
                        time.sleep(1)
                        print(f"{YELLOW}Thank you for using{RESET}")
                        break
                    
                    case _: # Default case for invalid input
                        functions.clear_screen()
                        functions.default_case()
                        continue
                       
            except ValueError: # Error handling
                logging.error('ValueError occurred in main menu selection')
                functions.value_error_print()
                continue
          
    except KeyboardInterrupt: # If user types ctrl + c during main menu loop the monitor thread is closed properly before exiting program
        logging.info('Program interrupted by user via KeyboardInterrupt')
        functions.clear_screen()
        print(f"\n{RED}Interuppted by user...{RESET}")
        if monitor.monitoring_running:
            monitor.monitoring_running = False
            if monitor.monitoring_thread and monitor.monitoring_thread.is_alive():
                monitor.monitoring_thread.join(timeout=2)
        time.sleep(1)
        print(f"\n{YELLOW}Exiting session...{RESET}")
    
main()    
    
