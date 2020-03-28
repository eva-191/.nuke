# -----------------------------------------------
# shuffleShortcuts.py
# Version: 3.0.0
# Author: Eva Chiochetti

# Last modified by: Eva Chiochetti
# Last Updated: March 28th, 2020
# -----------------------------------------------

# -------------------------------------------------------------------------
# USAGE:
#
# Creates a shuffle node that shuffles RGBA channels into the Green channel
# -------------------------------------------------------------------------


import nuke

def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):

    # Create a new shuffle node. and assign it to a variable so we can change some things...
    myShuffle = nuke.createNode("Shuffle")


    # Change the input & output channels to what is defined in the in_channel and out_channel arguments.
    myShuffle['in'].setValue(in_channel)
    myShuffle['out'].setValue(out_channel)


    # Change the relevant knobs to shuffle the RGBA channels to the green channel.
    myShuffle['red'].setValue(set_channel)
    myShuffle['green'].setValue(set_channel)
    myShuffle['blue'].setValue(set_channel)
    myShuffle['alpha'].setValue(set_channel)
    
    # Change the the node colour to green (we have to convert Nuke's weird hex colour values to RGB to be a bit more human-readable)
    myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255,gColor*255,bColor*255,1),16))
    
    #Add a node label
    myShuffle['label'].setValue("[value red] > [value out]")




# Adding menu items for our shuffleShortcuts.py functions
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "ctrl+shift+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to All)", "shuffleShortcuts.createCustomShuffle(
    [pasted text truncated for security]
