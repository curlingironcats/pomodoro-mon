import os
import pathlib
import sys
import time
import tkinter
from tkinter import *
import pygame.mixer
from tkextrafont import Font


# Pomodoro Timer
# functions outside window

# give functionality to the pomodoro button
def pomodoro():
    # hide the stop button, show the start button again
    window.title(f"{WINDOW_TITLE}")
    study_hours_label.place(x=850)
    stop_button_border.place(x=850, y=canvas.winfo_height() - 350)
    start_button.pack()
    pygame.mixer.music.unload()

    # resets the timer and countdown when pomodoro button is pressed
    global timer_seconds
    global timer_minutes
    global local_minutes

    window.after_cancel(timer_cancel)
    local_minutes = 0
    timer_seconds = 0
    try:
        with open(minutes_file_path, "r") as file:
            timer_minutes = int(file.read())
    except ValueError:
        timer_minutes = 30

    timer_label.configure(text=f"{timer_minutes}:00",
                          bg=POMODORO_COLOR)

    # changes the background color when pomodoro button is pressed
    canvas.configure(bg=POMODORO_COLOR)

    start_button.configure(foreground=POMODORO_COLOR,
                           activeforeground=POMODORO_COLOR)

    stop_button.configure(foreground=POMODORO_COLOR,
                          activeforeground=POMODORO_COLOR)

    settings_button.configure(activebackground=POMODORO_COLOR,
                              activeforeground=POMODORO_COLOR,
                              background=POMODORO_COLOR)

    study_hours_label.configure(fg=POMODORO_COLOR)

    # bold the pomodoro button font, lighten the other button fonts when pomodoro button is pressed
    # also changes the background color to match the canvas
    # pomodoro = normal
    # short_break, long break = light
    pomodoro_button.configure(bg=POMODORO_COLOR,
                              activebackground=POMODORO_COLOR,
                              font=normal_font)

    short_break_button.configure(bg=POMODORO_COLOR,
                                 activebackground=POMODORO_COLOR,
                                 font=light_font)

    long_break_button.configure(bg=POMODORO_COLOR,
                                activebackground=POMODORO_COLOR,
                                font=light_font)


# gives functionality to the short break button
def short_break():
    # hide the stop button, show the start button again
    window.title(f"{WINDOW_TITLE}")
    study_hours_label.place(x=850)
    stop_button_border.place(x=850, y=canvas.winfo_height() - 350)
    start_button.pack()
    pygame.mixer.music.unload()

    # resets the timer and countdown when short break button is pressed
    global timer_seconds
    global timer_minutes
    global local_minutes

    window.after_cancel(timer_cancel)
    local_minutes = 0
    timer_seconds = 0
    timer_minutes = 5
    timer_label.configure(text=f"0{timer_minutes}:00",
                          bg=SHORT_BREAK_COLOR)

    # changes the background color when short break button is pressed
    canvas.configure(bg=SHORT_BREAK_COLOR)

    start_button.configure(foreground=SHORT_BREAK_COLOR,
                           activeforeground=SHORT_BREAK_COLOR)

    stop_button.configure(foreground=SHORT_BREAK_COLOR,
                          activeforeground=SHORT_BREAK_COLOR)

    settings_button.configure(activebackground=SHORT_BREAK_COLOR,
                              activeforeground=SHORT_BREAK_COLOR,
                              background=SHORT_BREAK_COLOR)

    study_hours_label.configure(fg=SHORT_BREAK_COLOR)

    # bold the short break button font, lighten the other button fonts when short break button is pressed
    # also changes the background color to match the canvas
    # short break = normal
    # pomodoro, long break = light
    short_break_button.configure(bg=SHORT_BREAK_COLOR,
                                 activebackground=SHORT_BREAK_COLOR,
                                 font=normal_font)

    pomodoro_button.configure(bg=SHORT_BREAK_COLOR,
                              activebackground=SHORT_BREAK_COLOR,
                              font=light_font)

    long_break_button.configure(bg=SHORT_BREAK_COLOR,
                                activebackground=SHORT_BREAK_COLOR,
                                font=light_font)


