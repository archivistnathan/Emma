# ------------------------------------------------------------------------------
# Environmental Monitoring and Management for Archives (EMMA) Project
#
# Test functionality of microphone used as sound intensity sensor
#
# PRIVACY NOTICE
# This code captures audio clips with a 1s duration. The clip is then automatically processed by the sox utility to return statistics relating to sound intensity. The clip is overwritten on the next reading cycle.
#
# FOR DEBUGGING ONLY
#
# (c) 2020 Jonathan Isip, Quezon City, Philippines
# A project with the University of the Philippines School of Library and Information Studies
# Released under GNU General Public License (GPL v3.0) 
# email nathan@slis.upd.edu.ph
# ------------------------------------------------------------------------------

# This code requires sox installed

# import libraries for GPIO and I2C
import subprocess
import re

# Record a 1s audio clip
subprocess.call(["arecord", "-D", "plughw:1,0", "-qd", "1", "monitor.wav"])

# FOR DEBUGGING, cecking is syntax of check_output is valid
checkp = subprocess.check_output(["date"])
print 'Date is: ', checkp

# Use sox to get clip stats which are outputted to stderr
soxout = subprocess.check_output(["sox", "monitor.wav", "-n", "stats"], stderr=subprocess.STDOUT)
print("Output is: ",soxout)
print("\n")

# Convert string to list
outlist = soxout.split('\n')
print("Converted list is: ",outlist)
print("\n")

#Split list item to attribute and value strings
clipstat = []
for line in range(len(outlist)):
	print(outlist[line])
	liststat = outlist[line].rsplit(" ",1)
	clipstat.append(liststat)

print("\n")

print(clipstat)

print(date())

#process = subprocess.Popen(["sox", "monitor.wav", "-n", "stats"], 
#                           stdout=subprocess.PIPE,
#                           universal_newlines=True)
#soundblock = process.communicate()[0]

# 	print(soundblock)

#while True:
#	output = process.stdout.readline()
#    print(output.strip())
    # Do something else
#    return_code = process.poll()
#    if return_code is not None:
#        print('RETURN CODE', return_code)
#        # Process has finished, read rest of the output 
#        for output in process.stdout.readlines():
#            print(output.strip())
#        break