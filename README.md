# Overview
Script produces an animation of a traveling wave.
At present it can produce an animated plot of a traveling sine wave and a one wavelenght sinusoidal pulse.
The script can also make an animated plot of a one wavelength sinusoidal pulse with an accompanying time vs amplitude graph at a fixed posistion. 

## Dependencies
* Should work with either Python3 or Python2 but I've only tested it on Python3
* numpy and matplotlib
* To save the animations as video files you may need FFMPEG

## Running
At present the code is a bit of a mess.
The code has only been tested on Ubuntu 20.04.
To run just type the command `python3 travelSineWave.py` in the terminal.
At present the code is configured to run the function `pulseTimeAnimation` with the default values for the arguements.
To the function `pulseTimeAnimaiton` has arguments for the wave number, angular frequency, wave amplitude and an varaible called `epsVal` that determines the size of the steps of the animation as a multiple of the wave period.
By default `epsVal` is set to 0.01 (time steps are 1 percent of the period), and the remaining arguments are set to 1.
If you want to change what plot is produced you need to comment out line 188 of `travelSineWave.py` and replace it with a different function call.
If you want to save the plot of the sine wave pulse and the time vs amplitude plot you need to modify the last 3 lines of the funciton `pulseTimeAnimation`.
You can modify line 190 to change the format that the file is saved under and what the file is named.
