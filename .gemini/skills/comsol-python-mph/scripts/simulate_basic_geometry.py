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
# Example script for basic COMSOL simulation setup and execution.
# This script demonstrates initializing the MPH client, creating a model,
# adding basic geometry, setting parameters, running a study, and extracting a metric.

import mph
import os
import sys

def initialize_comsol_client():
    """Initializes the COMSOL client connection."""
    try:
        client = mph.start()
        print("COMSOL client initialized successfully.")
        return client
    except Exception as e:
        print(f"Error initializing COMSOL client: {e}")
        sys.exit(1)

def create_basic_model(client):
    """Creates a new COMSOL model and adds basic geometry and physics."""
    model = client.create('Model')
    print("New model created.")
    
    try:
        # Add a component
        comp = model.java.component('comp1')
        
        # Add geometry: a simple block
        geom = comp.geom('geom1')
        if not geom.java.getJavaObject().isBuilt(): # Check if geometry is already built
            geom.java.create('blk1', 'Block')
            geom.java.feature('blk1').set('size', ['1 [mm]', '1 [mm]', '1 [mm]'])
            geom.java.run()
            print("Basic block geometry created.")
        
        # Add a simple physics interface (e.g., Heat Transfer in Solids)
        # Note: Actual physics setup is highly dependent on simulation type.
        # You might need to use comp.physics('ht').create(...) for heat transfer.
        # For demonstration, we'll just print a message.
        print("Placeholder for physics setup. Adapt for specific simulation needs.")
        
        # Mesh and run study would follow here.
        # Example:
        # comp.mesh('mesh1').run()
        # model.solve('Study 1')
        
        return model
    except Exception as e:
        print(f"Error during simulation setup: {e}")
        return None

def set_simulation_parameters(model, params):
    """Sets simulation parameters in the COMSOL model."""
    if not params:
        print("No parameters provided to set.")
        return
    try:
        for name, value in params.items():
            model.parameter(name, value)
            print(f"Parameter '{name}' set to '{value}'.")
    except Exception as e:
        print(f"Error setting parameters: {e}")

def run_study(model, study_name="Study 1"):
    """Runs a specific study in the COMSOL model."""
    try:
        model.solve(study_name)
        print(f"Study '{study_name}' executed.")
    except Exception as e:
        print(f"Error running study '{study_name}': {e}")
        sys.exit(1)

def extract_mean_temperature(model):
    """Extracts the mean temperature from the simulation results."""
    try:
        # Example expression for mean temperature on a boundary or domain
        # This expression might need adjustment based on the actual physics setup.
        metric_expression = "dmean(T)" # Example: Mean temperature
        metric_unit = "K"
        metric = model.evaluate(metric_expression, metric_unit)
        print(f"Extracted metric: {metric} {metric_unit if metric_unit else ''}")
        return metric
    except Exception as e:
        print(f"Error extracting metric '{metric_expression}': {e}")
        return None

def save_model(model, output_path):
    """Saves the COMSOL model."""
    try:
        model.save(output_path)
        print(f"Model saved to {output_path}")
    except Exception as e:
        print(f"Error saving model to {output_path}: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    # --- Configuration ---
    # Path to load an existing .mph file, or None to create a new model.
    model_file_path = None 
    
    # Parameters to set in the model. These can be swept in optimization loops.
    simulation_params = {
        "heater_temp": "350 [K]",
        "material_density": "7850 [kg/m^3]"
    }
    
    # Name of the study to run (if not running all studies).
    study_name = "Study 1" 
    
    # Output path for saving the final model.
    output_model_path = "results/simulated_model.mph"

    # --- Workflow ---
    client = initialize_comsol_client()
    model = load_or_create_model(client, model_file_path)
    
    if model:
        model = configure_simulation(model, simulation_parameters)
        if model:
            run_simulation(model, study_name)
            metric_value = extract_metric(model, "dmean(T)", "K") # Example: Extract mean temperature
            
            if metric_value is not None:
                save_model(model, output_model_path)
                print(f"Simulation completed. Extracted metric: {metric_value} K")
            else:
                print("Failed to extract metric. Cannot proceed.")
        else:
            print("Model configuration failed, cannot proceed with simulation.")
    else:
        print("Model loading/creation failed, cannot proceed.")

    # Ensure the COMSOL client is managed properly.
    # client.disconnect() # Uncomment if explicit disconnection is required.
