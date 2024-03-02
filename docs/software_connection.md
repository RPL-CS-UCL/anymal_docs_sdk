## Software Connection

### ROS Topic
##### Map, LiDAR scan, TF
<div align="center">
  <a href="">
    <img align="center" src="image/screenshot_map_tf.png" width="50%" alt="screenshot_map_tf">
  </a> 
</div>

##### Twist
<div align="center">
  <a href="">
    <img align="center" src="image/screenshot_twist_example.png" width="50%" alt="screenshot_twist_example">
  </a> 
</div>

##### Twist
<div align="center">
  <a href="">
    <img align="center" src="image/screenshot_twist_example.png" width="50%" alt="screenshot_twist_example">
  </a> 
</div>

```
/state_estimator/anymal_state: state of base and joint, using priproc data
/state_estimator/pose_in_odom: state in the odometry representation
/slam/pose/pose: state in the point cloud map using lidar
```

### ROS Rqt_graph
##### state_estimator
<div align="center">
  <a href="">
    <img align="center" src="image/screenshot_anymald_topic_state_estimator.png" width="40%" alt="screenshot_anymald_topic_state_estimator">
  </a> 
</div>

##### slam
<div align="center">
  <a href="">
    <img align="center" src="image/screenshot_anymald_topic_slam.png" width="50%" alt="screenshot_anymald_topic_slam">
  </a> 
</div>

##### path_planning
<div align="center">
  <a href="">
    <img align="center" src="image/screenshot_anymald_topic_path_planning.png" width="50%" alt="screenshot_anymald_topic_path_planning">
  </a> 
</div>

### Disable ROS-specific node
1. (Not recommended) Modify the parameter and change ```enabled: true``` as ```enabled: false``` (like search ```joy_manager```) in 
```/home/jjiao/robohike_ws/src/RPL-RoboHike/robot_docs_sdk/anymal_docs_sdk/anymal_common_config_files/config/default.yaml```