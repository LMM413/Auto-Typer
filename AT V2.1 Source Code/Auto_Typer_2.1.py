# Imports for UI
import tkinter as tk
import threading

# Imports for auto typer
import random as rd
import keyboard
import time
import csv
import math

# Imports for exe functionality 
import sys
import os

# Used to change the version name anywhere it appears
version = "V 2.1"

# Window setup and rules
root = tk.Tk()
root.title(f"Auto Typer {version}")
root.geometry("650x590")
root.resizable(False, False)
root["bg"] = "#0e0e0e"

"""This function is responsible for the displaying of tooltips, it takes in an activation event and tooltip
message, this function is called by the queue_tooltip function which adds a delay."""
def show_tooltip(event, message):
    global tooltip
    tooltip = tk.Toplevel(root)
    tooltip.wm_overrideredirect(True)  # Remove window borders
    tooltip.geometry(f"+{event.x_root+5}+{event.y_root+5}")  # Position near cursor
    label = tk.Label(tooltip, text=message, bg="lightgrey", font=("Arial", 8))
    label.pack()

""" This function hides the tooltip once the mouse leaves the activation area."""
def hide_tooltip(event):
    global tooltip
    if tooltip:
        tooltip.destroy()

""" This function delays the display of a tooltip to require .3s of continued hovering to activate it.
It also passes along the message argument."""
def queue_tooltip(event, message):
    root.after(300, show_tooltip(event, message))


#
# ↓ The follwing lines are responsible for creating UI and its function ↓
#


# Make the "Lucas Martin - 2025" label 
name_label = tk.Label(root, 
                        text='Lucas Martin - 2025',
                        anchor='center',
                        width=15,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 7))
name_label.place(x=557,y=574)

#
# Make ---General--- label
#
general_label = tk.Label(root, 
                        text=f"- - - - - - General - - - - - -",
                        anchor='center',
                        width=25,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 11, "bold"))
# Assign it a location
general_label.place(x=413, y=10)