# gives functionality to the long break button
def long_break():
    # hide the stop button, show the start button again
    window.title(f"{WINDOW_TITLE}")
    study_hours_label.place(x=850)
    stop_button_border.place(x=850, y=canvas.winfo_height() - 350)
    start_button.pack()
    pygame.mixer.music.unload()

    # resets the timer and countdown when long break button is pressed
    global timer_seconds
    global timer_minutes
    global local_minutes

    window.after_cancel(timer_cancel)
    local_minutes = 0
    timer_seconds = 0
    timer_minutes = 15
    timer_label.configure(text=f"{timer_minutes}:00",
                          bg=LONG_BREAK_COLOR)

    # changes the background color when long break button is pressed
    canvas.configure(bg=LONG_BREAK_COLOR)

    start_button.configure(foreground=LONG_BREAK_COLOR,
                           activeforeground=LONG_BREAK_COLOR)

    stop_button.configure(foreground=LONG_BREAK_COLOR,
                          activeforeground=LONG_BREAK_COLOR)

    settings_button.configure(activebackground=LONG_BREAK_COLOR,
                              activeforeground=LONG_BREAK_COLOR,
                              background=LONG_BREAK_COLOR)

    study_hours_label.configure(fg=LONG_BREAK_COLOR)

    # bold the long break button font, lighten the other button fonts when short break button is pressed
    # also changes the background color to match the canvas
    # long break = normal
    # pomodoro, short break = light
    long_break_button.configure(bg=LONG_BREAK_COLOR,
                                activebackground=LONG_BREAK_COLOR,
                                font=normal_font)

    pomodoro_button.configure(bg=LONG_BREAK_COLOR,
                              activebackground=LONG_BREAK_COLOR,
                              font=light_font)

    short_break_button.configure(bg=LONG_BREAK_COLOR,
                                 activebackground=LONG_BREAK_COLOR,
                                 font=light_font)


# gives functionality to the start button
def start():
    # all the variables we need to access and change
    global timer_cancel
    global timer_minutes
    global timer_seconds
    global center_x
    global center_y
    global start_button
    global stop_button_border
    global stored_minutes
    global local_minutes
    bg_color = (canvas.config("bg"))

    # change the start button to the stop button when start button is pressed
    alarm_sound.stop()
    start_button.forget()
    stop_button_border.place(x=313 - 34, y=canvas.winfo_height() - 350)

    # animate the image of mameo when the timer is ticking
    if timer_seconds % 2:
        canvas.itemconfig(mameo_pic, image=mameo1)
    else:
        canvas.itemconfig(mameo_pic, image=mameo2)

    # tick over the minutes and seconds
    if timer_seconds == 0:
        timer_minutes -= 1
        timer_seconds = 59
        if stop_button_border.winfo_x() == 279:
            local_minutes += 1
        if bg_color[4] == POMODORO_COLOR and local_minutes >= 1:
            stored_minutes += 1
            settings_dir.mkdir(parents=True, exist_ok=True)
            with open(timer_track_file_path, "w") as file:
                file.write(str(stored_minutes))

    else:
        timer_seconds -= 1

    if timer_seconds == -1:
        timer_seconds = 59

    if timer_seconds < 10:
        zero_place_seconds = 0
    else:
        zero_place_seconds = ""
    if timer_minutes < 10:
        zero_place_minutes = 0
    else:
        zero_place_minutes = ""

    # update the window title to show time remaining
    window.title(f"{WINDOW_TITLE} - {zero_place_minutes}{timer_minutes}:{zero_place_seconds}{timer_seconds}")

    #  update timer label when the time ticks
    timer_label.configure(text=f"{zero_place_minutes}{timer_minutes}:{zero_place_seconds}{timer_seconds}")

    # timer ends at 0 minutes 0 seconds
    # when timer ends, change the mode to break time or focus depending on which mode we were on

    if timer_seconds == 0 and timer_minutes == 0:
        # access the bg color to prepare for mode change
        # if on pomodoro, change to short break
        if bg_color[4] == POMODORO_COLOR:
            short_break()
        # if on short break, change to pomodoro
        elif bg_color[4] == SHORT_BREAK_COLOR:
            pomodoro()
        # if on long break, change to pomodoro
        elif bg_color[4] == LONG_BREAK_COLOR:
            pomodoro()

        # when timer ends, play the alarm sound
        # and switch the stop button to the start button
        alarm()
        stop()
    else:
        # if timer is not at 0 minutes 0 seconds
        # so if timer is not over, then continue to call the start function countdown
        timer_cancel = window.after(1000, start)


