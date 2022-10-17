import datetime
from datetime import timedelta
import csv
import itertools
from simple_chalk import chalk, green

print('''
.......,,,,............................:**:.........................................,,..............
.....:*%%%%?:.....................,,,..;SS:....................................,,,.,+;,.............
....:%SSSSSS;....................:%%;..;S%:....................................+%%,,;;,.............
....*S%*++*?:....,,..............:%S+..;S%:.,.....................,.......,,...+S%,.,,..............
....?S%,...,...:*?%?;,.:**:..+*+;?%%?*+;S%*???;,+*+..,**:..;**,,+?%?+,..;????;+?%%**;.,;**;::;:.....
....?S%*:,....:%SSSSS*,;SS;..?S?+S%%SS?;S%SSSSS;*S%,.+SS+.,%S?,?SSSSS*.+SSSSS*?S%%SS+.;%%%%?;;+:....
....;SSS%%*:.,?S%*+?SS;;SS;..?S?:*%S?++;S%?+*%S*;SS;.?SS?.:%S++S%+:*S%:?S?::+:;?%%**;.+%%%%%%+;;....
.....;?%SSS%::SS+..,%S?;SS;..?S?.:%S+..;SS:..?S?,%S*,%%%%:+S%:%S?;:+%S+?S%+:...+S%,...*??%%%%%*:....
......,:+%%S?+SS:...?S?;%S;..?S?.:%S+..;S%:..?S?.*S?+S%%S+?S?:%%%SSSSS+;SSS%?:.+S%,...+%?*%%%SS;....
.........,%S%+SS;...?S?;%S;..?S?.:%S+..;S%:..?S?.;S%%S++S%%S;,%%%*****;.:*%%S?,+S%,...,%S%*?SS?,....
....;*:,,;%S?:%S?:,+%S*;SS+,,?S?.:%S+..;S%:..?S?.,%%%%::%%%%,,%S%:..,:.,,.,*S%,+S%:....;%SS*?%:.....
....*S%%%%%S+.*SS%%SS%:,%S%%%%S?.,%S%?*;S%:..?S?..?SS?.,?%S*..+SS%??%?.*%**%S%,;S%%?;...;%SS*:......
....*%SSSS%+,.,*%SSS%;..;%SSSS%?..+SSS?+SS:..?S?..+SS+..+SS;..,+%SSSS?,?SSSS%;.,?SSS+....:%?:.......
....,:;;+;,.....:;+;,....,;;;;:,...:+;:,::,..:;:..,::,..,;:,....:;+;:,.,;++;,...,;+;,.....,,........
....................................................................................................
====================================================================================================
|                                   Ramp Shift Change Optimizer                                    |
====================================================================================================
PROBLEM: Typically 30+ gates utilized in ramp staffing. Often times a flight is on a gate during shift change causing delays.
AM shift would occasionally be off before the pm starts or not enough time is available to start the upload.

Using Ramp Schedule:
1.) Determine Staffed Gates
2.) Enter AM Shift's Off Time
3.) Enter PM Shift's Start Time
4.) Calculate time between off time and start time.
5.) Determine closure start time and stop time per gate
6.) Rearrange/Sort gate order to match top to bottom Opssuite Order.

Resulting in aircraft not being loaded in a timely manner. 
Goal is to identify scheduling issues, calculate shift change time for a closure. 
Convert to Opssuite in order to go top to bottom adding closures quickly.

@Notes 
Closure 15 minutes prior to AM off time. Up until 15 minutes past PM Start time
30 GATES
'''
      )

# ****REQUIRE VALIDATION ON VALUES *****
# time increments in minutes
FIVE_MINUTES = timedelta(minutes=5)
TEN_MINUTES = timedelta(minutes=10)
FIFTEEN_MINUTES = timedelta(minutes=15)
TWENTY_MINUTES = timedelta(minutes=20)
TWENTYFIVE_MINUTES = timedelta(minutes=25)
THIRTY_MINUTES = timedelta(minutes=30)
FORTY_MINUTES = timedelta(minutes=40)
FORTYFIVE_MINUTES = timedelta(minutes=45)

