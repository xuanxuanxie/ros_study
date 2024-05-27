#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from carla import Client, Location
import carla



def callback(data):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z
    client = Client('localhost', 2000)
    world = client.get_world()
    spectator = world.get_spectator()
    transform = carla.Transform(carla.Location(x, y, z), carla.Rotation(yaw=0))
    spectator.set_transform(transform)

rospy.init_node('carla_view', anonymous=True)
rospy.Subscriber("/carla/agent_0/odometry", Odometry, callback)
rospy.spin()
