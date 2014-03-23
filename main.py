#!/usr/bin/python

import numpy as np

from atom import *

natoms = 1000
# Parameters taken from C-C bond in AMBER
A = 1.09129369e-7 # ev nm^12
B = 0.00005328582 # ev nm^6

def simple_cubic_lattice(nx, ny, nz, a):
    lattice_points = []
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                point = np.array([a*i, a*j, a*k])
                lattice_points.append(point)
    return lattice_points

def twelve_six(A, B, r): 
    '''Returns value of Lennard-Jones potential A/r12 - B/r6'''
    r2 = r*r 
    r6 = r2 * r2 * r2
    r12 = r6 * r6
    return (A/r12) - (B/r6)

def twelve_six_force(A, B, r):
    """Returns the Lennard-Jones force"""
    r2 = r*r 
    r6 = r2 * r2 * r2
    r7 = r6 * r
    r12 = r6 * r6
    r13 = r12 * r 
    return -12*A/r13 + 6*B/r7

def pe(x):
    """Returns potential energy of system.

    Arguments:
    x -- (natoms x 3) Numpy array of atomic positions

    """
    sum = 0.0
    for i in range(natoms):
        for j in range(i+1, natoms):
            r = d(x[i], x[j])
            sum += twelve_six(A, B, r) 
    return sum

def f(x):
    """Returns force on each atom.

    Arguments:
    x -- (natoms x 3) Numpy array of atomic positions

    Returns:
    force -- (natoms x 3) Numpy array of atomic forces

    """
    force = np.zeros((natoms, natoms, 3))
    for i in range(natoms):
        for j in range(i+1, natoms):
            s  = np.abs(x[j] - x[i])
            fx = twelve_six_force(A, B, s[0])
            fy = twelve_six_force(A, B, s[1])
            fz = twelve_six_force(A, B, s[2])
            force[i][j] = [fx, fy, fz]
    return force


def d(x1, x2):
    s = x1 - x2
    return np.sqrt(np.dot(s, s))

def verlet(x):
    """Integrates the equations of motion and returns new particle
    positions."""
    xnew = 2*x - xold + dtsq*a

if __name__ == '__main__':
    carbon = Atom(12.0, 'C')
    x = simple_cubic_lattice(10, 10, 10, 1.0)
    print f(x) 


