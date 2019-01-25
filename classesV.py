class VelocityProfile:
    def __init__(self, beta, mu0, n, R):
        self.beta, self.mu0, self.n, self.R = beta, mu0, n, R

    def value(self, r):
        beta, mu0, n, R = self.beta, self.mu0, self.n, self.R
        n = float(n)  # ensure float divisions
        v = (beta/(2.0*mu0))**(1/n)*(n/(n+1))*(R**(1+1/n) - r**(1+1/n))
        return v


v1 = VelocityProfile(R=1, beta=0.06, mu0=0.02, n=0.1)
from matplotlib.pylab import *
r = linspace(-10, 10, 50) # 50 points 

v = v1.value(r)
plot(r, v)

xlabel("r")
ylabel("v")
#legend(["t^2*exp(-t^2)", "t^4*exp(-t^2)"])
title("Plotting  curve v : r")
savefig("Velocity.png") # produce PNG
show()