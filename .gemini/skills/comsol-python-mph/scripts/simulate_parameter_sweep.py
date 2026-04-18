# MIT License
#
# Copyright (c) 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Example script demonstrating a parameter sweep in COMSOL simulations using MPH.
# This script initializes the client, loads a model, sets a parameter,
# runs a study multiple times with varying parameter values, and extracts a metric for each.

import mph
import os
import sys
import pandas as pd

def initialize_comsol_client():
    """Initializes the COMSOL client connection."""
    try:
        client = mph.start()
        print("COMSOL client initialized successfully.")
        return client
    except Exception as e:
        print(f"Error initializing COMSOL client: {e}")
        sys.exit(1)

def load_model(client, model_path):
    """Loads an existing MPH model."""
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        sys.exit(1)
    try:
        model = client.load(model_path)
        print(f"Model loaded from {model_path}")
        return model
    except Exception as e:
        print(f"Error loading model {model_path}: {e}")
        sys.exit(1)

def run_parameter_sweep(model, param_name, param_values, study_name=None):
    """
    Performs a parameter sweep by iterating through values for a given parameter,
    running the simulation for each, and returning the extracted metrics.
    """
    results = []
    
    print(f"Starting parameter sweep for '{param_name}'...")
    
    for value in param_values:
        try:
            # Set the parameter for the current iteration
            model.parameter(param_name, value)
            print(f"  Set '{param_name}' to '{value}'. Running simulation...")
            
            # Run the simulation study
            if study_name:
                model.solve(study_name)
            else:
                model.solve()
            
            # Extract the metric
            metric_expression = "dmean(T)" # Example: Mean temperature
            metric_unit = "K"
            metric = model.evaluate(metric_expression, metric_unit)
            
            if metric is not None:
                results.append({
                    "parameter_value": value,
                    "metric": metric,
                    "unit": metric_unit
                })
                print(f"  Simulation successful. Metric: {metric} {metric_unit}")
            else:
                print("  Failed to extract metric.")
                
        except Exception as e:
            print(f"  Error during simulation for '{param_name}' = '{value}': {e}")
            # Decide whether to continue sweep or stop on error
            continue # Continue to next parameter value
            
    return results

def save_results(results, output_path="sweep_results.csv"):
    """Saves the sweep results to a CSV file."""
    if not results:
        print("No results to save.")
        return
    try:
        df = pd.DataFrame(results)
        df.to_csv(output_path, sep='	', index=False)
        print(f"Parameter sweep results saved to {output_path}")
    except Exception as e:
        print(f"Error saving results to {output_path}: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    # --- Configuration ---
    # Path to an existing .mph file to load for the sweep.
    # If None, a new model will be created and configured (requires more setup).
    model_file_path = None # Example: "models/my_model.mph"
    
    # Parameter to sweep, its values, and the study to run.
    parameter_to_sweep = "frequency"
    parameter_values = [f"{f} [GHz]" for f in np.linspace(1, 5, 5)] # Sweep frequency from 1 to 5 GHz
    study_to_run = "Study 1" # Name of the study to execute
    
    # Output path for saving the sweep results.
    output_results_path = "results/parameter_sweep.tsv"

    # --- Workflow ---
    client = initialize_comsol_client()
    
    # If model_file_path is None, you'd need to add model creation/configuration here.
    # For this example, we assume a pre-existing model or template is loaded.
    # If starting from scratch, use client.create('Model') and add geometry/physics.
    if model_file_path is None:
        print("Error: Model path not specified. Cannot proceed with sweep.")
        # You would typically load a pre-configured model or create one here.
        # For demonstration, let's assume a model is available.
        # model = client.create('Model') 
        # configure_simulation(model, {}) # Add setup here if creating new
        sys.exit(1)
    else:
        model = load_model(client, model_file_path)

    sweep_results = run_parameter_sweep(model, parameter_to_sweep, parameter_values, study_to_run)
    save_results(sweep_results, output_results_path)

    # Optional: Save the final model state after the sweep
    # save_model(model, "results/swept_model.mph")

    print("Parameter sweep script finished.")
    # client.disconnect() # Uncomment if explicit disconnection is required.
