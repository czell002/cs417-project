#! /usr/bin/env python3

"""
This module processes the peacewise linear interpolation of data from the
CPU Temperatures project.
"""


def _interpolate_point(
    x_0: float,
    x_1: float,
    y_0: float,
    y_1: float
) -> tuple[float, float]:
    """
    This function takes in 2 points from x and y, returning the interpolation/line between
    those points. The first float returned is the y-intercept, the second is the slope.
    """
    # print(f"x_0 = {x_0} ; x_1 = {x_1} ; y_0 = {y_0} ; y_1 = {y_1}")
    # Calculate the slope of the line between these two points
    m: float = (y_1 - y_0) / (x_1 - x_0)

    # Calculate the y-intercept for the line between these points
    b: float = y_0 - m * x_0

    # Return the slope and y-intercept of the line between these points
    return (b, m)


def interpolate(
    times_and_core_data: tuple[list[float], list[list[float]]]
) -> list[list[tuple[float, float]]]:
    """
    Create and return peacewise linear interpolations for each time chunk for each list
    of core temps provided
    
    Args:
        times_and_core_data: A tuple containing the parsed time data and core temperature data.
        This tuple must contain a list of floats representing the times in the first slot, and
        a list of 4 lists of floats representing the temperature readings at those times for
        4 different cores
    
    Returns:
        core_interpolations: A list of all 4 core's peacewise linear interpolations. For each
        data point, the first float is the y-intercept, and the second is the slope.
        
    """
    times, core_data = times_and_core_data

    core_interpolations: list[list[tuple[float, float]]] = []
    
    for core_number, core_n_data in enumerate(core_data):
        # Evaluate the interpolation of this core for all times
        core_n_interpolation: list[tuple[float, float]] = []
        previous_core_reading: float = core_n_data[0]
        for time, core_reading in list(zip(times, core_data[core_number]))[1:]:
            b, m = _interpolate_point(time - 30, time, previous_core_reading, core_reading)
            core_n_interpolation.append((b, m))
            previous_core_reading = core_reading
        core_interpolations.append(core_n_interpolation)
    return core_interpolations

    
    
