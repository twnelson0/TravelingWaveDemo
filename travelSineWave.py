#Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#Sine Wave function
sineWave = lambda x,t,k,ohm,amp,phase : amp*np.cos(k*x - ohm*t + phase)

#Animate a sinewave
def sineAnimation(k,ohm,amp = 1):
    #Obtain physical quanities
    per = 2*np.pi/ohm
    waveLen = np.pi*2/k

    #Set up the frame
    fig = plt.figure()
    ax = plt.axes(xlim =(0,4*waveLen), ylim=(-(amp + 0.1*amp),(amp + 0.1*amp)))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    #ax.set_title("Test")
    line, = ax.plot([], [], 'k-', lw=2)
    time_text = ax.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes) #Show current time 


    #Initialazation function
    def init():
        line.set_data([], [])
        time_text.set_text("")
        
        return line, time_text
    
    #Animate Frame
    def animate(frame):
        x = np.linspace(0,4*(2*np.pi)/k,100)
        y = sineWave(x,frame*per*0,0.01,k,ohm,amp)
        line.set_data(x,y)

        time_text.set_text('t = %.1f s' % (frame*per*0.01))
        #time_text.set_text("t = " + str(frame*per*0.01) + " s")

        return line, time_text

    
    #Animate wave
    anim = animation.FuncAnimation(fig,animate,init_func = init, frames = 500, interval = 35,blit = True)
    plt.show()

#Animate a traveling sinusodial pulse
def sinePulseAnimation(k,ohm,amp = 1):
    #Obtain physical quanities
    per = 2*np.pi/ohm
    waveLen = np.pi*2/k
    cProp = ohm/k

    #Set up the frame
    fig = plt.figure()
    ax = plt.axes(xlim =(0,4*waveLen), ylim=(-(amp + 0.1*amp),(amp + 0.1*amp)))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    #ax.set_title("Test")
    line, = ax.plot([], [], 'k-', lw=2)
    time_text = ax.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes) #Show current time

    #Initialazation function
    def init():
        line.set_data([], [])
        time_text.set_text("")
        
        return line, time_text 

    #Animate Frame
    def animate(frame):
        t = frame*per*0.01
        x = np.linspace(0,4*(2*np.pi)/k,500)
        y = x*0

        #Fill the amplitude array
        for i in range(500):
            #Create Pulse
            if (x[i] >= 0 + cProp*t and x[i] <= (2*np.pi)/k + cProp*t):
                y[i] = sineWave(x[i],t,k,ohm,amp,-np.pi/2)
            else:
                continue
        
        line.set_data(x,y)
        time_text.set_text('t = %.1f s' % t)

        return line, time_text

    #Animate wave
    anim = animation.FuncAnimation(fig,animate,init_func = init, frames = int(3*waveLen/(cProp*0.01*per)), interval = 35,blit = True)
    plt.show()


#Animate pulse and t vs y plot at fixed point
def pulseTimeAnimation(k = 1, ohm = 1, amp = 1, epsVal = 0.01):
    #Obtain physical quanities
    per = 2*np.pi/ohm
    waveLen = np.pi*2/k
    cProp = ohm/k
    nFrames = int(3*waveLen/(cProp*epsVal*per))

    #Set up the frame
    fig, axes = plt.subplots(2,1)
    line1, = axes[0].plot([], [], 'k-', lw=2)
    line2, = axes[1].plot([], [], 'r-', lw=2)

    #Set up plot 1
    axes[0].set_xlim(0,4*waveLen)
    axes[0].plot(4*(2*np.pi)/k*249/499,0,'r*', lw = 1)
    axes[0].set_ylim(-(amp + 0.1*amp),(amp + 0.1*amp))
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].set_title("x vs y")

    #Set up plot 2
    axes[1].set_xlim(0,3*waveLen/cProp)
    axes[1].set_ylim(-(amp + 0.1*amp),(amp + 0.1*amp))
    axes[1].set_xlabel("t")
    axes[1].set_ylabel("y")
    axes[1].set_title("")
    axes[1].set_title('t vs y at x = %.1f' % (4*waveLen/(500 - 1)*249))

    plt.subplots_adjust(hspace=0.65)

    time_text = axes[0].text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=axes[0].transAxes) #Show current time

    #Initialazation function
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        time_text.set_text("")
        
        return line1, line2, time_text

    #Animate the first plot
    def animate(frame):
        #Animate plot 1
        t1 = frame*per*epsVal 
        x = np.linspace(0,4*(2*np.pi)/k,500)
        y1 = x*0

        #Fill the amplitude array
        for i in range(500):
            #Create Pulse
            if (x[i] >= 0 + cProp*t1 and x[i] <= (2*np.pi)/k + cProp*t1):
                y1[i] = sineWave(x[i],t1,k,ohm,amp,-np.pi/2)
            else:
                continue
        
        line1.set_data(x,y1)
        time_text.set_text('t = %.1f s' % t1)

        #Animate plot 2
        y2Arr = np.array([])
        t2Arr = np.array([])

        #Regenerate previous frames 
        for i in range(frame + 1):
            tVal = i*per*epsVal

            #Pulse condition
            if (tVal >= (x[249] - waveLen)/cProp and tVal <= x[249]/cProp):
                yVal = sineWave(x[249],tVal,k,ohm,amp,-np.pi/2)
            else:
                yVal = 0
            
            t2Arr = np.append(t2Arr,tVal)
            y2Arr = np.append(y2Arr,yVal)
        
        line2.set_data(t2Arr,y2Arr)

        #Check for timing bug
        if (t2Arr[len(t2Arr) - 1] != t1):
            print("!!The Plots are out of sync!!")

        return line1, line2, time_text

    #Animate wave
    anim = animation.FuncAnimation(fig,animate,init_func = init, frames = int(3*waveLen/(cProp*epsVal*per)), interval = 45,blit = True)
    plt.show()
    #anim.save("TestAnim.avi",animation.FFMpegWriter(fps=10))



#sineAnimation(1,1)
#sinePulseAnimation(1,1)
pulseTimeAnimation()

#if __namespace__ == "__main__"



