# A Python console meetings calendar

# Imports the calendar module
import calendar
# Imports the datetime module
from datetime import datetime 
# Imports the time module
import time
# Imports the os module
import os

# Introducing the user to the program
print("""
               Meetings Calendar program.
""")
print("This program allows you to set up meetings with a date and time.")
print("All meetings will produced in a text file." + "\n")

# Explaining how to use the program
print("How to use the program:")
print("- Input date and time in the format 'dd mon 00:00'  ")
print("- Example: 22 mar 10:00")
print("- Input location of meeting by entering any place name")
print("- Example: Online \n")

# Allows user to continue and use the program
while True:
    answer = input("Would you like to view your existing meetings or create a new one? y/n ")
    if answer == "n":
        quit()
    if answer == "y":
        break

# Shows user if they have any existing meetings by reading text file
def print_existing_meetings():
    if not os.path.isfile("meetings.txt"):
        print("\nYou do not have any existing meetings \n")
        return
    print("\nYour existing meetings: ")
    file_object = open('meetings.txt', 'r')
    file_content = file_object.read()
    print(file_content)

# Function to get date and time of meeting
def ask_for_dtime():
    given_dtime = input("What date and time would you like to set up a meeting for? ")
    return datetime.strptime(given_dtime, "%d %b %H:%M")

# Function to get location of meeting
def ask_for_place():
    return input("\nWhere is the meeting taking place? ")

# Function to write meetings in text file
def write_meeting_to_file(dtime, place):
    file_object = open('meetings.txt', 'a')
    file_object.write(meeting_time.strftime("Meeting at %H:%M on %d %b at location " + place + "\n"))

# Shows users if they have successfully created a meeting
# Loop allows for multiple meetings to be created
print_existing_meetings()
while True:
    meeting_time = ask_for_dtime()
    meeting_place = ask_for_place()
    print(meeting_time.strftime("You have successfully created a meeting at %H:%M on %d %b"))
    write_meeting_to_file(meeting_time, meeting_place)
    answer1 = input("Would you like to create another meeting? y/n ")
    if answer1 != "y":
        break

# Thanks user for using the program
print("\nThank you for using the meetings calendar program")
print("If you would like to view your current meetings or create more please relaunch the program.")
input()   
