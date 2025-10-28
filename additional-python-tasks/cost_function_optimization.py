import numpy as np
from scipy.optimize import minimize

def find_closest_waypoint(car_pos, waypoints):
    distances = np.linalg.norm(waypoints - car_pos, axis=1)
    return np.argmin(distances)


def car_sim(v0, psi0, control_vars, dt=0.02):

    velocities = [v0]
    headings = [psi0]
    
    for k in range(0, len(control_vars), 2):
        v_next = control_vars[k]
        psi_next = control_vars[k + 1]
        velocities.append(v_next)
        headings.append(psi_next)
    
    return np.array(velocities), np.array(headings)

def cost_total(control_vars):

    v_des = 10.0
    v0 = 5.5
    psi0 = np.deg2rad(0)
    
    car_pos = np.array([1.0, 1.0])
    waypoints = np.array([
        [1.0, 1.0],
        [0.9, 2.0],
        [0.9, 3.0],
        [1.0, 4.1],
        [1.7, 5.0],
        [2.3, 6.0]
    ])
    idx = find_closest_waypoint(car_pos, waypoints)
    if idx < len(waypoints) - 1:
        next_wp = waypoints[idx + 1]
    else:
        next_wp = waypoints[idx - 1]
    psi_des = np.arctan2(next_wp[1] - waypoints[idx][1], next_wp[0] - waypoints[idx][0])

    velocities, headings = car_sim(v0, psi0, control_vars)

    w1, w2, w3 = 1.0, 2.0, 0.5
    total_cost = 0.0
    for k in range(len(velocities)):
        e_v = (velocities[k] - v_des) ** 2
        e_angle = (headings[k] - psi_des)
        e_angle_sq = e_angle ** 2
        e_dist = abs(np.sin(e_angle)) * velocities[k]

        total_cost += (w1 * e_v) + (w2 * e_angle_sq) + (w3 * e_dist ** 2)

    return total_cost

x0 = np.array([6, np.deg2rad(5),
               7, np.deg2rad(10),
               8, np.deg2rad(15),
               9, np.deg2rad(20)])

bounds = [(0, 15), (np.deg2rad(-90), np.deg2rad(90))] * 4

result = minimize(cost_total, x0, method='SLSQP', bounds=bounds)

print(f"Total cost: {result.fun:.4f}\n")

v0 = 5.5
psi0 = np.deg2rad(0)
car_pos = np.array([1.0, 1.0])
waypoints = np.array([
    [1.0, 1.0],
    [0.9, 2.0],
    [0.9, 3.0],
    [1.0, 4.1],
    [1.7, 5.0],
    [2.3, 6.0]
])
idx = find_closest_waypoint(car_pos, waypoints)
if idx < len(waypoints) - 1:
    next_wp = waypoints[idx + 1]
else:
    next_wp = waypoints[idx - 1]
psi_des = np.arctan2(next_wp[1] - waypoints[idx][1], next_wp[0] - waypoints[idx][0])
psi_des_deg = np.rad2deg(psi_des)

opt_control_vars = result.x
velocities, headings = car_sim(v0, psi0, opt_control_vars)

print(f" Desired heading from waypoints: {psi_des_deg:.2f}°\n")

print(" Optimal Control Variables per timestep:")
for i in range(4):
    v_opt = opt_control_vars[2 * i]
    psi_opt = np.rad2deg(opt_control_vars[2 * i + 1])
    print(f"Timestep {i + 1}:  Velocity = {v_opt:.3f} m/s      Heading = {psi_opt:.2f}°")
print("\n")

print(" Simulated Velocity and Heading Progression :")

for i in range(len(velocities)):
    print(f"Step {i}:  Velocity = {velocities[i]:.3f} m/s      Heading = {np.rad2deg(headings[i]):.2f}°")
