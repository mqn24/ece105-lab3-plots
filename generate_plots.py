"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic sensor temperature data.

    Parameters
    ----------
    seed : int
        Seed for the random number generator (used with
        ``numpy.random.default_rng``) to produce reproducible results.

    Returns
    -------
    sensor_a : ndarray, shape (200,)
        Simulated temperature readings from Sensor A in degrees Celsius.
    sensor_b : ndarray, shape (200,)
        Simulated temperature readings from Sensor B in degrees Celsius.
    timestamps : ndarray, shape (200,)
        Sorted timestamps in seconds uniformly sampled on the interval [0, 10].

    Notes
    -----
    The generated data matches the notebook: Sensor A ~ N(25, 3), Sensor B ~ N(27, 4.5),
    with 200 samples each. Timestamps are sampled uniformly and the arrays are
    sorted by timestamp so plotting shows temporal evolution.
    """
    rng = np.random.default_rng(seed)
    n = 200
    timestamps = rng.uniform(0, 10, size=n)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)
    order = np.argsort(timestamps)
    timestamps = timestamps[order]
    sensor_a = sensor_a[order]
    sensor_b = sensor_b[order]
    return sensor_a, sensor_b, timestamps
# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_scatter(ax, timestamps, sensor_a, sensor_b, *, seed=None):
    """Draw scatter plot of two sensors vs time onto an Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on. The function modifies this Axes in place.
    timestamps : array_like, shape (200,)
        Time values in seconds (assumed sorted) for the x-axis.
    sensor_a : array_like, shape (200,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : array_like, shape (200,)
        Temperature readings from Sensor B in degrees Celsius.
    seed : int, optional
        Optional seed used in the data generation; if provided it will be shown
        in the plot title for reproducibility/context. Default is None.

    Returns
    -------
    None

    Notes
    -----
    The visual style matches the notebook: colored markers for each sensor with
    faint connecting lines, axis labels with units, a legend, a grid, and a
    compact layout handled by the caller if desired.
    """
    # plot markers
    ax.scatter(timestamps, sensor_a, color='blue', s=30, alpha=0.8,
               label='Sensor A', edgecolors='none')
    ax.scatter(timestamps, sensor_b, color='orange', s=30, alpha=0.8,
               marker='s', label='Sensor B', edgecolors='none')
    # connecting lines for temporal evolution
    ax.plot(timestamps, sensor_a, color='blue', linewidth=0.8, alpha=0.6)
    ax.plot(timestamps, sensor_b, color='orange', linewidth=0.8, alpha=0.6)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    if seed is not None:
        ax.set_title(f'Sensor Readings vs Time (seed={seed})')
    else:
        ax.set_title('Sensor Readings vs Time')
    ax.legend()
    ax.grid(True)
def plot_histogram(sensor_a, sensor_b, timestamps, ax, *, bins=30, seed=None):
    """Draw overlaid histograms of two sensor temperature distributions on an Axes.

    Parameters
    ----------
    sensor_a : array_like, shape (n,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : array_like, shape (n,)
        Temperature readings from Sensor B in degrees Celsius.
    timestamps : array_like, shape (n,)
        Timestamps corresponding to the readings (unused by this plot,
        accepted for API consistency).
    ax : matplotlib.axes.Axes
        Axes object to draw the histogram on. Modified in place.
    bins : int or sequence, optional
        Number of histogram bins or bin edges. Default is 30.
    seed : int, optional
        Optional seed used in the data generation; if provided it will be shown
        in the plot title for reproducibility/context. Default is None.

    Returns
    -------
    None

    Notes
    -----
    Matches the notebook: plots Sensor A in blue and Sensor B in orange with
    transparency so both distributions are visible, and draws vertical dashed
    lines at each sensor's mean with a legend.
    """
    ax.hist(sensor_a, bins=bins, alpha=0.5, color='blue', label='Sensor A')
    ax.hist(sensor_b, bins=bins, alpha=0.5, color='orange', label='Sensor B')
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)
    ax.axvline(mean_a, color='blue', linestyle='--', linewidth=1,
               label=f'Sensor A mean = {mean_a:.2f} °C')
    ax.axvline(mean_b, color='orange', linestyle='--', linewidth=1,
               label=f'Sensor B mean = {mean_b:.2f} °C')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    if seed is not None:
        ax.set_title(f'Histogram of Sensor Readings (seed={seed})')
    else:
        ax.set_title('Histogram of Sensor Readings')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)


def plot_boxplot(sensor_a, sensor_b, timestamps, ax, *, seed=None):
    """Draw side-by-side box plots comparing two sensor distributions on an Axes.

    Parameters
    ----------
    sensor_a : array_like, shape (n,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : array_like, shape (n,)
        Temperature readings from Sensor B in degrees Celsius.
    timestamps : array_like, shape (n,)
        Timestamps corresponding to the readings (unused by this plot,
        accepted for API consistency).
    ax : matplotlib.axes.Axes
        Axes object to draw the box plot on. Modified in place.
    seed : int, optional
        Optional seed used in the data generation; if provided it will be shown
        in the plot title for reproducibility/context. Default is None.

    Returns
    -------
    None

    Notes
    -----
    Matches the notebook: creates side-by-side boxes for Sensor A and Sensor B,
    applies light fill colors, and draws a horizontal dashed line at the overall
    mean across both sensors.
    """
    data = [sensor_a, sensor_b]
    bp = ax.boxplot(data, labels=['Sensor A', 'Sensor B'], patch_artist=True)
    colors = ['lightblue', 'lightgreen']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    overall_mean = np.mean(np.concatenate(data))
    ax.axhline(overall_mean, color='gray', linestyle='--', linewidth=1,
               label=f'Overall mean = {overall_mean:.2f} °C')
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (deg C)')
    if seed is not None:
        ax.set_title(f'Side-by-side Box Plot of Sensor Readings (seed={seed})')
    else:
        ax.set_title('Side-by-side Box Plot of Sensor Readings')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)