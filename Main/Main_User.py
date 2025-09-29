from Monitoring import Monitoring_Mode, Initialise_Monitoring


print("---------------------------------")
print("Program menu | Select and option")
print("---------------------------------\n")

main_system_menu = input("[1] Commence Monitoring\n[2] Show Current Monitoring Activity\n[3] Configure Alerts\n[4] Alert List\n[5] Commence Monitoring Mode\n")

while True: 
    
    match main_system_menu:
        
        case "1":
            
            Initialise_Monitoring()
        
        case "2":
            pass
        
        case "3":
            
            while True:
                
                print("----------------------------")
                print("Choose an Alert to configure")
                print("----------------------------\n")
                
                configure_menu = input("[1] CPU Usage\n[2] Memory Usage\n[3] Disk Usage\n[4] Exit to Main Menu\n")
                
                
        
        case "4":
            
                Monitoring_Mode()
        
        case "5":
            pass 
    
    