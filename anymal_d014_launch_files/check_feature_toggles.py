#!/usr/bin/env python3

from anymal_launch import check_feature_toggles_for_generation
from anymal_d import get_anymal_d_feature_toggle_descriptions

import rospy


def main():
    rospy.init_node('check_feature_toggles')
    anybotics_pkg_found = False
    try:
        from anymal_d_anybotics import get_anymal_d_anybotics_feature_toggle_descriptions
        anybotics_pkg_found = True
    except (ImportError, ModuleNotFoundError):
        pass

    if anybotics_pkg_found:
        check_feature_toggles_for_generation("d", {**get_anymal_d_feature_toggle_descriptions(),
                                                   **get_anymal_d_anybotics_feature_toggle_descriptions()})
    else:
        check_feature_toggles_for_generation("d", get_anymal_d_feature_toggle_descriptions())

if __name__ == '__main__':
    main()
