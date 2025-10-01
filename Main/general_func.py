import os 

class GeneralFunctions: # General functions for menu and system
     
    @staticmethod
    def clear_screen(): # Clears screens at input
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def end_task(): # Ends processes when called upon 
        running = False
        
    