# gives functionality to the stop button
def stop():
    # stop any music playing
    # and stop the calling of the start function
    window.title(f"{WINDOW_TITLE}")
    pygame.mixer.music.unload()
    window.after_cancel(timer_cancel)
    # hide the stop button, then show the start button
    stop_button_border.place(x=850, y=canvas.winfo_height() - 350)
    start_button.pack()


# start/stop sound effect when start/stop button is clicked
def start_stop_sound():
    alarm_start_sound.set_volume(2)
    pygame.mixer.Sound.play(alarm_start_sound)


# music will play when the function is called when it is a break mode
def music_play():
    bg_color = (canvas.config("bg"))
    if bg_color[4] == LONG_BREAK_COLOR or bg_color[4] == SHORT_BREAK_COLOR:
        pygame.mixer.music.load(music_path, "mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)


# functions that will be performed if the user exits the program
def window_exit():
    # remember the position of the window when closed

    # make directory in appdata
    settings_dir.mkdir(parents=True, exist_ok=True)
    with open(window_settings_file_path, "w") as conf:
        conf.write(window.geometry())  # Assuming root is the root window

    # stop all music, allocate time for this process
    # prevents sound spillover if program is opened again
    pygame.mixer.Sound.stop(alarm_sound)
    pygame.mixer.Sound.stop(alarm_start_sound)
    pygame.mixer.music.unload()
    time.sleep(0.08)
    sys.exit(0)


# sound that plays when the timer is done
def alarm():
    alarm_sound.set_volume(0.5)
    pygame.mixer.Sound.play(alarm_sound)


# give functionality to the settings button
def settings():
    if study_hours_label.winfo_x() == 850:
        stored_hours = (stored_minutes / 60)
        stored_hours_conversion = "{0:.1f}".format(stored_hours)
        study_hours_label.configure(text=f"{stored_hours_conversion} hours studied",
                                    font=normal_font,
                                    background="#FFFFFF")
        study_hours_label.place(x=start_button_border.winfo_x(),
                                y=start_button_border.winfo_y() + 2)
        study_hours_label.place(x=((404) - (study_hours_label.winfo_width() / 2)))
        start_button.forget()
        window.update()
    else:
        study_hours_label.place(x=850)
        start_button.pack()


# -----------------------------------------------------------------------------------------------------------------------
# Constants, Variables, etc.
WINDOW_TITLE = "Pomomon"
HEIGHT = 750
WIDTH = 800
POMODORO_COLOR = "#4D77D9"
SHORT_BREAK_COLOR = "#7550BC"
LONG_BREAK_COLOR = "#C1561E"
# create directory in the appdata folder for standalone exe
# e.g. C:\Users\Onson Sweemey\AppData\Roaming\Ramis App
settings_dir = pathlib.Path(os.getenv("APPDATA"), "Pomomon")
# e.g. C:\Users\Onson Sweemey\AppData\Roaming\Ramis App\settings.json

# read in the timer minutes from a file

minutes_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SETTINGS\\timerminutes.txt")
try:
    with open(minutes_file_path, "r") as file:
        timer_minutes = int(file.read())
except ValueError:
    timer_minutes = 30
timer_seconds = 0


print(minutes_file_path)
print(os.getcwd())

# keep track of minutes locally after starting countdown
local_minutes = 0
# open the timetracker file to keep track of time studied
timer_track_file_path = settings_dir.joinpath("timertracker.txt")

try:
    with open(timer_track_file_path, "r") as file:
        stored_minutes = float(file.read())
except FileNotFoundError:
    stored_minutes = 0

# placeholder to stop the countdown timer
timer_cancel = "placeholder"

# create window
window = Tk()
window.resizable(False, False)
# give the window a title
window.title(f"{WINDOW_TITLE}")
# set window size
# automatically remember the position of the window from when it was last closed


window_settings_file_path = settings_dir.joinpath("windowsettings.txt")

# read the X and Y positon of the window from when last closed
try:
    with open(window_settings_file_path, "r") as conf:
        window.geometry(conf.read())
except FileNotFoundError:
    # default window position.
    window.geometry(f"{WIDTH}x{HEIGHT}")

# change window icon
clock_image = ()
window.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images\\pomoicon.ico"))

# prepare music and sound files
stored_music = "5PM.mp3"

music_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"music\\{stored_music}")
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.0)

