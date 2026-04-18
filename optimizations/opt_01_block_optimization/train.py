import mph
import sys

def run_simulation():
    # 1. Start Client
    client = mph.start()
    
    # 2. Create/Load Model
    # For optimization, we often start from a baseline .mph file
    # or build it from scratch here.
    model = client.create('OptimizationModel')
    
    try:
        # 3. Define Geometry (Example: A simple block)
        # In a real loop, the agent will modify these lines
        geom = model.java.modelNode().create("comp1").geom().create("geom1", 3)
        blk = geom.feature().create("blk1", "Block")
        blk.set("size", ["0.2", "0.2", "0.2"]) # Iteration 1: Expansion
        geom.run("fin")
        
        # 4. Set Physics & Mesh
        # (Simplified for the template)
        
        # 5. Solve
        model.solve()
        
        # 6. Evaluate Metric
        # Replace 'metric_expression' with actual COMSOL expression
        metric = model.evaluate('1', '1') # Placeholder
        print(f"METRIC: {metric}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_simulation()
