# SITLO: Simulation in the Loop Optimization

SITLO (Simulation in the Loop Optimization) is an automated, closed-loop computational architecture engineered to execute parametric discovery and inverse problem resolution across multiphysics domains. It follows the "Autoresearch" principle to iteratively modify designs and keep improvements based on scalar metrics. 

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/fefddb8a-e2c3-4458-a5d2-ee11f962badc" />

## Laboratories: MultiPhysics Simulators 
- COMSOL 

## CLI Workflow Automation

You can automate the management and execution of experiments using the following built-in workflows:

### 1. sitlo-setup-optimization-task
Creates the necessary directory structure and template files for a new optimization task.
*   **Usage**: Execute this within the root project directory.
*   **Prompt**: "Create a new optimization tasknamed <opt_name>. The goal is to optimize <parameter> to minimize/maximize <metric> based on the physical principles of <description>."

### 2. sitlo-run-optimization-task
Autonomously executes the optimization loop for a specific optimization directory.
*   **Usage**: Execute this after defining the physics in the optimization's folder.
*   **Prompt**: "Run the optimization for <opt_name>. 


## Project Structure

- optimizations/: Contains different optimization tasks.
    - opt_name/:
        - program.md: Problem definition and instructions.
        - evaluation.py: Runs the simulation and returns the metric.
        - train.py: The editable asset containing geometric parameters.
        - results/: Contains results.tsv and optimization_graph.png.

## Workflow

1.  The agent reads the hypothesis and modifies `train.py`.
2.  `evaluation.py` is executed to run the COMSOL simulation.
3.  The scalar metric is extracted and logged in `results/results.tsv` with a detailed tag.
4.  `plot_results.py` updates the optimization graph.

## Procedures

- [Setup New Optimization Task](workflows/setup-optimization-task.md)
- [Run Optimization Task](workflows/run-optimization-task.md)




