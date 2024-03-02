#!/usr/bin/env python3

import sys
sys.path.append('../sdk/anymal-research-software')

from anymal.anymal.anymal_launch.src.anymal_launch.anymal_launch import get_ros_launch, launch_sim
from anymal_d import get_anymal_d_feature_toggle_descriptions

import rospy


def main():
	ros_launch = get_ros_launch() # Creates ROS master on the fly.
	rospy.init_node('anymal_sim')
	anybotics_pkg_found = False
	try:
		from anymal_d_anybotics import get_anymal_d_anybotics_feature_toggle_descriptions
		anybotics_pkg_found = True
	except (ImportError, ModuleNotFoundError):
		pass
		
	if anybotics_pkg_found: # NOTE(gogojjh): default: False
		launch_sim("d", {**get_anymal_d_feature_toggle_descriptions(),
										 **get_anymal_d_anybotics_feature_toggle_descriptions()}, ros_launch=ros_launch)
	else:
		print(f"***** DEBUG: Get description: {get_anymal_d_feature_toggle_descriptions()}")
		launch_sim("d", get_anymal_d_feature_toggle_descriptions(), ros_launch=ros_launch)


if __name__ == '__main__':
	main()
