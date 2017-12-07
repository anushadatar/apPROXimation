#!/usr/bin/env python

from modsim import *

def make_system(x, y, vx, vy, alpha):
    """
    """
    state = State(x, y, vx, vy)
    g = 9.8 * UNITS.meter / UNITS.second**2
    m = .175 * UNITS.kilogram # Mass of frisbee
    rho = 1.23  * UNITS.kilogram/UNITS.meter**3 # Density of air
    area = 0.0568 * UNITS.meter**2 # Surface area of frisbee
    CL0 = 0.1 # Lift coefficient alpha=0.
    CLA = 1.4 # Alpha-dependent lift coefficient
    # Drag coefficient when alpha = 0
    CDO = 0.08
    # Alpha-dependent drag coefficient
    CDA = 2.72 
    # Constant associated with launch angle.
    alpha_constant = -4
    # Launch angle (in degrees).
    alpha = alpha

    # Now that we have lots of constants, we can calculate the actual coefficients.
    # Lift coefficient.
    CL = CL0 + CLA*alpha_constant*math.pi/180
    # Drag coefficient.
    CD = CD0 + CDA*((alpha - alpha_constant) * math.pi/180)**2
    # Return our system, because real object oriented programming is "soooo overrated"
    return System(state, g=g, m=m, rho=rho, area=area, CL=CL, CD=CD)

def slope_func(state, t, system):
    """
    """
    x, y, vx, vy = state
    unpack(system)

    # Make some useful vectors.
    a_grav = Vector(a, -g)
    v = Vector(vx, vy)
    # Make some change vectors.
    dvydt = (rho*(vy**2)*area*(CL/2)/(m + g))
    dvxdt = (rho*(vx**2)*area*CD)
    return dvxdt, dvydt

system = make_system(0, 0, 10, 0, 10)
run_odeint(system, slope-func)
plot(system.results)    
