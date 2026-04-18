import pandas as pd
import sys
import random

def run_evaluation():
    # Read current size from train.py
    with open('train.py', 'r') as f:
        content = f.read()
        try:
            # Simple extraction logic for the demonstration
            size_str = content.split('blk.set("size", ["')[1].split('"')[0]
            size = float(size_str)
            
            # Logic for detailed tag (based on change from baseline 0.1)
            diff = size - 0.1
            if diff > 0:
                tag = f"Expansion: Size increased by {diff:.2f}"
            elif diff < 0:
                tag = f"Contraction: Size decreased by {abs(diff):.2f}"
            else:
                tag = "Baseline"
                
        except Exception as e:
            print(f"Error parsing train.py: {e}")
            size = 0.1
            tag = "Unknown Change"
    
    # Simulate a metric based on size
    # Metric = -10 * (size - 0.5)^2 + 5
    metric = -10 * (size - 0.5)**2 + 5 + random.uniform(-0.1, 0.1)
    
    print(f"SITLO EVALUATION")
    print(f"Parameters: size={size}")
    print(f"METRIC: {metric}")
    print(f"TAG: {tag}")

if __name__ == "__main__":
    run_evaluation()
