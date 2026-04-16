# Sensor Plotting Utilities

Generate publication-quality visualizations from synthetic temperature sensor data.

**Installation**

- Activate the project conda environment:

```bash
conda activate ece105
```

- Install the required packages (using `conda` or `mamba` is recommended):

```bash
conda install numpy matplotlib
# or
mamba install numpy matplotlib
```

**Usage**

Run the script to generate the example plots and save a combined PNG:

```bash
python generate_plots.py
```

By default the script uses seed `1847` and writes `sensor_analysis.png` in the
current directory.

**Example output**

- Scatter plot: time (0–10 s) on the x-axis and temperature (°C) on the y-axis for
     both sensors; markers and faint connecting lines show temporal evolution.
- Histogram: overlaid histograms (30 bins) of the two sensors with vertical dashed
     lines indicating each sensor's mean.
- Box plot: side-by-side box plots comparing the two sensor distributions and a
     horizontal dashed line showing the overall mean.

**AI tools used and disclosure**

I used copilot to do this and I did checked the code and tried to understand the code and how it work.
