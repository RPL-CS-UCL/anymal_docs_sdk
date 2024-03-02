#!/usr/bin/env python3

from anymal_launch import load_config_with_argparse
from anymal_d import get_anymal_d_feature_toggle_descriptions

import rospy


def main():
    rospy.init_node('load_config')
    anybotics_pkg_found = False
    try:
        from anymal_d_anybotics import get_anymal_d_anybotics_feature_toggle_descriptions
        anybotics_pkg_found = True
    except (ImportError, ModuleNotFoundError):
        pass

    if anybotics_pkg_found:
        load_config_with_argparse("d", {**get_anymal_d_feature_toggle_descriptions(),
                                        **get_anymal_d_anybotics_feature_toggle_descriptions()})
    else:
        load_config_with_argparse("d", get_anymal_d_feature_toggle_descriptions())


if __name__ == '__main__':
    main()
