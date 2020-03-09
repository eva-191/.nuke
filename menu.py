# ----------------------------------
# menu.py
# Version: 1.0.0
# Last Updated: March 9th, 2020
# ----------------------------------

import nuke
import platform

# Define where .nuke directory is on each OS's network.
Win_Dir = ''
MacOSX_Dir = ''
Linux_Dir = '/net/homes/echioche/.nuke'

#Set global directory
dir = Linux_Dir 

if platform.system() = "Linux":
	dir = Linux_Dir
elif platform.system() == "Darwin":
	dir = Mac_Dir
elif platform.system() == "Windows":
	dir = Win_Dir
else:
	dir = None






nuke.knobDefault('Merge2.bbox', 'B')
nuke.knobDefault('STMap.uv', 'rgb')
nuke.knobDefault('STMap.label', '[value filter]')
