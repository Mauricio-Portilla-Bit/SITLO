# This file contains the parameters for the hanging rope optimization.
# The shape of the rope is defined by the polynomial y(x) = a0 + a1*x + a2*x^2
# where x ranges from 0 to 1.
# Constraints:
# y(0) = 1  => a0 = 1
# y(1) = 0  => a0 + a1 + a2 = 0 => 1 + a1 + a2 = 0 => a1 + a2 = -1

import numpy as np
import os
import sys

# --- Curve generation logic ---

def get_y_values(a1, a2, x_values):
    """Calculates y(x) for a polynomial y(x) = a0 + a1*x + a2*x^2."""
    a0 = 1.0 # Fixed y-intercept based on y(0)=1
    return a0 + a1 * x_values + a2 * x_values**2

def get_y_prime_values(a1, a2, x_values):
    """Calculates y'(x) for a polynomial y(x) = a0 + a1*x + a2*x^2."""
    # y'(x) = a1 + 2*a2*x
    return a1 + 2 * a2 * x_values

# --- End of curve generation logic ---


# This file contains the parameters for the hanging rope optimization.
# Initial guess for coefficients (e.g., a parabola)
# This shape satisfies y(0)=1 and y(1)=0, and has some curvature.
# Modified parameters for the next iteration:
a1 = -0.8
a2 = -0.2

# These parameters will be modified by the optimization loop.
# The evaluation.py script reads these values.


if __name__ == "__main__":
    # Example usage for testing train.py directly
    # This would typically not be run by the main SITLO loop,
    # but is useful for direct testing of parameter definitions.
    
    # Use the parameters defined directly in this file
    current_a1 = a1
    current_a2 = a2
    
    # Define x interval for calculation
    x_start, x_end = 0.0, 1.0
    num_points = 100
    x_values = np.linspace(x_start, x_end, num_points)
    
    y_values = get_y_values(current_a1, current_a2, x_values)
    y_prime_values = get_y_prime_values(current_a1, current_a2, x_values)
    
    print("y(x) values (sample):", y_values[:5])
    print("y'(x) values (sample):", y_prime_values[:5])
    
    # If evaluation.py is meant to run this, it would call these functions.
    # For now, just demonstrating the curve generation.