# Make the text for the hotkey entry box
hotkey_label = tk.Label(root, 
                        text='Start/Stop Hotkey',
                        anchor='center',
                        width=14,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
hotkey_label.place(x=427, y=35)
# Assign its tooltip
hotkey_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The hotkey used to start and \n stop the typing simulation. \n Example: ctrl+s"))
hotkey_label.bind("<Leave>", hide_tooltip)

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
hotkey_entry.place(x=430, y=58)
hotkey_entry.insert(tk.END, 'f2')

# Make the text for the start delay entry box
start_delay_label = tk.Label(root, 
                        text=f"Start Delay",
                        anchor='center',
                        width=8,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
start_delay_label.place(x=560, y=35)
# Assign its tooltip
start_delay_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The amount of seconds \n after the hotkey is pressed \n before typing starts. \n Must be 1 to 10."))
start_delay_label.bind("<Leave>", hide_tooltip)

# Make the start delay entry
start_delay_entry = tk.Entry(root,
                        width=4,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
start_delay_entry.place(x=562, y=58)
start_delay_entry.insert(tk.END, '2')

#
# Make ---Behavior--- label
#
behavior_label = tk.Label(root, 
                        text=f"- - - - - - Behavior - - - - - -",
                        anchor='center',
                        width=25,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 11, "bold"))
# Assign it a location
behavior_label.place(x=413, y=95)

# Make the text for the error % entry box
error_label = tk.Label(root, 
                        text=f"Error Chance",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
error_label.place(x=420, y=120)
# Assign its tooltip
error_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The % chance that the \n program makes a single \n letter mistake. \n Must be 0 to 100."))
error_label.bind("<Leave>", hide_tooltip)

# Make the error % entry
error_entry = tk.Entry(root,
                        width=4,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
error_entry.place(x=431, y=143)
error_entry.insert(tk.END, '5')

# Make the text for the interval timing box for error %
error_entry_interval_label = tk.Label(root, 
                        text=f"Time before fix",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
error_entry_interval_label.place(x=542, y=120)
# Assign its tooltip
error_entry_interval_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The interval of times that the program can \n take to fix the mistake. Must be a single \n number or an interval 0.1 to 10."))
error_entry_interval_label.bind("<Leave>", hide_tooltip)

# Makes the interval timing box for error %
error_entry_interval = tk.Entry(root,
                        width=8,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
error_entry_interval.place(x=550, y=143)
error_entry_interval.insert(tk.END, '0.5 - 1.2')

# Make the text for the space pause % box
space_pause_label = tk.Label(root, 
                        text=f"Space wait",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
space_pause_label.place(x=413, y=170)
# Assign its tooltip
space_pause_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The % chance that the \n program stops at a \n space and waits. \n Must be 0 to 100."))
space_pause_label.bind("<Leave>", hide_tooltip)

# Make the space pause % box
space_pause_box = tk.Entry(root,
                        width=4,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
space_pause_box.place(x=431, y=193)
space_pause_box.insert(tk.END, '5')

# Make the text for the interval timing box for space pause % 
space_entry_interval_label = tk.Label(root, 
                        text=f"Wait duration",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
space_entry_interval_label.place(x=540, y=170)
# Assign its tooltip
space_entry_interval_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The interval of times that the program can \n wait before resuming typing. Must be \n a number or an interval 0.1 to 30."))
space_entry_interval_label.bind("<Leave>", hide_tooltip)

# Makes the interval timing box for space pause % 
space_entry_interval = tk.Entry(root,
                        width=8,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
space_entry_interval.place(x=550, y=193)
space_entry_interval.insert(tk.END, '1 - 3')

# Make the text for the period pause % box
period_pause_label = tk.Label(root, 
                        text=f"Period wait",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
period_pause_label.place(x=414, y=222)
# Assign its tooltip
period_pause_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The % chance that the \n program stops at a \n period and waits. \n Must be 0 to 100."))
period_pause_label.bind("<Leave>", hide_tooltip)

# Make the period pause % box
period_pause_box = tk.Entry(root,
                        width=4,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
period_pause_box.place(x=431, y=243)
period_pause_box.insert(tk.END, '5')

# Make the text for the interval timing box for period pause % 
period_entry_interval_label = tk.Label(root, 
                        text=f"Wait duration",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
period_entry_interval_label.place(x=540, y=222)
# Assign its tooltip
period_entry_interval_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The interval of times that the program can \n wait before resuming typing. Must be \n a number or an interval 0.1 to 60."))
period_entry_interval_label.bind("<Leave>", hide_tooltip)

# Makes the interval timing box for period pause % 
period_entry_interval = tk.Entry(root,
                        width=8,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
period_entry_interval.place(x=550, y=243)
period_entry_interval.insert(tk.END, '1 - 5')

#
# Make ---Speed--- label
#
speed_label = tk.Label(root, 
                        text=f"- - - - - - Speed - - - - - -",
                        anchor='center',
                        width=35,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 11, "bold"))
# Assign it a location
speed_label.place(x=367,y=280)

# Make the text for the block size box
block_size_label = tk.Label(root, 
                        text=f"Block size",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
block_size_label.place(x=412,y=306)
# Assign its tooltip
block_size_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The amount of letters that can \n be contained in a group that is \n given a general speed. Must be a \n full number 1 to 60 or it will be rounded."))
block_size_label.bind("<Leave>", hide_tooltip)

# Make the interval block size box
block_size_box = tk.Entry(root,
                        width=8,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
block_size_box.place(x=431,y=327)
block_size_box.insert(tk.END, '1 - 8')

# Make the text for the interval timing box for block speed
block_size_box_interval_label = tk.Label(root, 
                        text=f"Block speed",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
block_size_box_interval_label.place(x=538,y=306)
# Assign its tooltip
block_size_box_interval_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The interval of speeds that the program \n can give a selected block. Must be a number \n or an interval 0.1 to 60."))
block_size_box_interval_label.bind("<Leave>", hide_tooltip)

# Makes the interval timing box for block speed 
block_size_box_interval = tk.Entry(root,
                        width=8,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
block_size_box_interval.place(x=550,y=327)
block_size_box_interval.insert(tk.END, '0.1 - .35')

# Make the text for the interval timing box for per letter jitter
per_letter_speed_interval_label = tk.Label(root, 
                        text=f"Letter jitter",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
per_letter_speed_interval_label.place(x=414,y=356)
# Assign its tooltip
per_letter_speed_interval_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The interval of variation speeds that the program gives \n each letter alone by +/- from block speed. Must be a \n number or an interval 0.1 to 10."))
per_letter_speed_interval_label.bind("<Leave>", hide_tooltip)

# Make the - sign for the interval timing box for per letter jitter
per_letter_speed_interval_label = tk.Label(root, 
                        text=f"_",
                        anchor='center',
                        width=1,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 10, "bold"))
# Assign it a location
per_letter_speed_interval_label.place(x=418,y=369)

# Makes the interval timing box for per letter jitter
per_letter_speed_interval_box = tk.Entry(root,
                        width=8,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
per_letter_speed_interval_box.place(x=431,y=377)
per_letter_speed_interval_box.insert(tk.END, '0.2 - 0.1')

# Make the text for the box for min letter speed
min_letter_speed_box_label = tk.Label(root, 
                        text=f"Min speed",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
min_letter_speed_box_label.place(x=532,y=356)
# Assign its tooltip
min_letter_speed_box_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The absolute fastest any letter is \n allowed to be typed, to prevent any inhuman \n speeds. Must be a number 0.01 to 10."))
min_letter_speed_box_label.bind("<Leave>", hide_tooltip)

# Makes the box for min letter speed
min_letter_speed_box = tk.Entry(root,
                        width=8,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
min_letter_speed_box.place(x=550,y=377)
min_letter_speed_box.insert(tk.END, '0.05')

# Make the text for the shift delay box
shift_delay_box_label = tk.Label(root, 
                        text=f"Shift delay",
                        anchor='center',
                        width=13,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
shift_delay_box_label.place(x=411,y=406)
# Assign its tooltip
shift_delay_box_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The delay added to any key that \n requires shift to be typed. Must \n be a number 0 to 10."))
shift_delay_box_label.bind("<Leave>", hide_tooltip)

# Makes the shift delay box
shift_delay_box = tk.Entry(root,
                        width=4,
                        highlightthickness=1,  
                        highlightbackground="black",  
                        highlightcolor="white",
                        bg = "#2c2c2c",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location and default value
shift_delay_box.place(x=431,y=427)
shift_delay_box.insert(tk.END, '0.25')

# Make the est WPM label
wpm_label = tk.Label(root, 
                        text='WPM: 45.31',
                        width=40,
                        anchor='center',
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 17, "bold"))
# Assign it a location
wpm_label.place(x=249,y=459)
# Assign its tooltip - Note: using triple quotes broke the width of the tooltip so had to use a very long line with newlines in it
wpm_label.bind("<Enter>", lambda event: queue_tooltip(event, f"20-30 WPM: Beginner level, typically someone who is just starting to learn touch \n typing. Or typing essays while thinking pausing frequently to gather thoughts \n \n 40-50 WPM: Average typing speed. Most people who use a keyboard regularly \n fall within this range. It's comfortable for daily tasks and general typing. \n \n 60-80 WPM: Competent typist. This range is common for those who type \n frequently and can type at a steady pace for extended periods.\n \n 90-120 WPM: Fast typist. These people are typically experienced typists, possibly using typing \n as part of their work or hobbies. They're highly efficient in typing without sacrificing accuracy. \n \n 130+ WPM: Expert typist. People in this category are often professional typists, \n transcriptionists, or competitive typists. They type very quickly and maintain accuracy"))
wpm_label.bind("<Leave>", hide_tooltip)

# Make the est time label
time_label = tk.Label(root, 
                        text='Time: 00:05',
                        width=40,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
time_label.place(x=387,y=489)
# Assign its tooltip
time_label.bind("<Enter>", lambda event: queue_tooltip(event, f"The estimated amount of time \n the program will take to finish.\n More accurate with larger inputs"))
time_label.bind("<Leave>", hide_tooltip)

# Make the status label over the save button
status_label = tk.Label(root, 
                        text=f'Welcome to {version}!',
                        anchor='center',
                        width=40,
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 9, "bold"))
# Assign it a location
status_label.place(x=387,y=515)

# Makes the save button
save_button = tk.Button(root, 
                       text='Save', 
                       width=13,
                       # No command assigned, it is assigned lower down as the function it calls isn't defined yet
                       highlightthickness=1,  
                       highlightbackground="black",  
                       highlightcolor="white",
                       bg = "#2c2c2c",
                       activebackground="#008604",
                       fg="#ffffff",
                       font=("Arial", 9, "bold")) 
# Assign it a location
save_button.place(x=455, y=537)


# Make the word count label
word_count_label = tk.Label(root, 
                        text='Words: 3',
                        width=10,
                        anchor='w',
                        bg="#0e0e0e",
                        fg="#ffffff",
                        font=("Arial", 8, ""))
# Assign it a location
word_count_label.place(x=403,y=572)


"""Allows all of the default values for the typing variables to be changed. This function is primarily used
to change the values of the defaults when a new preset is selected."""
def set_defaults(
    error, delay, 
    error_interval_lower, error_interval_higher, 
    space, space_interval_lower, space_interval_higher, 
    period, period_interval_lower, period_interval_higher, 
    block_size_lower, block_size_higher, 
    block_size_interval_lower, block_size_interval_higher, 
    min_letter_speed, 
    per_letter_speed_interval_lower, per_letter_speed_interval_higher, 
    shift_delay
):
    global error_default, delay_default, error_interval_lower_default, error_interval_higher_default
    global space_default, space_interval_lower_default, space_interval_higher_default
    global period_default, period_interval_lower_default, period_interval_higher_default
    global block_size_lower_default, block_size_higher_default
    global block_size_interval_lower_default, block_size_interval_higher_default
    global min_letter_speed_default, per_letter_speed_interval_lower_default, per_letter_speed_interval_higher_default
    global shift_delay_default
    
    error_default = error
    delay_default = delay
    error_interval_lower_default = error_interval_lower
    error_interval_higher_default = error_interval_higher
    space_default = space
    space_interval_lower_default = space_interval_lower
    space_interval_higher_default = space_interval_higher
    period_default = period
    period_interval_lower_default = period_interval_lower
    period_interval_higher_default = period_interval_higher
    block_size_lower_default = block_size_lower
    block_size_higher_default = block_size_higher
    block_size_interval_lower_default = block_size_interval_lower
    block_size_interval_higher_default = block_size_interval_higher
    min_letter_speed_default = min_letter_speed
    per_letter_speed_interval_lower_default = per_letter_speed_interval_lower
    per_letter_speed_interval_higher_default = per_letter_speed_interval_higher
    shift_delay_default = shift_delay

# Called to give all of the typing variables their default values
set_defaults(
    error=5,
    delay=2,
    error_interval_lower=0.5,
    error_interval_higher=1.2,
    space=5,
    space_interval_lower=1,
    space_interval_higher=3,
    period=5,
    period_interval_lower=1,
    period_interval_higher=5,
    block_size_lower=1,
    block_size_higher=8,
    block_size_interval_lower=0.1,
    block_size_interval_higher=0.35,
    min_letter_speed=0.05,
    per_letter_speed_interval_lower=0.2,
    per_letter_speed_interval_higher=0.1,
    shift_delay=0.25
)

"""Works with set_defaults for mass updating the values used for typing, this however is responsible
for changing the numbers placed in the entry boxes when the preset is changed."""
def update_ui_preset():
    # Update the error chance entry
    error_entry.delete(0, tk.END)
    error_entry.insert(tk.END, str(error_default))

    # Update the start delay entry
    start_delay_entry.delete(0, tk.END)
    start_delay_entry.insert(tk.END, str(delay_default))

    # Update the error interval entry
    error_entry_interval.delete(0, tk.END)
    error_entry_interval.insert(tk.END, f"{error_interval_lower_default} - {error_interval_higher_default}")

    # Update the space chance entry
    space_pause_box.delete(0, tk.END)
    space_pause_box.insert(tk.END, str(space_default))

    # Update the space interval entry
    space_entry_interval.delete(0, tk.END)
    space_entry_interval.insert(tk.END, f"{space_interval_lower_default} - {space_interval_higher_default}")

    # Update the period chance entry
    period_pause_box.delete(0, tk.END)
    period_pause_box.insert(tk.END, str(period_default))

    # Update the period interval entry
    period_entry_interval.delete(0, tk.END)
    period_entry_interval.insert(tk.END, f"{period_interval_lower_default} - {period_interval_higher_default}")

    # Update the block size entry
    block_size_box.delete(0, tk.END)
    block_size_box.insert(tk.END, f"{block_size_lower_default} - {block_size_higher_default}")

    # Update the block speed interval entry
    block_size_box_interval.delete(0, tk.END)
    block_size_box_interval.insert(tk.END, f"{block_size_interval_lower_default} - {block_size_interval_higher_default}")

    # Update the per letter speed interval entry
    per_letter_speed_interval_box.delete(0, tk.END)
    per_letter_speed_interval_box.insert(tk.END, f"{per_letter_speed_interval_lower_default} - {per_letter_speed_interval_higher_default}")

    # Update the min letter speed entry
    min_letter_speed_box.delete(0, tk.END)
    min_letter_speed_box.insert(tk.END, str(min_letter_speed_default))

    # Update the shift delay entry
    shift_delay_box.delete(0, tk.END)
    shift_delay_box.insert(tk.END, str(shift_delay_default))


"""This is used in relation to the preset dropdown, the selected value is assigned a
letter to represent it via this dict. The letter is set to display in the dropdown once
the preset is selected as opposed to the entire word."""
def on_preset_select(selected_value):
    global preset_tooltip, error_default, delay_default
    preset_map = {
        "Essay": "E",
        "Normal": "N",
        "Proficient": "P"
    }
    # Update the displayed value in the dropdown to the abbreviation
    preset_dropdown_choice.set(preset_map.get(selected_value, ""))

    # Changes tooltip based off preset selected, this is for normal
    if selected_value == "Normal":
        preset_dropdown.bind("<Enter>", lambda event: queue_tooltip(event, f"Normal: Average typing speed for somone who uses a \n computer regularly, typing without as much thought such as \n typing to a friend or something more casual."))
        preset_dropdown.bind("<Leave>", hide_tooltip)
        set_defaults(
        error=5,
        delay=2,
        error_interval_lower=0.5,
        error_interval_higher=1.2,
        space=5,
        space_interval_lower=1,
        space_interval_higher=3,
        period=5,
        period_interval_lower=1,
        period_interval_higher=5,
        block_size_lower=1,
        block_size_higher=8,
        block_size_interval_lower=0.1,
        block_size_interval_higher=0.35,
        min_letter_speed=0.05,
        per_letter_speed_interval_lower=0.2,
        per_letter_speed_interval_higher=0.1,
        shift_delay=0.25
        )
        update_ui_preset()
        saveChanges(preset = True)
    # Changes tooltip based off preset selected, this is for essay
    elif selected_value == "Essay":
        preset_dropdown.bind("<Enter>", lambda event: queue_tooltip(event, f"Essay: Typing slower along with more pauses for \n thought, for if you were typing something such \n as an essay or a more important paper."))
        preset_dropdown.bind("<Leave>", hide_tooltip)
        set_defaults(
        error=3,
        delay=2,
        error_interval_lower=0.7,
        error_interval_higher=1.4,
        space=15,
        space_interval_lower=3,
        space_interval_higher=7,
        period=20,
        period_interval_lower=5,
        period_interval_higher=12,
        block_size_lower=3,
        block_size_higher=9,
        block_size_interval_lower=0.15,
        block_size_interval_higher=0.4,
        min_letter_speed=0.06,
        per_letter_speed_interval_lower=0.25,
        per_letter_speed_interval_higher=0.15,
        shift_delay=0.25
        )
        update_ui_preset()
        saveChanges(preset = True)
    # Changes tooltip based off preset selected, this is for proficient
    elif selected_value == "Proficient":
        preset_dropdown.bind("<Enter>", lambda event: queue_tooltip(event, f"Proficient: Fast yet mostly accurate typing, \n for if you were someone who types consistantly \n for work, hobbies, or competition."))
        preset_dropdown.bind("<Leave>", hide_tooltip)
        set_defaults(
        error=1,
        delay=2,
        error_interval_lower=0.3,
        error_interval_higher=1.1,
        space=3,
        space_interval_lower=1,
        space_interval_higher=3,
        period=2,
        period_interval_lower=2,
        period_interval_higher=4,
        block_size_lower=4,
        block_size_higher=15,
        block_size_interval_lower=0.1,
        block_size_interval_higher=0.16,
        min_letter_speed=0.03,
        per_letter_speed_interval_lower=0.22,
        per_letter_speed_interval_higher=0.12,
        shift_delay=0.15
        )
        update_ui_preset()
        saveChanges(preset = True)
    
# Variable used and default value for presets dropdown
preset_dropdown_choice = tk.StringVar(root)
preset_dropdown_choice.set("N")
# Make and place the font size dropdown
preset_dropdown = tk.OptionMenu(root, preset_dropdown_choice, "Essay", "Normal", "Proficient",command=on_preset_select)
preset_dropdown.config(font=("Arial", 8, "bold"), bg="#2c2c2c", fg="#ffffff", width=1, height=1, highlightthickness=1, highlightbackground="black", highlightcolor="white")
preset_dropdown.place(x=556,y=536)
# Sets default tooltip and default values for the preset
preset_dropdown.bind("<Enter>", lambda event: queue_tooltip(event, f"Normal: Average typing speed for somone who uses a \n computer regularly, typing without as much thought such as \n typing to a friend or something more casual."))
preset_dropdown.bind("<Leave>", hide_tooltip)

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
text_entry.place(x=-1,y=0,height=590, width=405)

# Variable and default value for font size dropdown
font_dropdown_choice = tk.StringVar(root)
font_dropdown_choice.set("Size")  # Default
# Make and place the font size dropdown
font_dropdown = tk.OptionMenu(root, font_dropdown_choice, 6, 8, 10, 12, 14, 16, 18)
font_dropdown.config(font=("Arial", 9, "bold"), bg="#2c2c2c", fg="#ffffff", width=2)
font_dropdown.place(x=344,y=0)

"""Allows the font size to be updated via the dropdown without changing the size of
the text entry box."""
def change_font_size(*args):
    new_size = int(font_dropdown_choice.get()) 
    new_font = ("Open Sans", new_size, "bold")  
    text_entry.config(font=new_font) 
font_dropdown_choice.trace_add("write", change_font_size)

# 
# ↑ The above lines are responsible for creating UI and its function ↑ 
#
# 
# ↓ The following lines are responsible for UI logic and the typing loop ↓
#
 
"""Opens the relative_letters.tsv file and writes it to a dict using the csv module. Specifically with
the first item in each row being the key that contains a list of letters that key is able
to misspell as, used later on."""
def tsv_to_dict(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        data = {row[0]: row[1:] for row in reader}
    return data

"""Sets the filepath of the mentioned tsv file to be the path of the program then filename, however
when ran as an .exe it directs the search for the file to where ever the .exe keeps it."""
if getattr(sys, 'frozen', False):  
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)  
file_path = os.path.join(base_path, "relative_letters.tsv")
data_dict = tsv_to_dict(file_path)

# The list of all the letter strings that can be used in a mistake
mistake_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# The list of special characters that aren't seen as capital but still need shift
shift_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?','“','”',"‘","’"]
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


"""Flips between typing and not using a bool, it also updates the text entry
box when ran and updates the status label over the save button. This function
will wait for the duration of the start delay before it starts to type."""
def toggle_wait():
    global can_start_type_loop
    can_start_type_loop = not can_start_type_loop
    if can_start_type_loop:  
        update_text()
        status_label.config(text='Typing In Progress - UI Disabled')  
        root.title(f"Auto Typer {version} (Typing In Progress - UI Disabled)")
        root.after(int((start_delay * 1000)), type_text)
# Sets default hotkey to call above function
keyboard.add_hotkey(hot_key, toggle_wait)

"""Updates the text entry var when the hotkey is hit, reguardless
of if the save button is hit."""
def update_text():
    global text
    text = str(text_entry.get("1.0", tk.END))

"""Flashes the selected object a chosen color for a chosen amount of time
before returning to the selected original color. This is mainly used to flash
the entry boxes different colors when saving."""
def flash_color(object, color, og_color, time):
    object.config(bg=color)
    root.after(time, lambda: object.config(bg=og_color)) 

"""Updates the single value number boxes based off given object and saves their value 
to the related var, if it is a valid number and between the given min and max then 
it is saved normally. If it is not a number it is set to the given default. If it is
over or under the min or max it is set to that value and the returned fail bool is true."""
def update_number_box(object, min, max, default, fail):
    try:
        var = default
        var = float(object.get())
        flash_color(object, "#008604", "#2c2c2c", 1500)
        if not min <= var <= max:
            raise ValueError
    except ValueError:
        object.delete(0, tk.END)
        if isinstance(var, (int, float)):
             if  var < min:
                 object.insert(tk.END, min)
                 var = min
             elif var > max:
                 object.insert(tk.END, max)
                 var = max
        if var != min and var != max:
             var = default
             object.insert(tk.END, default)
        fail = True
        flash_color(object, "#860000", "#2c2c2c", 1500)
    return [var, fail]

"""Updates the two number inteval boxes based off given object and saves their values 
to the related vars, if they are both a valid number and between the given min and max then 
it is saved normally. If either is not a valid number or above / below the min or max then
then both values are set to default and the fail bool is returned as true."""
def update_interval_box(object, min, max, fail, lower_val, upper_val):
    # First checks and returns if a single number was given
    try:
        var = float(object.get())
        if min <= var <= max:
            upper = var
            lower = var
            fail = False
            flash_color(object, "#008604", "#2c2c2c", 1500)
            return [float(lower), float(upper), fail]
        else: 
            raise ValueError
    except ValueError:
    # If not a single number, tries to convert the string into an interval of two numbers
        try:
            var_spaces = str(object.get())
            var = var_spaces.replace(" ", "")
            is_lower = True
            lower = ""
            upper = ""
            # Loops through string with spaces removed looking for a , or -
            marking = ""
            for i in var:
                if i == "," or i == "-":
                    if is_lower:
                        is_lower = False
                        marking = i
                # Swaps between the two vars used for the two numbers based on when the marker is found
                if is_lower:
                    lower += i
                else:
                    upper += i
            # Removes the marker from the upper number
            if marking != "":
                upper_cleaned = upper.replace(marking, "")
            # Continues like how the simple number function does, now with two numbers
            flash_color(object, "#008604", "#2c2c2c", 1500)
            if not min <= float(lower) <= max or not min <= float(upper_cleaned) <= max:
                raise ValueError
        except ValueError:
            lower, upper_cleaned = lower_val, upper_val
            fail = True
            object.delete(0, tk.END)
            object.insert(tk.END, f"{lower} - {upper_cleaned}")
            flash_color(object, "#860000", "#2c2c2c", 1500)
        return [float(lower), float(upper_cleaned), fail] 

"""Assigns the new given hotkey from the UI to a keyboard module hotkey, 
it is only updated if the hotkey is different."""
def update_hotkey():
    global hot_key
    new_hotkey = str(hotkey_entry.get())
    flash_color(hotkey_entry, "#008604", "#2c2c2c", 1500)

    if new_hotkey != hot_key:  
        keyboard.remove_hotkey(hot_key)  
        hot_key = new_hotkey  
        keyboard.add_hotkey(hot_key, toggle_wait)

"""Based off all settings entered, estimates the WPM that the program will
type at along with the amount of time it will take to type the given text.
It also converts the minutes calculation to a readable MM:SS"""
def calc_wpm():
    total_chars = len(text)
    total_words = total_chars / 5 # Used to use the actual amount of words before but char / 5 seems to be the standard
    

    error_average = (((error_interval_lower + error_interval_higher) / 2) * (error_chance / 100)) * total_chars
    space_time = (((space_interval_lower + space_interval_higher) / 2) * (space_chance / 100)) * text.count(" ")
    period_time = (((period_interval_lower + period_interval_higher) / 2) * (period_chance / 100)) * text.count(".")
    block_speed_average = (((block_size_interval_lower + block_size_interval_upper) / 2) + ((per_letter_speed_interval_lower + per_letter_speed_interval_upper) / 2)) * total_chars
    if block_speed_average < min_letter_speed:
        block_speed_average = min_letter_speed

    capital_time = (sum(1 for char in text if char.isupper())) * shift_delay
   
    total_typing_time = (block_speed_average + error_average + space_time + period_time + capital_time) / 60
    
    wpm = round((total_words / total_typing_time), 2)
    
    total_min = math.floor(total_typing_time)
    total_sec = round((total_typing_time - total_min) * 60)
    
    return [wpm, total_min, total_sec]


"""Saves all changes when the save button is pressed, mostly calls the
update_number_box and update_interval_box functions to save their values to 
their vars and check for any issues. Also updates the hotkey and text entry which
never fails. If one or more box returns fail as true the status label over the save
button will change its text to reflect that. It also will be different if a preset
is loaded."""
def saveChanges(preset = False):
    global error_chance, start_delay, error_interval_lower, error_interval_higher, space_chance, space_interval_lower, space_interval_higher, period_chance, period_interval_lower, period_interval_higher, block_size_lower, block_size_upper, block_size_interval_lower, block_size_interval_upper, per_letter_speed_interval_lower, per_letter_speed_interval_upper, min_letter_speed, shift_delay
    fail = False
    error_chance, fail = update_number_box(error_entry, 0, 100, error_default, fail) 
    start_delay, fail = update_number_box(start_delay_entry, 1, 10, delay_default, fail)
    error_interval_lower, error_interval_higher, fail = update_interval_box(error_entry_interval, 0.1, 10, fail, error_interval_lower_default, error_interval_higher_default)
    space_chance, fail = update_number_box(space_pause_box, 0, 100, space_default, fail)
    space_interval_lower, space_interval_higher, fail = update_interval_box(space_entry_interval, 0.1, 30, fail, space_interval_lower_default, space_interval_higher_default)
    period_chance, fail = update_number_box(period_pause_box, 0, 100, period_default, fail)
    period_interval_lower, period_interval_higher, fail = update_interval_box(period_entry_interval, 0.1, 60, fail, period_interval_lower_default, period_interval_higher_default)
    block_size_lower, block_size_upper, fail = update_interval_box(block_size_box, 1, 60, fail, block_size_lower_default, block_size_higher_default)
    block_size_interval_lower, block_size_interval_upper, fail = update_interval_box(block_size_box_interval, .1, 60, fail, block_size_interval_lower_default, block_size_interval_higher_default)
    per_letter_speed_interval_lower, per_letter_speed_interval_upper, fail = update_interval_box(per_letter_speed_interval_box, 0, 10, fail, per_letter_speed_interval_lower_default, per_letter_speed_interval_higher_default)
    per_letter_speed_interval_lower = -per_letter_speed_interval_lower
    min_letter_speed , fail = update_number_box(min_letter_speed_box, 0.01, 10, min_letter_speed_default, fail)
    shift_delay, fail = update_number_box(shift_delay_box, 0, 10, shift_delay_default, fail)
    update_hotkey() 
    update_text() 
    wpm, total_min, total_sec= calc_wpm() 
    wpm_label.config(text=f'WPM: {wpm}')
    time_label.config(text=f'Time: {total_min:02}:{total_sec:02}')
    if not preset:
        if fail:
            status_label.config(text='Saved: Invalid values defaulted')
        else:
            status_label.config(text='Saved: All values valid')
    else:
        status_label.config(text='Preset values applied')
# Adds this function ^ to the save button
save_button.config(command=saveChanges)

"""Updates the word counter live based off the text entry."""
def update_word_count(event=None):
    text_content = text_entry.get("1.0", "end-1c") 
    words = text_content.split()
    word_count_label.config( text = f"Words: {len(words)}")
# Calls this function ^ when a key is released in the text entry box
text_entry.bind("<KeyRelease>", update_word_count)


"""Main typing loop, uses all of the given vars from the UI to decide behavior.
responsbile for everything that happens once the hotkey is hit as this is the
only section ran."""
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
                
        # Pause control
        
        # X chance to wait Xs-Xs at a period
        if rd.uniform(0, 1) < (period_chance / 100) and i == ".":
            time.sleep(rd.uniform(period_interval_lower, period_interval_higher))

        # X% chance to wait Xs-Xs at a space
        if rd.uniform(0, 1) < (space_chance / 100) and i == " ":
            time.sleep(rd.uniform(space_interval_lower, space_interval_higher))
        
        # X% chance to mistype letter, 95% chance the letter is nearby and 5% chance it is random
        if rd.uniform(0, 1) < (error_chance / 100) and i != " " and i!= '\n' and i not in shift_list:
            # Makes the 95%-5% choice
            if rd.uniform(0, 1) < .95:
                mistake = "err"
                while mistake == "err":
                    mistake = rd.choice(data_dict[i])
            else: mistake = rd.choice(mistake_list)
            # Types and deletes the mistake
            keyboard.press_and_release(mistake)
            time.sleep(rd.uniform(error_interval_lower, error_interval_higher))
            keyboard.press_and_release('backspace')

        # Speed Control

        # Chooses the amount of affected letters and general speed they'll be typed at 
        if rand_letter == 0:
            rand_letter = rd.randint(round(block_size_lower), round(block_size_upper))
            rand_range = rd.uniform( block_size_interval_lower, block_size_interval_upper)
        # Adds small variation per letter based off general speed
        rand_speed = rd.uniform((rand_range + per_letter_speed_interval_lower), (rand_range + per_letter_speed_interval_upper))
        # Prevents a letter ever being typed faster than .05s
        if rand_speed < min_letter_speed:
            rand_speed = min_letter_speed
        # Applies the work of this group
        time.sleep(rand_speed)

        # Special Characters

        # Converts Gdocs smart double quotes to normal ones
        if i == "“" or i == "”":
            time.sleep(shift_delay)
            keyboard.press('shift')
            keyboard.press_and_release('\'')
            keyboard.release('shift')
        
        # Converts Gdocs smart single quotes to normal ones
        elif i == "‘" or i == "’":
            time.sleep(shift_delay)
            keyboard.press_and_release('\'')

        # Types Letters    

        # Converts uppercase letters to lowercase then types them while holding shift
        # Is also set to be used if any special characters need shift
        elif is_upper:
            time.sleep(shift_delay)
            keyboard.press('shift')
            keyboard.press_and_release(i)
            keyboard.release('shift')
        
        # Types lowercase letters
        else:
            try:
                keyboard.press_and_release(i)
            except:
                pass

        
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
    root.title(f"Auto Typer {version}")

    # Resets the toggle  variable so typing will start upon hotkey
    can_start_type_loop = False

"""Main loop to continuously check the wait variable and type accordingly"""
def main_loop():
    root.after(100, main_loop)

# Start the main loop
root.after(100, main_loop)

# Start the Tkinter main loop
root.mainloop()

"""
--------------------------------------
UPDATE NOTES V2.0 - V2.1
--------------------------------------
Window now displays correct version name
Added a "Lucas Martin - 2025" label to bottom right
Added tooltip framework and tooltips to all current options
saving returns a fail var, used to give a diff message if anything is set to default
Added settings sections
made save color flashes longer, 1s to 1.5s
added UI options for all behavior variables, error, space, and period % and wait controls
added UI options for all speed variables, speed, delays, blocks, and jitter controls
added estimated wpm and time
added presets that changes default values and applies preset values
added word counter
added more comments and reworded comments
"""