# Overview
Script produces an animation of a traveling wave.
At present it can produce an animated plot of a traveling sine wave and a one wavelenght sinusoidal pulse.
The script can also make an animated plot of a one wavelength sinusoidal pulse with an accompanying time vs amplitude graph at a fixed posistion. 

## Dependencies
* Python > 3.X.Y
* numpy and matplotlib
* To save the animations you may need FFMPEG

## Running
At present the code is a bit of a mess.
The code has only been tested on Ubuntu 20.04.
To run just type the command `python3 travelSineWave.py` in the terminal.
At present the code is configured to show the user a sine wave pulse with an accompanying time vs amplitude plot.
If you want to change what plot is produced you need to comment out line 188 of `travelSineWave.py` and replace it with a different function call.
If you want to save the plot of the sine wave pulse and the time vs amplitude plot you need to modify the last 3 lines of the funciton `pulseTimeAnimation`.
You can modify line 190 to change the format that the file is saved under and what the file is named.
