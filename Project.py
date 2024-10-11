#problem 1
'''import matplotlib.pyplot as plt
import math
import numpy as np

a = float(input("Enter a value for the lattice constant a in (nm) \n"))
b = float(input("Enter a value for the lattice constant b  in (nm) \n"))
c = float(input("Enter a value for the lattice constant c in (nm) \n"))
print("The entered lattice constants are a = {}, b = {}, and c = {}".format(a,b,c))

h = float(input("Enter a value for the plane position 'h' \n"))
k = float(input("Enter a value for the lattice position 'k' \n"))
l = float(input("Enter a value for the lattice position 'l'  \n"))
print("The entered plane is ({}{}{})".format(h,k,l))

d = ((h**2)/(a**2)+(k**2)/(b**2)+(l**2)/(c**2))**(-1/2)

lam = 0.154
twotheta = (np.degrees(np.arcsin(lam/(2*d))))*2

print("The calculated value for two theta is {} in degrees, and the value for d is {} in nm".format(twotheta,d))'''

#problem 2b
'''
import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(0,1,100)
l = 1.54 #A
k = (2*np.pi)/l
a = 2 #A
x = a
x2 = 2*a
x3 = 3*a
c = ((3.0*(10**8))/(10**18))*10**10 # speed of light in meters per as
w = (2*np.pi*c)/l
a1 = np.sin(2*k*x-w*t)
a2 = np.sin(2*k*x2-w*t)
a3 = np.sin(2*k*x3-w*t)

plt.figure(1)
plt.plot(t,a1, color = 'r', label = "A_1")
plt.plot(t,a2, color ='b', label = "A_2")
plt.plot(t,a3, color = 'g', label = "A_3")

plt.xlabel("Time (as)")
plt.ylabel("Intensity")
plt.title("Plot of Three Scattering X-Rays")
plt.legend() 

asum = a1 + a2 + a3
plt.figure(2)
plt.plot(t,asum)
plt.xlabel("Time (as)")
plt.ylabel("Intensity")
plt.title("Plot of Sum of Scattering")
plt.show()

print(np.max(asum)**2)
'''
#problem 2c
'''
import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(0,1,100)
l = 1.54 #A
k = (2*np.pi)/l
a = 2 #A
asum = [0]*100
for num in range(1,101):
    x = a*num
    c = ((3.0*(10**8))/(10**18))*10**10 # speed of light in meters per as
    w = (2*np.pi*c)/l
    afunc = np.sin(2*k*x-w*t)
    plt.figure(1)
    plt.plot(t,afunc)
    plt.xlabel("Time (as)")
    plt.ylabel("Intensity")
    plt.title("Plot of 100 Scattering X-Rays")
    plt.legend() 
    asum = asum + afunc
plt.figure(2)
plt.plot(t,asum)
plt.xlabel("Time (as)")
plt.ylabel("Intensity")
plt.title("Plot of Sum of Scattering X-Rays")
plt.show()

print(np.max(asum**2))

'''
#problem 2d
'''


import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(0,1,100)
l = 1.54 #A
k = (2*np.pi)/l
a = np.linspace(1,4,300)
asum = [0]*100
amplist = []
for num1 in a:
    for num2 in range(1,101):
        apos =  num1
        x = apos*num2+10
        c = ((3.0*(10**8))/(10**18))*10**10 # speed of light in angstrom per as
        w = (2*np.pi*c)/l
        afunc = np.sin(2*k*x-w*t)
        asum = asum + afunc
    amp = (np.max(asum))**2
    amplist.append(amp)
    asum = [0]*100
plt.figure(2)
plt.plot(a,amplist)
plt.xlabel("Lattice Constant (A)")
plt.ylabel("Intensity")
plt.title("Plot of Summed Diffracted X-rays with x_n positioned 10 A further away ")
plt.show()
'''
#problem 3a


import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(0,1,100)
l = 1.54 #A
k = ((2*np.pi)/l)*np.sin(np.pi/4)
a = 2.84 #A
asum = [0]*100
for num in range(1,101):
    x = a*num
    c = ((3.0*(10**8))/(10**18))*10**10 # speed of light in meters per as
    w = (2*np.pi*c)/l
    afunc = np.sin(2*k*x-w*t)
    plt.figure(1)
    plt.plot(t,afunc)
    plt.xlabel("Time (as)")
    plt.ylabel("Intensity")
    plt.title("Plot of 100 Scattering X-Rays at 45 degrees")
    plt.legend() 
    asum = asum + afunc
plt.figure(2)
plt.plot(t,asum)
plt.xlabel("Time (as)")
plt.ylabel("Intensity")
plt.title("Plot of Sum of Scattering X-Rays at 45 degrees")
plt.show()

print(np.max(asum**2))

'''
#problem 3b

import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(0,1,100)
l = 1.54 #A
thetalist = np.linspace(5,85,800)
a = 2.84
asum = [0]*100
amplist = []
for num1 in thetalist:
    for num2 in range(1,101):
        theta =  num1
        rad = np.pi*theta/180
        k = ((2*np.pi)/l)*np.sin(rad)
        x = a*num2
        c = ((3.0*(10**8))/(10**18))*10**10 # speed of light in angstrom per as
        w = (2*np.pi*c)/l
        afunc = np.sin(2*k*x-w*t)
        asum = asum + afunc
    amp = (np.max(asum))**2
    amplist.append(amp)
    asum = [0]*100
twotheta = thetalist*2
plt.figure(2)
plt.plot(twotheta,amplist)
plt.xlabel("Two Theta Value (2*Theta)")
plt.ylabel("Intensity")
plt.title("Plot of Summed Diffracted X-rays With Moving Source From 5 Degrees to 87.5 degrees ")
plt.show()
'''
'''
#problem 4

import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(0,1,100)
l = 1.54 #A
thetalist = np.linspace(5,85,800)
a = 2.84
asum = [0]*100
amplist = []
for num1 in thetalist:
    for num2 in range(1,101):
        theta =  num1
        rad = np.pi*theta/180
        k = ((2*np.pi)/l)*np.sin(rad)
        x = a*num2
        c = ((3.0*(10**8))/(10**18))*10**10 # speed of light in angstrom per as
        w = (2*np.pi*c)/l
        afunc = np.sin(2*k*x-w*t)+np.sin(2*k*(x+(0.5*a))-w*t)
        asum = asum + afunc
    amp = (np.max(asum))**2
    amplist.append(amp)
    asum = [0]*100
twotheta = thetalist*2
plt.figure(2)
plt.plot(twotheta,amplist)
plt.xlabel("Two Theta Value (2*Theta)")
plt.ylabel("Intensity")
plt.title("Plot of Summed Diffracted X-rays BCC Crystal ")
plt.show()
'''