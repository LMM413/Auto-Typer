# Imports for UI
import tkinter as tk
import threading

# Imports for auto typer
import random as rd
import keyboard
import time
import csv

# Window setup and rules
root = tk.Tk()
root.title("Auto Typer V1.2")
root.geometry("650x567")
root.resizable(False, False)
root["bg"] = "#0e0e0e"

# Make the text for the hotkey entry box
hotkey_label = tk.Label(root, 
                        text='Start/Stop Hotkey',
                        anchor='center',
                        width=20,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
hotkey_label.place(x=400,y=15)

# Make the hotkey entry box
hotkey_entry=tk.Entry(root,
                highlightthickness=1,  
                width=10,
                highlightbackground="black",  
                highlightcolor="white",
                bg = "#2c2c2c",
                fg="#ffffff",
                font=("Arial", 9, "bold"))
# Assign it a location and starting text
hotkey_entry.place(x=425,y=38)
hotkey_entry.insert(tk.END, 'f2')

# Make the text for the error % entry box
hotkey_label = tk.Label(root, 
                        text=f"% Error Chance",
                        anchor='center',
                        width=20,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
hotkey_label.place(x=396,y=75)

# Make the error % entry
error_box = tk.Entry(root,
                        width=4,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
error_box.place(x=426   ,y=98)
error_box.insert(tk.END, '5')

# Make the status label over the save button
status_label = tk.Label(root, 
                        text='',
                        anchor='center',
                        width=40,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
status_label.place(x=390,y=485)

# Makes the save button
save_button = tk.Button(root, 
                       text='Save', 
                       width=20, 
                       # No command assigned, it is assigned lower down as the function it calls isn't defined yet
                       highlightthickness=1,  
                       highlightbackground="black",  
                       highlightcolor="white",
                       bg = "#2c2c2c",
                       activebackground="#008604",
                       fg="#ffffff",
                       font=("Arial", 9, "bold")) 
# Assign it a location
save_button.place(x=455, y=510)

# Make the large text entry
text_entry = tk.Text(root,  
                highlightthickness=1,  
                highlightbackground="black", 
                highlightcolor="white",
                fg="#d2d2d2",
                bg = "#1d1d1d",
                font=("Open Sans", 10, "bold"))  
# Assign in a location and starting text, set size so font changes dont affect it
text_entry.insert(tk.END, 'Enter text here...')
text_entry.place(x=0,y=0,height=567, width=405,)

# Variable and default value for font size dropdown
font_dropdown_choice = tk.StringVar(root)
font_dropdown_choice.set("Size")  # Default
# Make and place the font size dropdown
font_dropdown = tk.OptionMenu(root, font_dropdown_choice, 6, 8, 10, 12, 14, 16, 18)
font_dropdown.config(font=("Arial", 9, "bold"), bg="#2c2c2c", fg="#ffffff", width=2)
font_dropdown.place(x=345,y=0)
# Changes font size without changing window size
def change_font_size(*args):
    new_size = int(font_dropdown_choice.get())  # Get the selected font size
    new_font = ("Open Sans", new_size, "bold")  
    text_entry.config(font=new_font) 
font_dropdown_choice.trace_add("write", change_font_size)


# Converts the tsv file to a python dictionary where each key has a set of values for possible mistakes
def tsv_to_dict(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        data = {row[0]: row[1:] for row in reader}
    return data

# Used tsv file for holding key data based off position of the keyboard

file_path = 'Filepath to the relative_letters.tsv file' #CHANGE THIS

data_dict = tsv_to_dict(file_path)

# The list of all the letter strings that can be used in a mistake
mistake_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# The list of special characters that aren't seen as capital but still need shift
shift_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']
# A variable that tells the program when to pick new type speeds
rand_letter = 0
# Toggles when hokey is hit
can_start_type_loop = False
# Tests for if shift will be needed when typing
is_upper = False
# Default for the text entered
text = ""
# Default hotkey
hot_key = 'f2'  
# Used to override the status text if typing gets stopped
was_stopped = False
# Chance of an error in percent
error_chance = 5


# Flips between typing and not, if can type it updates the text and starts after 2s
def toggle_wait():
    global can_start_type_loop
    can_start_type_loop = not can_start_type_loop
    if can_start_type_loop:  
        update_text()
        status_label.config(text='Typing In Progress - UI Disabled')  
        root.title("Auto Typer V1.2 (Typing In Progress - UI Disabled)")
        root.after(2000, type_text)
# Sets default hotkey once
keyboard.add_hotkey(hot_key, toggle_wait)

# Updates the text variable with what the user entered
def update_text():
    global text
    text = str(text_entry.get("1.0", tk.END))

# Flashes an object a color for an amount of time before going back
def flash_color(object, color, og_color, time):
    object.config(bg=color)
    root.after(time, lambda: object.config(bg=og_color)) 

# Tries to update the error % with a number 0-10, if it cant it is set to 5
def update_error():
    global error_chance
    try:
        error_chance = int(error_box.get())
        flash_color(error_box, "#008604", "#2c2c2c", 1000)
        if not 0 <= error_chance <= 100:
            raise ValueError
    except ValueError:
        error_chance = 5
        error_box.delete(0, tk.END)
        error_box.insert(tk.END, '5')
        flash_color(error_box, "#860000", "#2c2c2c", 1000)

# if the hotkey is the same it does nothing, if it is different it updates it
def saveChanges():
    global hot_key, font_dropdown_choice
    new_hotkey = str(hotkey_entry.get())
    flash_color(hotkey_entry, "#008604", "#2c2c2c", 1000)
    status_label.config(text='Config Updated')
    update_error()
    new_font_size = int(font_dropdown_choice.get())
    change_font_size(new_font_size)

    if new_hotkey != hot_key:  
        keyboard.remove_hotkey(hot_key)  
        hot_key = new_hotkey  
        keyboard.add_hotkey(hot_key, toggle_wait)
# Adds this function ^ to the save button
save_button.config(command=saveChanges)


# Main typing function
def type_text():
    global is_upper, rand_letter, rand_range, rand_speed, can_start_type_loop, was_stopped, error_chance
    # Loops for each letter in the input string
    for i in text:
        # Kills the loop if the hotkey is pressed again
        if not can_start_type_loop:
            # Resets the toggle  variable so typing will start upon hotkey
            can_start_type_loop = False
            was_stopped = True
            break
            

        # Makes letter lowercase and notes if it needs to be uppercase when typed
        # Also notes if any special character will need shift to be typed
        if i.isupper() or i in shift_list:
            is_upper = True
            if i.isupper():
                i = i.lower()
                
        # 10% chance to wait 1s-10s at a period
        if rd.uniform(0, 1) < .1 and i == ".":
            time.sleep(rd.randint(1, 10))

        # 10% chance to wait 1s-10s at a space
        if rd.uniform(0, 1) < .1 and i == " ":
            time.sleep(rd.randint(1, 5))
        
        # 5% chance to mistype letter, 95% chance the letter is nearby and 5% chance it is random
        if rd.uniform(0, 1) < (error_chance / 100) and i != " " and i!= '\n' and i not in shift_list:
            # Makes the 95%-5% choice
            if rd.uniform(0, 1) < .95:
                mistake = "err"
                while mistake == "err":
                    mistake = rd.choice(data_dict[i])
            else: mistake = rd.choice(mistake_list)
            # Types and deletes the mistake
            keyboard.press_and_release(mistake)
            time.sleep(rd.uniform(.5, 1.2))
            keyboard.press_and_release('backspace')

        # Speed Control

        # Chooses the amount of affected letters and general speed they'll be typed at 
        if rand_letter == 0:
            rand_letter = rd.randint(1, 8)
            rand_range = rd.uniform(.1, .35)
        # Adds small variation per letter based off general speed
        rand_speed = rd.uniform((rand_range - .2), (rand_range + .1))
        # Prevents a letter ever being typed faster than .05s
        if rand_speed < .05:
            rand_speed = .05
        # Applies the work of this group
        time.sleep(rand_speed)

        # Special Characters

        # Converts Gdocs smart double quotes to normal ones
        if i == "“" or i == "”":
            time.sleep(.25)
            keyboard.press('shift')
            keyboard.press_and_release('\'')
            keyboard.release('shift')
        
        # Converts Gdocs smart single quotes to normal ones
        elif i == "‘" or i == "’":
            time.sleep(.25)
            keyboard.press_and_release('\'')

        # Types Letters    

        # Converts uppercase letters to lowercase then types them while holding shift
        # Is also set to be used if any special characters need shift
        elif is_upper:
            time.sleep(.25)
            keyboard.press('shift')
            keyboard.press_and_release(i)
            keyboard.release('shift')
        
        # Types lowercase letters
        else:
            keyboard.press_and_release(i)
        
        # Removes one from the tracking of the speed group 
        rand_letter -= 1
        # Resets flag for testing for uppercase letters
        is_upper = False
    
    # Decides if the typing completed or typing cancelled text is displayed
    if was_stopped:
        status_label.config(text='Typing Cancelled')
        was_stopped = False
    else:
        status_label.config(text='Typing Completed')
    
    # Resets window name
    root.title("Auto Typer V1.2")

    # Resets the toggle  variable so typing will start upon hotkey
    can_start_type_loop = False
    
    

# Main loop to continuously check the wait variable and type accordingly
def main_loop():
    root.after(100, main_loop)  # Keep checking for wait state


# Start the main loop
root.after(100, main_loop)

# Start the Tkinter main loop
root.mainloop()



"""
--------------------------------------
UPDATE NOTES V1.2 - V2.0
--------------------------------------
Shrunk overall UI size
Added a % fail entry box to UI
Added labels to the settings
renamed variables from cameltype to underscore spaces
Added colors upon saving and changed default hotkey to f1
Changed theme to dark
Added colors to indicate if a change was valid
Added font size dropdown
"""