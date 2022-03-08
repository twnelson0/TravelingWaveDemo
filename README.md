# Overview
Script produces an animation of a traveling wave.
At present it can produce an animated plot of a traveling sine wave and a one wavelength sinusoidal pulse.
The script can also make an animated plot of a one wavelength sinusoidal pulse with an accompanying time vs amplitude graph at a fixed position. 

## Dependencies
* Should work with either Python3 or Python2 but has only been tested extensively in Python3
* Requires packages numpy and matplotlib
* To save the animations as video files FFMPEG may be needed

## Running
At present the code is a bit of a mess and the UI is functionally nonexistent.
The code has only been tested on Ubuntu 20.04.
To run just type the command `python3 travelSineWave.py` in the terminal.
At present the code is configured to run the function `pulseTimeAnimation` with the default values for the arguments.
The function `pulseTimeAnimaiton` has arguments for the wave number, angular frequency, wave amplitude, phase, a variable called `epsVal` that determines the size of the time steps of the animation as a multiple of the wave period and a variable called `nWav` that determines how many "wave lengths" the pulse will be.
By default `epsVal` is set to 0.01 (time steps are 1 percent of the period), the phase is set to -pi/2 and the remaining arguments are set to 1.
If you want to change what plot is produced you need to comment out line 188 of `travelSineWave.py` and replace it with a different function call.
If you want to save the plot of the sine wave pulse and the time vs amplitude plot you need to modify the last 3 lines of the function `pulseTimeAnimation`.
You can modify line 190 to change the format that the file is saved under and what the file is named.

There is also a time vs amplitude and position vs amplitude animated plot for a plane wave. 
It takes the most same arguments as the pulse function, the only difference is that it doesn't take the `nWav` variable as an argument.