VALID_GATE_VALUES = [
    23, 24, 25, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36,
    37, 38, 39, 40, 41, 42, 43,
    44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57,
    58, 59, 60, 61, 62, 63, 64,
    65, 66, 67
]

CONTROL_PANEL = {
    "C23": True, 
    "C24": True, 
    "C25": True, 
    "C26": True,
    "C27": True, 
    "C28": True, 
    "C29": True, 
    "C30": False,
    "C31": True, 
    "C32": False, 
    "C33": True, 
    "C34": False,
    "C35": True, 
    "C36": False, 
    "C37": True, 
    "C38": False,
    "C39": False, 
    "C40": False, 
    "C41": True, 
    "C42": False,
    "C43": True, 
    "C44": True, 
    "C45": True, 
    "C46": False,
    "C47": True, 
    "C48": False, 
    "C49": False, 
    "C50": False,
    "C51": False, 
    "C52": False, 
    "C53": False, 
    "C54": True,
    "C55": True, 
    "C56": True, 
    "C57": True, 
    "C58": True,
    "C59": True, 
    "C60": True, 
    "C61": True, 
    "C62": True,
    "C63": True,
    "C64": True, 
    "C65": True, 
    "C66": True, 
    "C67": True,
}

# EMPTY_CONTROL_PANEL = {}
# CHANGE_GATE_STATUS = str(input("What gate would you like to change the status of?"))
# for gate in CONTROL_PANEL:
#     if CHANGE_GATE_STATUS == gate:
#         CONTROL_PANEL.update(['False'])
#         print(gate)

# UPDATED_CONTROL_PANEL


# def current_control_panel():
#     count = 0
#     for key, value in CONTROL_PANEL.items():
#         if value == True:
#             count += 1
#             print("#", count, key, value)
#     print("Operating", count, "Gates")


# # Question to close or open a gate:
# SEE_GATES = str(
#     input("Would you like to see what gates you are using?, YES OR NO"))
# if SEE_GATES == "yes" or SEE_GATES == "YES":
#     print("Ok, here's the current gates you are using:")
#     current_control_panel()
    # CHANGE_GATE_STATUS_QUESTION = str(input("Would you like to change the status of any of these gates?"))
    # if CHANGE_GATE_STATUS_QUESTION == "yes" or CHANGE_GATE_STATUS_QUESTION == "YES":
    #     print("you answered yes")
    #     # change_gate_status()
    # elif CHANGE_GATE_STATUS_QUESTION == "no" or CHANGE_GATE_STATUS_QUESTION == "NO":
    #     print("You answered no")
    # else:
    #     print('Oh well')
# elif SEE_GATES == "no" or SEE_GATES == "NO":
#     print("ok moving on then:")
# else:
#     print("you didn't answer the question yes or no")
#     exit()

# RAMP_SCHEDULE_GATES = []
# ramp_gate_count = 0
# for key, value in CONTROL_PANEL.items():
#     if value == True:
#         ramp_gate_count += 1
#         RAMP_SCHEDULE_GATES.append(key)
# print("OPERATING:", len(RAMP_SCHEDULE_GATES), "GATES",
#       RAMP_SCHEDULE_GATES)


gate_list = [
'44',
'41',
'43',
'45',
'47',
'54',
'56',
'58',
'60',
'55',
'57',
'59',
'61',
'62',
'64',
'66',
'63',
'65',
'67',
'23',
'25',
'27',
'29',
'24',
'26',
'28',
'31',
'33',
'35',
'37']

ramp_scheduled_gates = []
opssuite_gates = []
ramp_am_off = []
ramp_pm_start = []
gate_gap_length = []
close_time = []
reopen_time = []

# RAMP SCHEDULE ORDER OF GATES

