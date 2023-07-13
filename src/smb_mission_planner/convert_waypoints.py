import yaml
import numpy as np

with open('/home/jonas/rss/smb_catkin_ws/src/planning/smb_mission_planner/configs/missions/main.yaml', 'r') as file:
    missions_data = yaml.load(file, Loader=yaml.FullLoader)
print("waypoints:")
for waypoint in missions_data["waypoints"]:
    print("  " + waypoint + ":")
    x_m_str = str(-1 * round(missions_data["waypoints"][waypoint]["y_m"]) - 1.6)
    y_m_str = str(round(missions_data["waypoints"][waypoint]["x_m"], 2))
    yaw_str = str(round(((180/np.pi) * missions_data["waypoints"][waypoint]["yaw_rad"] + 80)*np.pi/180, 2))
    print("    x_m: " + x_m_str + "\n    y_m: " + y_m_str + "\n    yaw_rad: " + yaw_str)