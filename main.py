import datetime
from datetime import timedelta
import csv
import itertools
from simple_chalk import chalk, green


"""
PROBLEM: 30 gates utilized in ramp staffing. AM shift would occasionally be off before the pm starts.
Resulting in aircraft not being loaded in a timely manner. 
Goal is to identify scheduling issues, calculate shift change time for a closure. 
Convert to Opssuite in order to go top to bottom adding closures quickly.

# First variable I need to enter hours, and then minutes

@devnotes 
Closure 15 minutes prior to AM off time. Up until 15 minutes past PM Start time
30 GATES

"""
# ****REQUIRE VALIDATION ON VALUES *****
VALID_GATE_VALUES = [
    23, 24, 25, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36,
    37, 38, 39, 40, 41, 42, 43,
    44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57,
    58, 59, 60, 61, 62, 63, 64,
    65, 66, 67
]
# time increments in minutes
FIVE_MINUTES = timedelta(minutes=5)
TEN_MINUTES = timedelta(minutes=10)
FIFTEEN_MINUTES = timedelta(minutes=15)
TWENTY_MINUTES = timedelta(minutes=20)
TWENTYFIVE_MINUTES = timedelta(minutes=25)
THIRTY_MINUTES = timedelta(minutes=30)
FORTY_MINUTES = timedelta(minutes=40)
FORTYFIVE_MINUTES = timedelta(minutes=45)

CONTROL_PANEL = {
    "C23": True, "C24": True, "C25": True, "C26": True, 
    "C27": True, "C28": True, "C29": True, "C30": False,
    "C31": True, "C32": False, "C33": True, "C34": False,
    "C35": True, "C36": False, "C37": True, "C38": False,
    "C39": False, "C40": True, "C41": True, "C42": True,
    "C43": True, "C44": True, "C45": True, "C46": False,
    "C47": True, "C48": False, "C49": False, "C50": False,
    "C51": False, "C52": False, "C53": False, "C54": True, 
    "C55": True, "C56": True, "C57": True, "C58": True,
    "C59": True, "C60": True, "C61": True, "C63": True,
    "C64": True, "C65": True, "C66": True, "C67": True,
}

ramp_scheduled_gates = []
opssuite_gates = []
ramp_am_off = []
ramp_pm_start = []
gate_gap_length = []
close_time = []
reopen_time = []
# closure_calc_value = x
# closure_value_before = 15
# closure_value_after = 15
# Ramp Staffed Gates

with open('rampschedule.csv', 'w', newline='') as g:
    filewriter = csv.writer(g)
    user_input = ''
    # Start a loop that will run until the user enters 'save'.
    while user_input != 'save':
        user_input = input("Ramp Schedule Gates - Enter Gate #: ")
        if user_input != 'save':
            ramp_scheduled_gates.append("C"+user_input)
        else:
            filewriter.writerow(ramp_scheduled_gates)
    staffed_gates = len(ramp_scheduled_gates)
    filewriter.writerow(
        ("We currently have:", staffed_gates, "staffed gates."))
print("We currently have:", staffed_gates, "staffed gates.")
g.close()

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
for (d, k, l, c, e, o) in zip(ramp_scheduled_gates, ramp_am_off, ramp_pm_start, gate_gap_length, close_time, reopen_time):
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
