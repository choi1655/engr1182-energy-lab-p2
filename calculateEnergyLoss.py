# ====================================================================
# CSCC ENGR 1182 Summer 2020
# Energy Lab Part 2
# Energy Loss Calculations
# Author: John Choi
# ====================================================================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# ====================================================================
# CONSTANTS
# ====================================================================

G_BALL_RADIUS = 0.01272  # unit: m, geometric radius of the ball
R_BALL_RADIUS = 0.01018  # unit: m, effective rolling radius of the ball on the track
BALL_MASS = 0.0097  # unit: kg, mass of the ball
GRAVITY = 9.81  # unit: m/s^2, gravitational pull


# ====================================================================
# FUNCTIONS
# ====================================================================
def calculate_energy_loss(velocity1: float, velocity2: float) -> float:
    temp1 = (G_BALL_RADIUS ** 2) / (R_BALL_RADIUS ** 2)
    temp1 *= 1.0 / 5
    temp1 += 0.5

    temp2 = (velocity1 ** 2) - (velocity2 ** 2)
    temp2 *= BALL_MASS
    return temp1 * temp2


def calculate_g_force(v_in, v_out, r_h) -> float:
    temp = (v_in + v_out) / 2.0
    temp = temp ** 2
    average_g_force = temp / (r_h * GRAVITY)
    return average_g_force


def get_average(values) -> float:
    avg = 0
    for number in values:
        avg += number
    return avg / len(values)


def print_summary_table_1(avg_g_forces, energy_losses):
    print("Printing Table 1...\n")
    print("% 20s% 30s% 30s" % ("Release point Number", "Average G Force", "Energy Loss (Joules)"))
    print("--------------------------------------------------------------------------------")
    for i in range(0, len(avg_g_forces)):
        print("% 20d% 30f% 30f" % (i + 1, avg_g_forces[i], energy_losses[i]))

    print("--------------------------------------------------------------------------------")


def print_summary_table_2(energy_loss, avg_g_forces, energy_loss_actual):
    print("Printing Table 2...\n")
    print("% 20s% 30s% 30s% 40s" % (
        "Release Point", "E-Loss Calc (J)", "Average G Force", "Energy Loss actual - calc (J)"))
    print("------------------------------------------------------------------------------------------------------------------------")
    for i in range(0, len(energy_loss)):
        print("% 20d% 30f% 30f% 40f" % (i + 1, energy_loss[i], avg_g_forces[i], energy_loss_actual[i]))

    print("------------------------------------------------------------------------------------------------------------------------")


def make_plot(name, x, y, x_label, y_label):
    """
    Plot values with graph title name, x label, and y label using x and y values passed in. Exports the graph to pdf.
    :param name: title of the graph
    :param x: horizontal axis values
    :param y: vertical axis values
    :param x_label: label for horizontal axis
    :param y_label: label for vertical axis
    """
    path = "./" + name + ".pdf"
    with PdfPages(path) as export_pdf:
        # plot the points and line of best fit
        plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
        # label the x and y axis
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        # title of the graph
        plt.title(name)
        export_pdf.savefig()
        plt.show()


# ====================================================================
# MAIN
# ====================================================================

avg_g_forces = []
energy_losses = []
inlet_velocities = []
outlet_velocities = []
radii = [0.23, 0.2225, 0.25, 0.205]
avg_radius = get_average(radii)
# Release point 1
print("Release Point 1...\n")
sensor_1_velocities = [0.8133333, 0.953333, 0.89, 1.03, 0.946667]
sensor_2_velocities = [0.483333333, 0.833333333, 0.973333333, 1.0833333]
avg_sensor_1 = get_average(sensor_1_velocities)
avg_sensor_2 = get_average(sensor_2_velocities)
inlet_velocities.append(avg_sensor_1)
outlet_velocities.append(avg_sensor_2)
energy_loss = calculate_energy_loss(avg_sensor_1, avg_sensor_2)
print("Energy loss: % f" % energy_loss)
energy_losses.append(energy_loss)
avg_g_force = calculate_g_force(avg_sensor_1, avg_sensor_2, avg_radius)
avg_g_forces.append(avg_g_force)
print("Average G Force: % f" % avg_g_force)