# alarm sound
alarm_sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds\\alarmdone.mp3")
alarm_sound = pygame.mixer.Sound(alarm_sound_path)

# start/stop sound
alarm_start_sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds\\alarmstart.mp3")
alarm_start_sound = pygame.mixer.Sound(alarm_start_sound_path)

# store the file path for fonts
font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts\\test.ttf")
font2_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts\\testing.ttf")
timer_font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts\\om_large_plain.ttf")

# set the fonts to style the text
normal_font = Font(file=str(font_path),
                   family="Josefin Sans SemiBold",
                   size="20")

light_font = Font(file=str(font2_path),
                  family="Josefin Sans Light",
                  size="20")

timer_font = Font(file=str(timer_font_path),
                  family="Omelette Large Plain",
                  size="100")

# draw a canvas on the window
# this is the main background color depending on the current mode
canvas = Canvas(window,
                bg=POMODORO_COLOR,
                height=HEIGHT,
                width=WIDTH)

canvas.pack()

# set the image of a button to a blank object
# so that we can resize the button using a specific specified width and height
# image_hacking it together basically
image_hack = PhotoImage(width=1, height=1)

# set the image for the settings button
settings_icon = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "images\\settingsicon.png"))

# prepare mameo images (digimon and tamer)
mameo1 = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "images\\mameo1.png"))
mameo2 = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "images\\mameo2.png"))

# create a white border outline to put around text buttons
pomo_button_border = tkinter.Frame(window,
                                   highlightbackground="#ffffff",
                                   highlightcolor="#ffffff",
                                   highlightthickness=4,
                                   bd=0,
                                   height=1)
short_button_border = tkinter.Frame(window,
                                    highlightbackground="#ffffff",
                                    highlightcolor="#ffffff",
                                    highlightthickness=4,
                                    bd=0)
long_button_border = tkinter.Frame(window,
                                   highlightbackground="#ffffff",
                                   highlightcolor="#ffffff",
                                   highlightthickness=4,
                                   bd=0)

start_button_border = tkinter.Frame(window,
                                    highlightbackground="#ffffff",
                                    highlightcolor="#ffffff",
                                    highlightthickness=4,
                                    bd=0)

stop_button_border = tkinter.Frame(window,
                                   highlightbackground="#ffffff",
                                   highlightcolor="#ffffff",
                                   highlightthickness=4,
                                   bd=0)

# we'll need buttons for "pomodoro", "short break", "long break"
# configure pomodoro button
pomodoro_button = Button(pomo_button_border,
                         text="Pomomon",
                         fg="#FFFFFF",
                         bg=POMODORO_COLOR,
                         font=normal_font,
                         activebackground=POMODORO_COLOR,
                         activeforeground="#FFFFFF", bd=0,
                         command=pomodoro,
                         width=174 - 12,
                         height=79 - 12,
                         image=image_hack,
                         compound="c")

# place pomodoro button
pomodoro_button.pack()
pomo_button_border.place(x=100, y=50)

