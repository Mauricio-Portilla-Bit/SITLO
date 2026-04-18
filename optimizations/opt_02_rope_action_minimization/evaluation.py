import pandas as pd
import numpy as np # Needed for numerical integration
import os
import sys

# Import curve generation logic from train.py
# Assuming train.py is in the same directory as evaluation.py
try:
    from train import get_y_values, get_y_prime_values
except ImportError:
    print("Error: Could not import curve generation functions from train.py.")
    print("Ensure train.py is in the same directory or accessible in sys.path.")
    sys.exit(1)

def load_params_from_train_py(file_path="train.py"):
    # Construct the absolute path to train.py relative to the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_file_path = os.path.join(script_dir, file_path)
    
    params = {}
    try:
        with open(full_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value_str = line.split('=', 1)
                        key = key.strip()
                        value_str = value_str.strip()
                        try:
                            if value_str.startswith('[') and value_str.endswith(']'):
                                value = [float(v.strip()) for v in value_str[1:-1].split(',')]
                            elif value_str.startswith('(') and value_str.endswith(')'):
                                value = tuple(float(v.strip()) for v in value_str[1:-1].split(','))
                            else:
                                value = float(value_str)
                            params[key] = value
                        except ValueError:
                            params[key] = value_str
        return params
    except FileNotFoundError:
        print(f"Error: {full_file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading parameters from {full_file_path}: {e}")
        sys.exit(1)

def calculate_action(a1, a2): # Modified to accept a1, a2 directly
    """
    Calculates the Action of the hanging rope given parameters a1 and a2.
    This implementation assumes the rope shape is a polynomial y(x) = a0 + a1*x + a2*x^2,
    with fixed endpoints y(0)=1 and y(1)=0.
    The Action is approximated by the integral of potential energy along the arc length.
    Assume linear density rho = 1 and gravity g = 1 for simplicity.
    """
    a0 = 1.0 # Fixed y-intercept based on y(0)=1

    x_start, x_end = 0.0, 1.0
    num_points = 100
    x_values = np.linspace(x_start, x_end, num_points)
    
    y_values = get_y_values(a1, a2, x_values)
    y_prime_values = get_y_prime_values(a1, a2, x_values)
    
    ds_values = np.sqrt(1 + y_prime_values**2)
    integrand = y_values * ds_values
    action = np.trapz(integrand, x_values)
    
    return action

if __name__ == "__main__":
    # This script is executed by the SITLO optimization loop.
    # It should load parameters from train.py, calculate the metric using logic from train.py, and print it.
    
    # Load parameters from train.py (relative path from evaluation.py)
    params_dict = load_params_from_train_py("train.py")
    
    a1_coeff = params_dict.get('a1')
    a2_coeff = params_dict.get('a2')
    
    if a1_coeff is None or a2_coeff is None:
        print("Error: Missing expected parameters 'a1' or 'a2' in train.py for action calculation.")
        sys.exit(1)

    # Pass the coefficients to the calculation function
    try:
        action_metric = calculate_action(a1_coeff, a2_coeff)
        print(f"{action_metric}") # Print the metric value to stdout
    except Exception as e:
        print(f"Error during metric calculation: {e}")
        sys.exit(1)