# Release point 2
print()
print("Release Point 2...\n")
sensor_1_velocities = [1.433333, 1.363333, 1.54, 1.44, 1.2866667]
sensor_2_velocities = [0.833333, 0.87, 0.736667, 1.086667, 0.97]
avg_sensor_1 = get_average(sensor_1_velocities)
avg_sensor_2 = get_average(sensor_2_velocities)
inlet_velocities.append(avg_sensor_1)
outlet_velocities.append(avg_sensor_2)
energy_loss = calculate_energy_loss(avg_sensor_1, avg_sensor_2)
print("Energy loss: % f" % energy_loss)
energy_losses.append(energy_loss)
avg_g_force = calculate_g_force(avg_sensor_1, avg_sensor_2, avg_radius)
avg_g_forces.append(avg_g_force)
print("Average G Force: % f" % avg_g_force)

# Release point 3
print()
print("Release Point 3...\n")
sensor_1_velocities = [1.81, 1.66, 2.0033333, 1.7766667, 1.5566667]
sensor_2_velocities = [0.97333333, 0.9233333, 0.96, 1.22, 1.1033333]
avg_sensor_1 = get_average(sensor_1_velocities)
avg_sensor_2 = get_average(sensor_2_velocities)
inlet_velocities.append(avg_sensor_1)
outlet_velocities.append(avg_sensor_2)
energy_loss = calculate_energy_loss(avg_sensor_1, avg_sensor_2)
print("Energy loss: % f" % energy_loss)
energy_losses.append(energy_loss)
avg_g_force = calculate_g_force(avg_sensor_1, avg_sensor_2, avg_radius)
avg_g_forces.append(avg_g_force)
print("Average G Force: % f" % avg_g_force)

# Release point 4
print()
print("Release Point 4...\n")
sensor_1_velocities = [2.37, 2.13333, 2.51333, 2.233333, 2.04]
sensor_2_velocities = [1.0833333, 1.1866667, 1.103333, 1.2766667, 1.353333]
avg_sensor_1 = get_average(sensor_1_velocities)
avg_sensor_2 = get_average(sensor_2_velocities)
inlet_velocities.append(avg_sensor_1)
outlet_velocities.append(avg_sensor_2)
energy_loss = calculate_energy_loss(avg_sensor_1, avg_sensor_2)
print("Energy loss: % f" % energy_loss)
energy_losses.append(energy_loss)
avg_g_force = calculate_g_force(avg_sensor_1, avg_sensor_2, avg_radius)
avg_g_forces.append(avg_g_force)
print("Average G Force: % f" % avg_g_force)

# Print table 1
print()
print_summary_table_1(avg_g_forces, energy_losses)

# Plot energy losses versus inlet velocity for each release point
make_plot("Plot 1", energy_losses, inlet_velocities, "inlet velocity", "energy loss")
# Plot values of energy loss versus average G force
make_plot("Plot 2", avg_g_forces, energy_losses, "average G force", "energy loss")

# Energy losses from spreadsheets, release points 1 to 4 in order
energy_losses_from_spreadsheet = [0.002, 0.002, 0.002, 0.003]
for i in range(0, len(energy_losses)):
    energy_losses_from_spreadsheet[i] = energy_losses[i] - energy_losses_from_spreadsheet[i]

# Plot values of "energy loss actual-calc" versus average G-force obtained for each configuration, Plot 3
make_plot("Plot 3", avg_g_forces, energy_losses_from_spreadsheet, "average G force", "energy loss actual-calc")

# print table 2
print_summary_table_2(energy_losses, avg_g_forces, energy_losses_from_spreadsheet)