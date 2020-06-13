# ====================================================================
# CSCC ENGR 1182 Summer 2020
# Energy Lab Part 2
# Energy Loss Calculations
# Author: John Choi
# ====================================================================

# ====================================================================
# GLOBALS
# ====================================================================

release_point_number: int = 1

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
def calculate_total_ball_energy(height: float, velocity: float):
    temp = (G_BALL_RADIUS ** 2) / (R_BALL_RADIUS ** 2)
    temp *= 1.0 / 5
    temp += 0.5
    temp *= (velocity ** 2)
    temp += height * GRAVITY
    result = BALL_MASS * temp
    return result


def calculate_energy_loss(velocity1: float, velocity2: float):
    temp1 = (G_BALL_RADIUS ** 2) / (R_BALL_RADIUS ** 2)
    temp1 *= 1.0 / 5
    temp1 += 0.5

    temp2 = (velocity1 ** 2) - (velocity2 ** 2)
    temp2 *= BALL_MASS
    return temp1 * temp2


# ====================================================================
# MAIN
# ====================================================================
