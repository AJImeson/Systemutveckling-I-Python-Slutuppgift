

Dev Log

My Main principles with this project: Well structured, free fom errors, even when completed; I should be able to continue building and develop it

- 2023-09-24

  Read through the project specifics before any type of actual work in VS-Code
  Began this project by building a menu structure with "match" and "case" design in a main.py file, never wrote a pseudo code or made a flow chart. 


- 2025-09-25

  I've started constructing my code: Menu base and have outlined functions for Monitoring options. Central methods will be starting monitoring and also starting alert 
  Created a function with advice from AI about ternary expression, which is a compact if/else one line statement, used it to create a function for clearing the terminal at inputs

- 2025-09-29

  Updated my repo with separate folders per file function within the code and also created several .md files for documentation.
  I now have a main folder, here my main will be executed in its own file and also a seperate file with functions for the menu or general tasks within the program.
  The other folder will contain a file for my class (or classses depending on progression) where i will 
  

- 2025-09-30

  Experimented and started constructing some classes and functions which will be implemented in the main menu
  Ran into problems with <modules>. Occured due to root folder issues when trying to import classes and functions

  Managed to start the function that show current monitoring of the system. Will improve this 

  For some reason VS-Code is still not finding my Modules, spent a bit too much time handling this but i don't want to restructure or reorganise my code and its sub folders for only this reason
          Edit* 2025-10-02: Sorted this, at the time i didn't have the understanding of when running a file i have to be very specific with folders or they won't run properly. Learnt about the -m command and what it does 

- 2025-10-01 

  Constructed several functions within different classes that can be called upon each other depending on it's purpose. Try using parameters within functions rather than several 

- 2025-10-02

  Frustrating day when I'm not able to get anything to work the way i want it to. Double check how to call functions/methods within classes with tutor.
  For next work/project i construct i will definitely construct a flow chart for visual understanding and more clearer workflow 

- 2025-10-03

  Constructed a function for configuring alerts and saw to that they append into the dictionary declared in the __init__ function.

- 2025-10-06

  I have done a lot of editing in my functions for configuring alerts and also printing them.
  Finished both the function to add/configure alerts and the one to print them out.

- 2025-10-07

  Main goal for this day is to look at error handling of what I've constructed and coded so far before continuing constructing rest of the project. So far I've almost completed all the basic requirments.
  After constructing my automatic monitoring that will trigger alerts, I'll have a look at the function for logging all the results from the monitoring, might create separate class for this. 
  After working with error handling I decided to do some more graphical programming just to make the text more interesting in the terminal by using ANSI colour in the Python library

- 2025-10-08

  Before and after lecture i did more error handling for what I've constructed so far and this is what most of my day consisted of doing. Had a look at creating a @staticmethod function that can be reused for any type of process in the program regardless of its object

- 2025-10-09

  Todays goal is to create the process that starts automatic monitoring for the alerts and prints
  Quite big issues with VS-Code, when trying to run file on my laptop with Ubuntu i get module errors and can't test my program, no issue on my windows laptop for some reason. Spent most of my day trying to solve this with no luck or progress 

- 2025-10-10

  This day has mostly been error handling functions so that they print the correct message depending on input and menu choice

- 2025-10-10 

  More error handling and reused the logic in my printing_monitor to have the same type of output in my monitoring mode for alerts, original idea was to have alerts printing at the same time as using the menu but ended up being problematic since implementing a clear_screen() only erased everything and had a hard time working around it, so i'm pleased with the result for this.
  Did some graphical for colour coding my printing functions in the Alerts subclass during a "break" from actual coding, made a separate function for this for reusability in a possible future.
  Nested some more options in the program that has caused some more problems than i wanted to, it seems as in the starting processes with nested while loops in match structure, monitoring won't show any activity or alerts in the main loop. 

- 2025-10-14

  Cleaned up my code by making @staticmethods for printing messages and menus that were being reused several times in the code. I also made sub classes that will inherit from Monitor so that the code is more structured and organised after purpose of methods. 
  
- 2025-10-15 

  Restructured my program so that i can: Both start and stop Monitoring process with user input. So far constructed this for Monitoring, but since both Monitoring and Alerts are constructed with threading i should be able to use same logic for Alerts.
  Created a method for this using Event() class with threading which is a flag that initially sets to false. For this i needed a lot of AI to help understand the flow and code lines since it required several 'if', 'False' and 'True' to work properly through my logic and main function for the app.

- 2025-10-16

  Hard time 

- 2025-10-18 / 2025-10-19

  Had a few minutes over to polish my code and managed to get the thread for alerts to stop when called for

- 2025-10-21

  Finished my report/documentation for this project, will need some polishing before handing in and maybe add some thoughts I've accumulated the past two days

- 2025-10-22

  Made a logging function with "logging" library, kept simple and clean since It's a new concept for myself 
  As of this date my program and assignment is more or less completed the way i want it to function properly 