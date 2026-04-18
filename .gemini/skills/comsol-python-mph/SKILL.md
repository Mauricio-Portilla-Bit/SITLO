---
name: comsol-python-mph
description: Automate COMSOL Multiphysics simulations using the MPH Python library. Use this skill to create geometries, run simulations, and extract scalar metrics for optimization loops. Trigger when users ask to interact with COMSOL models programmatically, run simulations, or extract data from MPH files.
---
# COMSOL Multiphysics Automation with MPH

This skill provides a workflow for automating COMSOL Multiphysics simulations using the MPH Python library. It enables tasks such as creating geometries, running simulations, and extracting scalar metrics for optimization loops.

## When to Use This Skill

Invoke this skill when users need to:
-   Interact with COMSOL models programmatically.
-   Run COMSOL simulations without manual GUI interaction.
-   Extract specific scalar metrics or data from MPH files or simulations.
-   Set up optimization loops involving COMSOL simulations.

## Workflow Overview

1.  **Initialize COMSOL Client**: Establish a connection to the COMSOL server using `mph.start()`.
2.  **Model Management**: Load existing `.mph` files or create new models programmatically.
3.  **Geometry and Physics Configuration**: Utilize the MPH Python API (via `model.java`) to define or modify geometries, physics, and studies.
4.  **Parameterization**: Set or sweep model parameters using `model.parameter(name, value)`.
5.  **Simulation Execution**: Run studies using `model.solve()`.
6.  **Data Extraction**: Evaluate expressions or extract metrics using `model.evaluate(expression, unit)`.
7.  **Optimization Loops**: Integrate simulation runs into broader optimization frameworks by extracting metrics and modifying parameters iteratively.

## Best Practices

-   **Leverage Java API**: For advanced model manipulation, use `model.java` to access the comprehensive COMSOL Java API. It's often useful to inspect COMSOL GUI actions and copy them as Java code.
-   **Parameter Sweeps**: Utilize parameterization for efficient exploration of the design space. See `scripts/simulate_parameter_sweep.py` for an example.
-   **Error Handling**: Implement robust error handling around simulation execution (`model.solve()`) to manage potential non-convergence or crashes.
-   **Performance Optimization**: Consider simplifying models, using coarser meshes, or time-boxing simulations during early optimization stages to speed up the process.

## Resources

-   **MPH API Reference**: Detailed documentation for the MPH Python library. (Refer to `references/mph_api.md`)
-   **Basic Simulation Template**: A starting template for basic simulation setup. (Refer to `assets/template.py`)
-   **Parameter Sweep Example**: Demonstrates running simulations with varying parameters. (Refer to `scripts/simulate_parameter_sweep.py`)
