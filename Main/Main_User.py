# from Monitoring import"
from Menu_Functions import clear_screen

print("---------------------------------")
print("Program menu | Select and option")
print("---------------------------------\n")

main_system_menu = input("[1] Start Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n[6] Quit Program\n")

while True: 
    clear_screen()
    try:
    
        match main_system_menu:
            
            case "1":
                clear_screen()
                pass
            
            case "2":
                clear_screen()
                pass 
            
            case "3":
                clear_screen()
                
                print("----------------------------")
                print("Choose an Alert to configure")
                print("----------------------------\n")
                    
                configure_menu = input("[1] CPU Usage\n[2] Memory Usage\n[3] Disk Usage\n[4] Exit to Main Menu\n")
                
                while True:
                    clear_screen()
                    
                    match configure_menu:
                            
                    
                        case "1":
                            pass
                                
                        case "2":
                            pass
                
                        case "3":
                            pass
                         
            
            case "4":
                clear_screen()
                pass 
                    
            
            case "5":
                clear_screen()
                pass
            
            case "6":
                print("Terminating Program....")
                print("Thank you for using")
                break
            
            case _:
                
                print("Invalid input - Choose between 1-6")
                continue
                
    except ValueError(Exception):
        print("Unknown error occured")
        continue 