from numpy import absolute
from numpy.random import normal
from numpy.random import uniform
from numpy import pi 
import numpy

class place_particle:
    def __init__(self, radius):
        self.theta = uniform(0, 2*pi)
        self.phi = uniform(-pi, pi)
        self.r = absolute(normal(0, 1))
        return

class distribute_particles:
    def __init__(self, n_particles, radius):
        self.n_particles = n_particles
        self.radius = radius
        self.thetas = uniform(0, 2*pi, n_particles)
        self.phis = uniform(-pi, pi, n_particles)
        self.spreads = absolute(normal(0, radius, n_particles))
        return