from datetime import timedelta
import csv

# t1 = timedelta(hours=7, minutes=36)
# t2 = timedelta(hours=11, minutes=32)
# t3 = timedelta(hours=13, minutes=7)
# t4 = timedelta(hours=21, minutes=0)
# arrival = t2 - t1
# lunch = (t3 - t2 - timedelta(hours=1))
# departure = t4 - t3
# print(arrival, lunch, departure)
gates = []
opssuite_gates = []
ramp_am_off = []
ramp_pm_start = []

with open('rampschedule.csv', 'w', newline='') as g:
    filewriter = csv.writer(g)
    user_input = ''
    # Start a loop that will run until the user enters 'save'.
    while user_input != 'save':
        user_input = input("Ramp Schedule Gates - Enter Gate #: ")
        if user_input != 'save':
            gates.append("C"+user_input)
        else:
            filewriter.writerow(gates)
print(gates)
    while user_input != 'save':
        user_input = input("Opssuite Gates - Enter Gate #: ")
        if user_input != 'save':
            opssuite_gates.append("C"+user_input)
        else:
            filewriter.writerow(opssuite_gates)
print(opssuite_gates)

        
g.close()

# Setup Opssuite Gate List
