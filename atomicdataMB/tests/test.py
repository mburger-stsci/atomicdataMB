from atomicdataMB import gValue, RadPresConst
import astropy.units as u
import matplotlib.pyplot as plt


g2 = gValue('Na', 5891, 0.352*u.au)
g1 = gValue('Na', 5897*u.AA, 0.352*u.au)

#plt.plot(g2.velocity, g2.g)
#plt.plot(g1.velocity, g1.g)
#plt.show()

#rr = RadPresConst('Na', 0.3*u.au)
#plt.plot(rr.velocity, rr.accel)
#plt.show()
