
from Main.Menu_Functions import clear_screen
from Monitoring.Monitoring_Class_Functions import Monitor

while True: 
    
    # User Main Menu start up screen
     
    clear_screen()
    print("---------------------------------") 
    print("Program menu | Select and option")
    print("---------------------------------\n")
    
    main_system_menu = input("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Quit Program\n")
    try:
    
        match main_system_menu:
            
            case "1":
                clear_screen()
                Monitor.Initialise_Monitoring() 
                pass
            
            case "2":
                clear_screen()
                pass 
            
            case "3": # Configure different alerts 
               
                configure_menu_bool = True
                while configure_menu_bool:
                    
                    clear_screen()
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
                            pass
                                
                        case "2":
                            pass
                
                        case "3":
                            pass # User main screen
                        
                        case "4": # End loop and return to Main Menu 
                            
                            clear_screen()
                            print("Exiting back to main menu")
                            configure_menu_bool = False                

                        case _:

                            print("Please choose a valid option")
                    
            
            case "4":
                clear_screen()
                pass 
                    
            
            case "5":
                clear_screen()
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