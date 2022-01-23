import numpy as np
import random

class randPoly(object):
	"""
	Generate random polynomial of specified degree, degree must be 0 or a natural number
	User must specify max and minimum value of terms in polynomial, by default these terms are between 0 and 1
	"""
	def __init__(self, deg, minVal = 0, maxVal = 1):
		super(randPoly, self).__init__()
		self.deg = deg
		self.minVal = minVal
		self.maxVal = maxVal
		self.coeffArr = np.array([])
		self.genPoly()

	#Generate terms in polynomical
	def genPoly(self):
		for k in range(self.deg):
			kTerm = random.random()*(self.maxVal + self.minVal) - self.minVal
			np.append(self.coeffArr,kTerm)

	#Output value of polynomial
	def poly(self,x):
		polyOut = 0
		for k in range(self.deg):
			polyOut += x**k*self.coeffArr[k]

		return polyOut


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

#Create a random polynoial pulse
#polyPulse = lambda x,t,k,ohm
