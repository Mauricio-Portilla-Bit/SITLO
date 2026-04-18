# SITLO: Simulation in the Loop Optimization

You are an autonomous research agent optimizing a physical or computational system.

## Problem Definition
Optimize the block dimensions in `train.py` to maximize the performance metric returned by `evaluation.py`.

_Define the problem you want to solve. from the initial setup, if the setup does not define the optimization variables, define them here, based on the physics of the problem, just add the necessary information to the table below_

| Optimization Variable | Description |
| -------- | -------- |
| Metric to Optimize  | _Description of the metric to optimize: variable to optimize, how to optimize it (minimize or maximize), and the units of the metric_   |
| Parameter 1   | _Description of the parameter that can vary to optimize the metric_   |
| Parameter 2   | _Description of the parameter that can vary to optimize the metric_   |
| Parameter 3   | _Description of the parameter that can vary to optimize the metric_   |
s
## Problem Constraints
_If there is any relevant constraint specified in the prompt, add it here. For example a given size, a temperature, a condition, pressure, etc._

## Relevant Citations and Context
_If there is any useful context in the context library folder, cite the reference to the file or files here. If there is no context, don't add this section_

## Laboratory
_Based on the description of the setup prompt, determine which laboratory to use. The available laboratories are listed on the /laboratories folder with their resumes in markdown files. If no laboratory is suitable for the problem or the setup explicitly states not to use a laboratory, don't add this section_

## Skills 
_If a laboratory is used, list the skills that the laboratory provides that are relevant to the problem and enable the required skill for the laboratory. If no laboratory is used, don't add this section_


## Loop Instructions (DON'T MODIFY): 
1.  **Observe**: Read `train.py` and the history in `results/results.tsv`.
2.  **Hypothesize**: Propose a specific geometric change (e.g., "Increase width by 5%").
3.  **Implement**: Edit `train.py`.
4.  **Execute**: Run `python3 evaluation.py`.
5.  **Evaluate**: Extract the `METRIC` and the detailed `TAG` from the output.
6.  **Log**: Append (iteration, hypothesis, metric, tag) to `results/results.tsv`.
7.  **Visualize**: Run `python3 ../../plot_results.py` from within the experiment folder.
8.  **Ratchet**: 
    - If improved: Keep the change.
    - If worse: Revert `train.py`.
9.  **Repeat**.


## IMPORTANT INSTRUCTIONS AND CONSTRAINTS

**NEVER MODIFY THE PROGRAM.MD FILE AND THE EVALUATION.PY FILE** The evaluation.py file is used to evaluate the performance of the system and the program.md file is used to define the problem and the loop instructions. Do not modify them.

**CRASHES**: If a run crashes (OOM, or a bug, or etc.), use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period.

**NEVER EXPLORE OTHER EXPERIMENTS** Limit to the context of this experiment and files cited in this program.md file. Do not explore other experiments or files outside of this experiment.