# short break button
# configure short break button
short_break_button = Button(short_button_border,
                            text="Short Break",
                            fg="#FFFFFF",
                            bg=POMODORO_COLOR,
                            font=light_font,
                            activebackground=POMODORO_COLOR,
                            activeforeground="#FFFFFF",
                            bd=0,
                            command=short_break,
                            image=image_hack,
                            compound="c",
                            width=174 - 12,
                            height=79 - 12)

# place short break button
short_break_button.pack()
short_button_border.place(x=313, y=50)

# long break
# configure long break button
long_break_button = Button(long_button_border,
                           text="Long Break",
                           fg="#FFFFFF",
                           bg=POMODORO_COLOR,
                           font=light_font,
                           activebackground=POMODORO_COLOR,
                           activeforeground="#FFFFFF",
                           bd=0,
                           image=image_hack,
                           compound="c",
                           command=long_break,
                           width=174 - 12,
                           height=79 - 12)

# place the long break button
# using window update to update coordinates of button
# then performing math on coordinates to get the right placement position
long_break_button.pack()
window.update()
temp_place = canvas.winfo_width()
long_button_border.place(x=temp_place, y=50)
window.update()
long_button_border.place(x=temp_place - long_button_border.winfo_width() - 100, y=50)

# start button
# start button configure
start_button = Button(start_button_border,
                      text="START",
                      fg=POMODORO_COLOR,
                      bg="#FFFFFF",
                      font=normal_font,
                      activebackground="#FFFFFF",
                      activeforeground=POMODORO_COLOR,
                      bd=0,
                      command=lambda: [start(), music_play(), start_stop_sound()],
                      image=image_hack,
                      compound="c",
                      width=250 - 12,
                      height=79 - 12)

# place the start button
start_button.pack()
start_button_border.place(x=313 - 34, y=canvas.winfo_height() - 350)

# stop button
stop_button = Button(stop_button_border,
                     text="STOP",
                     fg=POMODORO_COLOR,
                     bg="#FFFFFF",
                     font=normal_font,
                     activebackground="#FFFFFF",
                     activeforeground=POMODORO_COLOR,
                     bd=0,
                     command=lambda: [stop(), start_stop_sound()],
                     image=image_hack,
                     compound="c",
                     width=250 - 12,
                     height=79 - 12)

# hide stop button offscreen until start button is pressed
stop_button.pack()
stop_button_border.place(x=850, y=canvas.winfo_height() - 350)

# settings button
window.update()
settings_button = Button(window,
                         fg=POMODORO_COLOR,
                         bg=POMODORO_COLOR,
                         activebackground=POMODORO_COLOR,
                         activeforeground=POMODORO_COLOR,
                         bd=0,
                         command=settings,
                         image=settings_icon,
                         compound="c",
                         width=0,
                         height=0)
settings_button.place(x=start_button_border.winfo_x() + start_button_border.winfo_width() + 15,
                      y=start_button_border.winfo_y() + 2)

# create and display a timer on canvas
# probably using a label
#
timer_label = Label(text=f"{timer_minutes}:00",
                    font=timer_font,
                    bg=POMODORO_COLOR,
                    fg="#FFFFFF",
                    image=image_hack,
                    compound="c")
timer_label.place(x=850, y=650)

# center the label with quick maths
window.update()
center_x = int(window.winfo_width() / 2) - int(timer_label.winfo_width() / 2)
center_y = int(window.winfo_height() / 2) - int(timer_label.winfo_height() / 2)
timer_label.place(x=center_x, y=center_y - 100)

# create mr. mameo's image :3
# use math to center image
mameo_pic = canvas.create_image((window.winfo_width() / 2), window.winfo_height() - 125,
                                image=mameo1)

# label that displays hours studied
# placeholder for label position
study_hours_label = Label(window,
                          font=normal_font,
                          fg=POMODORO_COLOR,
                          background="#FFFFFF",
                          width=15,
                          pady=14)
study_hours_label.place(x=850,
                        y=850)

# updates the functionality when the window is closed
window.protocol("WM_DELETE_WINDOW", window_exit)

# display window
window.mainloop()
