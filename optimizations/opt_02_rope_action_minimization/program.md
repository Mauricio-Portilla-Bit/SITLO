# SITLO Experiment: Rope Action Minimization (opt_02)

## Problem Definition
Find the shape of a hanging rope between two fixed points that minimizes the total "Action" of the system. The specific path is unknown a priori and must be discovered through optimization. This is a variational problem aiming to find the catenary curve.

## Citations and Context
- **Euler-Lagrange Principles**: Refer to `../../context_library/euler_lagrange.md` to understand how to apply the principle of least action to functionals representing the rope's properties (e.g., length and potential energy).
- **Variational Calculus**: The goal is to find the function $y(x)$ (rope shape) that minimizes the Action integral.

## Optimization Loop
1.  **Observe**: Read current `train.py` (parameters defining the rope's shape) and `results/results.tsv`.
2.  **Hypothesize**: Propose changes to the parameters in `train.py` that are expected to reduce the Action.
3.  **Implement**: Edit `train.py`.
4.  **Execute**: Run `python3 evaluation.py`.
5.  **Evaluate**: Capture the `METRIC` (Total Action) and `TAG` from the output.
6.  **Log**: Record (iteration, hypothesis, metric, tag) in `results/results.tsv`.
7.  **Visualize**: Run `python3 ../../plot_results.py`.
8.  **Ratchet**: Keep improvements only.
9.  **Repeat**.

## Parameters (to be defined in train.py)
- Initial guess for the rope shape (e.g., coefficients of a polynomial or a predefined curve form).
- Physical properties relevant to the Action calculation (e.g., linear density, gravity).

## Metric
- **Action**: The functional to be minimized. This will be calculated by `evaluation.py`.


## IMPORTANT INSTRUCTIONS AND CONSTRAINTS

**NEVER MODIFY THE PROGRAM.MD FILE AND THE EVALUATION.PY FILE** The evaluation.py file is used to evaluate the performance of the system and the program.md file is used to define the problem and the loop instructions. Do not modify them.

**CRASHES**: If a run crashes (OOM, or a bug, or etc.), use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period.

**NEVER EXPLORE OTHER EXPERIMENTS** Limit to the context of this experiment and files cited in this program.md file. Do not explore other experiments or files outside of this experiment.