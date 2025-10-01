import os 

class General_Functions: # General functions for menu and system
     
    @staticmethod
    def clear_screen(): # Clears screens at input
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def end_task(self, target): # Ends processes when called upon 
        target.running = False
        
    