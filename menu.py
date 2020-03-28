# -----------------------------------------------
# menu.py
# Version: 1.0.0
# Last Updated: March 10th, 2020
# -----------------------------------------------


# -----------------------------------------------
# GLABAL IMPORTS ::::::::::::::::::::::::::::::::
# -----------------------------------------------

import nuke
import platform
import nukescripts
import shuffleShortcuts

# Define where .nuke directory is on each OS's network.
Win_Dir = ''
MacOSX_Dir = ''
Linux_Dir = '/net/homes/echioche/.nuke'

# Automatically set global directory
if platform.system() == "Linux":
	dir = Linux_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Windows":
	dir = Win_Dir
else:
	dir = None





# -----------------------------------------------
# KNOB DEFAULTS :::::::::::::::::::::::::::::::::
# -----------------------------------------------



nuke.knobDefault('Merge2.bbox', 'B')
nuke.knobDefault('STMap.uv', 'rgb')
nuke.knobDefault('STMap.label', '[value filter]')
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')





# -----------------------------------------------
# CUSTOM MENUS ::::::::::::::::::::::::::::::::::
# -----------------------------------------------


utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')


myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_bender.png")
myGizmosMenu.addCommand('Autocrop', 'nukescripts.autocrop()')





# ADD GIZMOS --------------------------------------------------------------------------------------------

myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon="bm_CameraShake_icon.png")
myGizmosMenu.addCommand('MonochromePlus', 'nuke.createNode("MonochromePlus")')
myGizmosMenu.addCommand('mS_Mark
    [pasted text truncated for security]
