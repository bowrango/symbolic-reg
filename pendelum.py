import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Pendulum rod lengths and masses
L1 = 1                 # (kg)
L2 = 1                 # (m)
m1 = 1                 # (kg)
m2 = 1                 # (kg)

# Initial angles and angular velocities of the double pendulum
theta1 = np.pi/4     # (rad.)
theta1dot = 0          # (rad./s)

theta2 = np.pi/2    # (rad.)
theta2dot = 0          # (rad./s)

# Gravitational acceleration
g = 9.81               # (m/s^2)

# Animation properties: 15 seconds at 60 frames per second -> 900 images
DURATION = 15
FPS = 60
dt = 1 / FPS

# Define the time range for calculations
t = np.arange(0, DURATION+dt, dt)


def derivative(y, t, L1, L2, m1, m2):
    """Returns the first derivative of y = theta1, z1, theta2, z2"""

    theta1, z1, theta2, z2 = y

    cos, sin = np.cos(theta1-theta2), np.sin(theta1-theta2)

    theta1dot = z1

    z1dot = (m2*g*np.sin(theta2)*cos - m2*sin*(L1*z1**2*cos + L2*z2**2) -
             (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*sin**2)

    theta2dot = z2

    z2dot = ((m1+m2)*(L1*z1**2*sin - g*np.sin(theta2) + g*np.sin(theta1)*cos) +
             m2*L2*z2**2*sin*cos) / L2 / (m1 + m2*sin**2)

    return theta1dot, z1dot, theta2dot, z2dot


# Initial conditions of system
y0 = np.array([theta1, theta1dot, theta2, theta2dot])

# Numerically integrate the equations of motion
y = odeint(derivative, y0, t, args=(L1, L2, m1, m2))

# Grab the theta vectors from the main matrix
theta1 = y[:, 0]
theta2 = y[:, 2]

# Convert the two bob positions to Cartesian coordinates
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)