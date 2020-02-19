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
# http://sox.sourceforge.net/sox.html

# import libraries for GPIO and I2C
import subprocess
import re
from datetime import datetime

print(datetime.now())

# Record a 1s audio clip
subprocess.call(["arecord", "-D", "plughw:1,0", "-qd", "1", "monitor.wav"])

# Use sox to get clip stats which are outputted to stderr
soxout = subprocess.check_output(["sox", "monitor.wav", "-n", "stats"], stderr=subprocess.STDOUT)

# Remove extra whitespaces
soxout = re.sub("\s\s+", " ", soxout)

# Convert string to list
outlist = soxout.split('\n')

#Split list item to attribute and value strings
clipstat = []
for line in range(len(outlist)):
	liststat = outlist[line].rsplit(" ",1)
	clipstat.append(liststat)

# Isolate specific values and convert to float
# From sox docsL Pk lev dB and RMS lev dB are standard peak and RMS level measured in dBFS. RMS Pk dB and RMS Tr dB are peak and trough values for RMS level measured over a short window (default 50ms).
# This measures dBFS, i.e. intensity relative to the full scale clipping point. This is not dB-SPL and thus not directly reflective of sound pressure.

print "Pk level dB: ", float(clipstat[3][1])
print "RMS level dB: ", float(clipstat[4][1])
print "RMS peak dB: ", float(clipstat[5][1])
print "RMS Trough dB: ", float(clipstat[6][1])

print(datetime.now())