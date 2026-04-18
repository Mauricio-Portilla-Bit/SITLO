import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def plot(experiment_dir):
    results_path = os.path.join(experiment_dir, 'results', 'results.tsv')

    if not os.path.exists(results_path):
        print(f"Error: {results_path} not found.")
        sys.exit(1)

    try:
        df = pd.read_csv(results_path, sep='	')
        df = df.sort_values(by='iteration')

        plt.figure(figsize=(12, 7))

        step_x, step_y, step_tags = [], [], []
        scatter_x, scatter_y, scatter_tags = [], [], []
        
        if not df.empty:
            # Add the first point as the start of the optimized path
            step_x.append(df['iteration'].iloc[0])
            step_y.append(df['metric'].iloc[0])
            step_tags.append(df['tag'].iloc[0])

            for i in range(1, len(df)):
                current_iter = df['iteration'].iloc[i]
                current_metric = df['metric'].iloc[i]
                current_tag = df['tag'].iloc[i]
                
                prev_metric = df['metric'].iloc[i-1]

                # Check for improvement (lower metric)
                if current_metric < prev_metric:
                    # This point represents an improvement, add to step data
                    step_x.append(current_iter)
                    step_y.append(current_metric)
                    step_tags.append(current_tag)
                else:
                    # This point is not an improvement, add to scatter data
                    scatter_x.append(current_iter)
                    scatter_y.append(current_metric)
                    scatter_tags.append(current_tag)

            # Plot optimized steps in blue
            if step_x:
                plt.step(step_x, step_y, where='post', color='blue', label='Optimized Path (Steps)')
                # Annotate step points
                for idx, (it, met) in enumerate(zip(step_x, step_y)):
                    original_row = df[(df['iteration'] == it) & (df['metric'] == met)]
                    if not original_row.empty:
                        tag = original_row['tag'].iloc[0]
                        plt.annotate(tag, (it, met), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue')

            # Plot non-optimized scatter points in gray
            if scatter_x:
                plt.scatter(scatter_x, scatter_y, color='gray', label='Non-Optimized (Scattered)', alpha=0.7)
                # Annotate scatter points
                for idx, (it, met) in enumerate(zip(scatter_x, scatter_y)):
                    original_row = df[(df['iteration'] == it) & (df['metric'] == met)]
                    if not original_row.empty:
                        tag = original_row['tag'].iloc[0]
                        plt.annotate(tag, (it, met), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='gray')

        else: # Handle empty dataframe case
            print("No data found in results.tsv to plot.")
            return

        plt.title('SITLO Optimization Progress')
        plt.xlabel('Iteration')
        plt.ylabel('Metric Value')
        plt.legend()
        plt.grid(True)
        plt.tight_layout() 
        
        output_graph_path = os.path.join(experiment_dir, 'results', 'optimization_graph.png')
        plt.savefig(output_graph_path)
        print(f"Graph updated: {output_graph_path}")
    except Exception as e:
        print(f"Error plotting: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 plot_results.py <experiment_dir>")
        sys.exit(1)
    
    experiment_dir = sys.argv[1]
    plot(experiment_dir)
