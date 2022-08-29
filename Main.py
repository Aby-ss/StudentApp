import os
import rich
import time
from rich.table import Table
from rich.progress import track
from rich.console import Console

import pandas as pd
from rich import print
from rich_tools import df_to_table

welcome_art = '''
███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║       ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║       ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                               
'''

print(welcome_art)

opt_art = '''

█   █▀▀ █ █ █▀█ █▀ █▀▀    █▄█ █▀█ █ █ █▀█   █▀█ █▀█ ▀█▀ █ █▀█ █▄ █    █
█   █▄▄ █▀█ █▄█ ▄█ ██▄     █  █▄█ █▄█ █▀▄   █▄█ █▀▀  █  █ █▄█ █ ▀█    █
█                                                                     █
'''

print(opt_art)

print('''
      1 |- Start Session -|
      2 |- Insert Time Table -|
      3 |- Event Reminder -|
      ''')

option = input("Choose your option : " )
option = int(option)

if (option == 1):
    workType = input("What are you doing, ie: studying, working out or cooking : ")
    session_Time = input("Choose a session time from 10m || 20m || 30m || 50m || : ")
    print("TUTORIAL  : Type '10' for a 10m session")
    
    session_Time = int(session_Time)
    
    
    if (session_Time == 10):
        for i in track(range(600), description= workType + " . . ."):
            time.sleep(1)
        
        print("Bye Bye ! 👍🏼")
            
    if (session_Time == 20):
        for i in track(range(1200), description= workType + " . . ."):
            time.sleep(1)
        
        print("Bye Bye ! 👍🏼")
            
    if (session_Time == 30):
        for i in track(range(1800), description= workType + " . . ."):
            time.sleep(1)
        
        print("Bye Bye ! 👍🏼")
    
    if (session_Time == 50):
        for i in track(range(3000), description= workType + " . . ."):
            time.sleep(1)
        
        print("Bye Bye ! 👍🏼")
        

if (option == 2):
    print("Create an excel sheet which houses the time table or any event planner ")
    print("Now save the file as .csv")
    file_Name = input("Enter the saved file's name : " )
    
    df = pd.read_csv(file_Name)
    table = df_to_table(df)
    print(table)
    
if (option == 3):
    event_art = '''
    ███████╗██╗   ██╗███████╗███╗   ██╗████████╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
    ██╔════╝██║   ██║██╔════╝████╗  ██║╚══██╔══╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
    █████╗  ██║   ██║█████╗  ██╔██╗ ██║   ██║       ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
    ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║       ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
    ███████╗ ╚████╔╝ ███████╗██║ ╚████║   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
    ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                  
    '''
    
    print(event_art)
    
    print('''Choose an option :
          
             1 |-- Set new Event --|
             2 |-- Check for upcoming events --|''')
    print(" ")
    
    event_option = int(input("Choose an option : "))
    
    if (event_option == 1):
        
        def write_list(fname, lines):
            with open(fname, "w") as fhandle:
                for line in lines:
                        fhandle.write(f'{line}\n')

            write_list('event_data.txt', [])

        new_event_art = '''
        ______    ____     _____     __  __ 
        |  ____|  / __ \   |  __ \   |  \/  |
        | |__    | |  | |  | |__) |  | \  / |
        |  __|   | |  | |  |  _  /   | |\/| |
        | |      | |__| |  | | \ \   | |  | |
        |_|       \____/   |_|  \_\  |_|  |_|
        '''
        print("Fill the form below to register an event :")
        print(" ")
        new_event_name = input("Event's name : ")
        new_event_date = input("Event's date in the 'Month/Date' [ie : 0821 - August/21st] format : " )

        f = open("event_data.txt", "a")
        f.write(new_event_date + " "  + new_event_name + "\n")
        f.close()

if (event_option == 2):
    with open('event_data.txt','r') as file:
        for line in file:
            event_date = line.split()[0]
            event_name = line.split()[1]
            print("Today is " + event_name + " at " + event_date)

            today = time.strftime('%m%d')

    if event_date == today:

        print("yes")


