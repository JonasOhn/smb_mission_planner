import rospy
import yaml
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker, MarkerArray

import tf.transformations as tf
import rospy
from geometry_msgs.msg import Quaternion
import tf.transformations as tf

def euler_to_quaternion(roll, pitch, yaw):
    quat = tf.quaternion_from_euler(roll, pitch, yaw)
    return quat

def publish_marker_array_from_yaml(yaml_file, rate):
    # Read YAML file
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Create marker array
    marker_array = MarkerArray()

    # Create markers for each waypoint in YAML data
    for index, waypoint_key in enumerate(yaml_data['waypoints']):
        waypoint = yaml_data['waypoints'][waypoint_key]
        x = waypoint['x_m']
        y = waypoint['y_m']
        z = 0  # Assuming z coordinate is 0 for visualization

        # Create a marker with waypoint coordinates
        marker = Marker()
        marker.header.frame_id = 'map_o3d'
        marker.header.stamp = rospy.Time.now()
        marker.ns = 'my_namespace'
        marker.id = index
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        marker.pose.position = Point(x, y, z)
        euler_angles = [0, 0, waypoint['yaw_rad']]
        quaternion = euler_to_quaternion(*euler_angles)
        marker.pose.orientation = Quaternion(*quaternion)
        marker.scale.x = 0.5
        marker.scale.y = 0.15
        marker.scale.z = 0.15
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 1.0

        # Add marker to the marker array
        marker_array.markers.append(marker)

    # Initialize ROS node and publisher
    marker_pub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)

    # Loop and publish the marker array
    while not rospy.is_shutdown():
        marker_pub.publish(marker_array)
        rate.sleep()

    rospy.loginfo('Marker array publishing completed.')



# Example usage:
if __name__ == '__main__':
    rospy.init_node('marker_publisher_node')
    yaml_file_path = 'main_sim.yaml'
    publish_rate = rospy.Rate(1)  # 1 Hz publishing rate
    publish_marker_array_from_yaml(yaml_file_path, publish_rate)

