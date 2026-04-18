# Variational Principles and the Euler-Lagrange Equation

## The Principle of Least Action
The Principle of Least Action states that the path taken by a physical system is the one that minimizes (or makes stationary) the Action functional $S$.

$$S = \int_{t_1}^{t_2} L(q, \dot{q}, t) dt$$

Where $L$ is the Lagrangian, typically $L = T - V$ (Kinetic - Potential Energy).

## Euler-Lagrange Equation
For a functional of the form $J[y] = \int_{a}^{b} f(x, y, y') dx$, the function $y(x)$ that minimizes $J$ must satisfy:

$$\frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) = 0$$

## Application to Curvature and Geodesics
When seeking the shortest path (or minimal "cost" path) on a surface or under a specific potential, the problem is often reduced to finding the curvature function $y(x)$ that satisfies the Euler-Lagrange equations for the specific energy or distance functional of the system.
