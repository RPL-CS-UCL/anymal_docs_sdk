#!/usr/bin/env python3

from stack_launcher import launch
import rospy


if __name__ == '__main__':
    rospy.init_node('anymal_lpc')
    launch("lpc", trigger_param="/config_loaded", use_cgroups=True)