# print("Here we're looking for the first Lead C-GATE just after the LAV DRIVERS SECTION")
# with open('rampschedule.csv', 'w', newline='') as g:
#     ENTERED_GATE_COUNTER = 0
#     filewriter = csv.writer(g)
#     user_input = ''
#     # Start a loop that will run until the user enters 'save'.
#     while user_input != 'save':
#         user_input = input("Scheduled Gates - Enter Gate #:")
#         if user_input == 'save' or user_input == '':
#             print("Saving Gates and Gate Count")
#             break
#         else:
#             ramp_scheduled_gates.append(user_input)
#             ENTERED_GATE_COUNTER += 1
#             print("ADDED", "GATE:", user_input, "to the list.", ENTERED_GATE_COUNTER, "gates so far")
#     staffed_gates = len(ramp_scheduled_gates)
#     filewriter.writerow(["Ramp Schedule Gates"])
#     for i in ramp_scheduled_gates:
#         filewriter.writerow([i])
#     filewriter.writerow(["We currently have:",staffed_gates,"staffed gates."])
#     print("We currently have:", staffed_gates, "staffed gates.")
#     if len(ramp_scheduled_gates) == len(RAMP_SCHEDULE_GATES):
#         print("GATE COUNTS ARE EQUAL GOOD JOB")
#     else:
#         print("Something's wrong, start over.")
#         exit()
# g.close()

# Ramp AM Offtime
with open('rampschedule.csv', 'a', newline='') as g:
    filewriter = csv.writer(g)
    user_input = ''
    # Start a loop that will run until the user enters 'save'.
    while user_input != 'save':
        user_input = input("Ramp Schedule - Enter AM Shift Off Time: ")
        if user_input != 'save':
            q = int(user_input[:2])
            r = int(user_input[-2:])
            s = timedelta(hours=q, minutes=r)
            ramp_am_off.append(s)
        else:
            filewriter.writerow(ramp_am_off)
g.close()

# Ramp PM Start Time
with open('rampschedule.csv', 'a', newline='') as g:
    filewriter = csv.writer(g)
    user_input = ''
    while user_input != 'save':
        user_input = input(
            "Ramp Schedule - Enter PM Start Time in 4 digit times: ")
        if user_input != 'save':
            q = int(user_input[:2])
            r = int(user_input[-2:])
            s = timedelta(hours=q, minutes=r)
            ramp_pm_start.append(s)
        else:
            filewriter.writerow(ramp_pm_start)
g.close()

# Calculate Gate Closure
# We want the AM offtime to occur after the PM start time.
# EXAMPLE 1300 OFF TIME 1230 START TIME 30 MINUTES OVERLAP

with open('rampschedule.csv', 'a', newline='') as g:
    filewriter = csv.writer(g)
    subtracted = list()
    for p in range(len(ramp_pm_start)):
        item = ramp_am_off[p] - ramp_pm_start[p]
        gate_gap_length.append(item)
        # filewriter.writerow(gate_gap_length)
print(gate_gap_length, "Minutes")
# CLOSE TIME
for e in ramp_am_off:
    t = e - THIRTY_MINUTES
    close_time.append(t)
# REOPEN TIME
for o in ramp_pm_start:
    n = o + THIRTY_MINUTES
    reopen_time.append(n)
for (d, k, l, c, e, o) in zip(gate_list, ramp_am_off, ramp_pm_start, gate_gap_length, close_time, reopen_time):
    print("Gate:", d, "Ramp off at:", k, "PM Crew starts:", l,
          "Gate gap length:", c, "close gate at:", e, "reopen gate at:", o)
g.close()


# REARRANGE GATES FOR OPSSUITE USE
# print(gate_gap_length)
# # Opssuite Gates:
# with open('rampschedule.csv', 'a', newline='') as g:
#     filewriter = csv.writer(g)
#     user_input = ''
#     # Start a loop that will run until the user enters 'save'.
#     while user_input != 'save':
#         user_input = input("Opssuite Gates - Enter Gate #: ")
#         if user_input != 'save':
#             opssuite_gates.append("C"+user_input)
#         else:
#             filewriter.writerow(opssuite_gates)
# print(opssuite_gates)
# g.close()
