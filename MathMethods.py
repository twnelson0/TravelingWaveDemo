import numpy as np


"""
Psudo 'Continous Dirac Measure' function, used to clean up wave pulse code and to allow for more generalized pulses.
Function returns a 0 if x is not between a and b (a and b inculsive)
Idea is that this is the indicator fucntion/dirac measure for the set [a,b]
"""
cDirac = lambda x,a,b: float(x >= a and x <= b)

#Sine Wave function
sineWave = lambda x,t,k,ohm,amp,phase : amp*np.cos(k*x - ohm*t + phase)

"""
Create a static sine wave pulse that is n*lambda in size
"""
sinePulseStatic = lambda x,t,k,ohm,amp,phase,n : cDirac(x,0,n*(np.pi*2)/k)*amp*np.cos(k*x - ohm*t + phase)

#Create a propogating sine wave pulse that is n*lambda in size
sinePulse = lambda x,t,k,ohm,amp,phase,n : cDirac(x,(ohm/k)*t,n*abs((np.pi*2)/k) + (ohm/k)*t)*sineWave(x,t,k,ohm,amp,phase)


