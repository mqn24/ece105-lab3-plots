"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np


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
