# This file is Copyright (c) 2020 Gregory Davill <greg.davill@gmail.com>
# License: MIT

# Simple script that makes use of the python interface in KiCad to position and route a LED matrix.

import sys
from pcbnew import *

# For some reason the script console inside of KiCad nightly is broken. 
# So we must run this externally, and also save back the changes we perform on the PCB.

#pcb = GetBoard()
pcb = LoadBoard('../kicad-src/meiji-led-ring.kicad_pcb')

from math import sin, cos, pi
from random import randint


center_x = 160
center_y = 88
n_leds = 24
radius = 28


for n in range(1, n_leds+1):
    # Pick out our designators, these need to be in order
    Ref = 'D' + str(n)
    nPart = pcb.FindFootprintByReference(Ref)

    rad = 2*pi * n/n_leds

    # Set part X/Y + Rotation
    nPart.SetPosition(wxPoint(FromMM(center_x + radius*cos(rad)), FromMM(center_y + radius*sin(rad))))
    
    nPart.SetOrientationDegrees((n / n_leds) * -360)

SaveBoard('../kicad-src/meiji-led-ring.kicad_pcb', pcb)
